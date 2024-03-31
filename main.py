import pandas as pd
import requests
import config
import psycopg2
from datetime import datetime
from psycopg2 import sql

# API gratuita de Alpha Vantage
API_KEY = config.API_KEY
HOST = config.HOST
PORT = config.PORT
DBNAME = config.DBNAME
USER = config.USER
PASSWORD = config.PASSWORD



# Función para obtener los datos de un stock en específico y limpiarlos
def get_and_clean_stock_data(symbol):
    url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={API_KEY}"
    response = requests.get(url)
    data = response.json()
    
    # Extraer y limpiar los datos
    time_series_data = data.get('Time Series (Daily)', {})
    if not time_series_data:
        return None
    # Convertir los datos a un DataFrame
    df = pd.DataFrame(time_series_data).T.reset_index()
    df.columns = ['date', 'open_price', 'high_price', 'low_price', 'close_price', 'volume']

    # Seleccionar la fila más reciente (dato más actual)
    latest_data = df.iloc[0]
    
    # Agregar la columna 'symbol'
    latest_data['symbol'] = symbol
    # Obtener la fecha y hora actual
    current_timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    latest_data['ingest_timestamp'] = current_timestamp
    print (latest_data)
    return latest_data


# Función para verificar si existe la tabla en la base de datos    
def create_table_if_not_exists(cur):
    create_table_query = sql.SQL('''
    CREATE TABLE IF NOT EXISTS stock_data (
        symbol VARCHAR(10),
        date DATE,
        open_price FLOAT,
        high_price FLOAT,
        low_price FLOAT,
        close_price FLOAT,
        volume INT,
        ingest_timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        PRIMARY KEY (symbol, date)
    );
    ''')
    cur.execute(create_table_query)




# Obtener datos de un símbolo específico
symbol = "AMZN"
stock_data = get_and_clean_stock_data(symbol)

if stock_data is not None and not stock_data.empty:
    # Crear la conexión a la base de datos con psycopg2
    conn = psycopg2.connect(
        host=HOST,
        port=PORT,
        dbname=DBNAME,
        user=USER,
        password=PASSWORD
    )
    
  
    # Generar SQL para insertar datos
    insert_query = """
    INSERT INTO stock_data (date, open_price, high_price, low_price, close_price, volume, symbol, ingest_timestamp)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """
    
    # Crear un cursor para ejecutar comandos SQL
    cur = conn.cursor()
    
    # Crear la tabla si no existe
    create_table_if_not_exists(cur)

    # Verificar si el último dato ya está en la base de datos
    cur.execute("SELECT EXISTS (SELECT 1 FROM stock_data WHERE symbol = %s AND date = %s)", (symbol, stock_data['date']))
    exists = cur.fetchone()[0]

    if not exists:
        # Ejecutar el comando SQL de inserción
        cur.execute(insert_query, tuple(stock_data))
        # Confirmar los cambios
        conn.commit()
    
    cur.close()
    conn.close()
    print("Los datos se han cargado exitosamente en Redshift.")
else:
    print("No se encontraron datos para el símbolo especificado.")




