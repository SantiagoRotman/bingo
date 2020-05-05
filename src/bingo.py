#Compruebo que la cantidad de celdas ocupadas sean meyor o igual a 15
def no_menor_15(carton1):
	contador = 0
	for fila in carton1:
		for celda in fila:
			if celda != 0:
				contador += 1
	return contador >= 15

#Compruebo que la cantidad de celdas ocupadas sean menor o igual a 15
def no_mayor_15(carton1):
	contador = 0
	for fila in carton1:
		for celda in fila:
			if celda != 0:
				contador += 1
	return contador <= 15

#Compruebo que las dimenciones sean 9x3.
def dimensiones(carton1):
	contador_x = 0
	for fila in carton1:
		contador_y = 0
		contador_x += 1
		for celda in fila:
			contador_y += 1
		if contador_y != 9:
			return False
	return contador_x == 3

#Compruebo que ninguna columna este vacia
def columnas_ocupadas(carton1):
	contador = 0
	for i in range(9):
		contador = 0
		if carton1[0][i] != 0:
			contador += 1
		if carton1[1][i] != 0:
			contador += 1
		if carton1[2][i] != 0:
			contador += 1
		if contador == 0:
			return False
		return True
