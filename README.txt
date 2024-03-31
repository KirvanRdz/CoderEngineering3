Este script en Python es una herramienta de ETL (Extracción, Transformación, Carga) 
diseñada para obtener datos de una API externa e insertarlos en una base de datos Amazon Redshift. 
Específicamente, recupera datos de acciones de la API de Alpha Vantage e inserta estos datos en una tabla Redshift llamada stock_data.

Requisitos Previos:
1. Docker instalado en tu sistema. Puedes descargarlo desde https://docs.docker.com/engine/install/
2. Acceso a una clave de API de Alpha Vantage (https://www.alphavantage.co/support/)
4. Acceso a un clúster Amazon Redshift.
5. Credenciales y detalles de configuración de la base de datos necesarios (host, puerto, nombre de la base de datos, nombre de usuario, contraseña).

Configuración:
1. Clona o descarga el repositorio en tu maquina local.
2. Asegúrate de tener un archivo .env en el directorio raíz del repositorio. Este archivo debe contener las variables de entorno necesarias para la ejecución del script, 
    como: API_KEY (clave de API de Alpha Vantage), HOST, PORT, DBNAME, USER, PASSWORD.

Ejecución del script con Docker:
1. Abre una terminal y navega hasta el directorio raíz del repositorio clonado.

2. Construye la imagen Docker ejecutando el siguiente comando: "docker build -t nombre_imagen ."
    Reemplaza "nombre_imagen" con el nombre que desees darle a tu imagen.

3. Una vez que la imagen se haya construido correctamente, puedes ejecutar el contenedor con el siguiente comando: "docker run --env-file .env nombre_imagen"
    Esto iniciará el script dentro del contenedor Docker, utilizando las variables de entorno especificadas en el archivo .env.

4. El script obtendrá y limpiará los datos de las acciones de la API de Alpha Vantage y los cargará en la base de datos Redshift según la configuración proporcionada en el archivo .env.


