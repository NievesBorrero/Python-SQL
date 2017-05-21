# -*- coding: utf-8 *-*

import MySQLdb

def ejecutarConsulta(consulta=''):
	conexion = MySQLdb.connect('localhost', 'root', '', 'empleados')  # Abro la conexión
	cursor= conexion.cursor()
	cursor.execute(consulta)
	if consulta.upper().startswith('SELECT'):
		datos = cursor.fetchall()
	else:
		#conexion.commit()
		datos = none
	cursor.close()
	conexion.close()
	return datos

def head(title):
	return '<html><head><title>'+title+'</title></head><body>\n'

def parrafo(cadena):
	return '<p>'+cadena+'</p>\n'

def encabezado(cadena):
	return '<h1>'+cadena+'</h1>'

def tabla (filas):
	temp = '<table border="1">\n'

	for fila in filas:
		temp= temp + '<tr>'
		for celda in fila:
			temp= temp+ '<td>'+ str(celda)+ '<td>\n'
		temp= temp+'</tr>\n'
	return temp+ '</table>\n'

def final():
	return '</body> </html>'

#Escribimos el fichero
fichero= open('empleados.html', 'w')
fichero.write(head('Empleados'))
fichero.write(encabezado('EMPLEADOS'))
fichero.write(parrafo('Lista de empleados ordenados por apellido'))
fichero.write(tabla(ejecutarConsulta('SELECT * FROM EMPLEADOS ORDER BY apellido')))
fichero.write(final())
fichero.close()
