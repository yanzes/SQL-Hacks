import pyodbc
import csv
# selecciona los server que se van a Consultar 
servers = ['server1',
           'server2',
           'server3',
           'server4',
           ]
#Conexion a los server (se realiza mediante Windows Authentication)
for server in servers:
    cnxn = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};'
        f'SERVER={server};'
        'Trusted_Connection=yes;'
        f'DATABASE=master;'
    )
#Realiza la consulta a las tablas del sistema en las cuales se evidencia el historial de los JOBs 
    cursor = cnxn.cursor()
    cursor.execute('SELECT TOP 10 j.name, h.run_date, h.run_time, h.run_duration,h.run_status, h.message, h.server '
                   'FROM msdb.dbo.sysjobhistory h '
                   'INNER JOIN msdb.dbo.sysjobs j ON h.job_id = j.job_id '
                   'WHERE h.step_id = 0 '
                   'ORDER BY h.run_date DESC, h.run_time DESC')
#Realiza el proceo de informacion en un archivo CSV
    with open('resultado.csv', 'a', newline='') as archivo_csv:
        escritor_csv = csv.writer(archivo_csv, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        # Encabezado del archivo CSV
        encabezado = ['Nombre del trabajo', 'Fecha de ejecución', 'Hora de ejecución', 'Duración de ejecución','status', 'Mensaje', 'Server']
        escritor_csv.writerow(encabezado)

        # Escritura de los datos en el archivo CSV
        for row in cursor:
            # Obtener duración en minutos
            duracion_minutos = int(row[3]) / 60

            # Agregar información al archivo CSV
            fila = [row[0], row[1], row[2], duracion_minutos, row[4], row[5]]
            escritor_csv.writerow(fila)
            print("se esta creando el reporte")
#Cierra la conexcion y Finaliza el proceso. 
    cnxn.close()

print("Finalizo el proceso consulte la información en la ruta del script")