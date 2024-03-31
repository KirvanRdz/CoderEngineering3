Este script en Python es una herramienta de ETL (Extracción, Transformación, Carga) 
diseñada para obtener datos de una API externa e insertarlos en una base de datos Amazon Redshift. 
Específicamente, recupera datos de acciones de la API de Alpha Vantage e inserta estos datos en una tabla Redshift llamada stock_data.

Requisitos Previos:
1. Python 3.x instalado.
2. Paquetes de Python necesarios: pandas, requests, psycopg2, python-dotenv
3. Acceso a una clave de API de Alpha Vantage (https://www.alphavantage.co/support/)
4. Acceso a un clúster Amazon Redshift.
5. Credenciales y detalles de configuración de la base de datos necesarios (host, puerto, nombre de la base de datos, nombre de usuario, contraseña).

Instalación:
1. Clona o descarga el repositorio que contiene el script.
2. Asegúrate de que todos los paquetes de Python requeridos estén instalados. Puedes instalarlos usando: 
    "pip install -r requirements.txt"
    Esto instalará todas las bibliotecas listadas en el archivo requirements.txt
4. Configura los detalles de conexión para tu clúster Amazon Redshift y API de Alpha Vantage en
   el archivo .env_example, despues renombra el archivo dejandolo como ".env"

Uso:
1. Ejecuta el script Python main.py
2. El script recuperará los datos de acciones más recientes para el símbolo especificado (en este caso, "AMZN") de la API de Alpha Vantage.
3. Si se recuperan datos correctamente, se va a verificar primero si existe la tabla "stock_data" de tu base de datos Redshift, en caso que no exista se crea. 
3. Despues intentará insertar los datos en la tabla stock_data.
4. Si los datos ya están presentes en la base de datos para la misma fecha y símbolo, no se insertarán nuevamente.
5. El script imprimirá un mensaje indicando si los datos se cargaron correctamente en Redshift o si no se encontraron datos para el símbolo especificado.