# SQL-Hacks
Scripts que me han ayudado en el proceso de auditoria de un servidor Data marshall


|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||Script para obtener información de los JOBs de SQL Server en varios servidores


Este script en Python permite obtener información de los JOBs (trabajos) programados en SQL Server en varios servidores y guardarla en un archivo de texto (.txt).

|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||Requisitos
>>>>>>>>>>>>>>>>>>>>>>Python 3.x
>>>>>>>>>>>>>>>>>>>>>>módulo pyodbc (para conectarse a SQL Server)

|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||Uso
>>>>>>>>>>>>>>>>>>>>>>Descargar el archivo HistorialJobSQLServer.py en su equipo.

>>>>>>>>>>>>>>>>>>>>>>Instalar el módulo pyodbc a través del siguiente comando:
----------------------pip install pyodbc
>>>>>>>>>>>>>>>>>>>>>>Editar el archivo HistorialJobSQLServer.py y agregar la información de los servidores de SQL Server que desea consultar. Por ejemplo:

|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||Conexiones a los server 

servers = [{'name': 'servidor1','host': 'localhost','port': '1433','database': 'mi_bd','user': 'mi_usuario','password': 'mi_contraseña'}, 
           {'name': 'servidor2','host': 'localhost','port': '1433','database': 'mi_bd','user': 'mi_usuario','password': 'mi_contraseña'}]
>>>>>>>>>>>>>>>>>>>>>>Ejecutar el archivo HistorialJobSQLServer.py con el siguiente comando:
----------------------python HistorialJobSQLServer.py

El script generará un archivo de texto llamado datos.csv en el mismo directorio donde se encuentra el archivo HistorialJobSQLServer.py. Este archivo contendrá la información de los 
JOBs programados en los servidores de SQL Server especificados en el paso 3.
|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||Notas

Este script utiliza la librería pyodbc para conectarse a SQL Server. Asegúrese de tener instalado el controlador ODBC adecuado para SQL Server en su equipo.

La información de los servidores de SQL Server se almacena en una lista de diccionarios. Si necesita agregar o quitar servidores, simplemente edite esta lista en el archivo HistorialJobSQLServer.py.

El archivo de texto generado (datos.csv) contiene información sobre los JOBs de SQL Server en formato CSV (valores separados por comas). Puede abrir este archivo en Excel u otro programa de hoja de cálculo para ver la información de forma más legible.