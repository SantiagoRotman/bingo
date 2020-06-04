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

#Compruebo que ninguna columna este vacia o completa
def columnas_ni_vacias_ni_llenas(carton1):
	contador = 0
	for i in range(9):
		contador = 0
		if carton1[0][i] != 0:
			contador += 1
		if carton1[1][i] != 0:
			contador += 1
		if carton1[2][i] != 0:
			contador += 1
		if contador == 0 or contador == 3:
			return False
	return True

#Compruebo que los numeros esten entre el uno y el noventa
def entre_1_y_90(carton1):
	for fila in carton1:
		for celda in fila:
			if celda < 0 or celda >= 90:
				return False
	return True

def menor_izq_a_der(carton):
	aux = -1
	for fila in carton:
		aux = -1
		for celda in fila:
			if celda <= aux and celda != 0:
				return False
			if celda != 0:
				aux = celda
	return True

def menor_arriba_a_abajo(carton):
	for i in range(9):
		if carton[0][i] >= carton[1][i] and carton[1][i] != 0:
			return False
		if carton[1][i] >= carton[2][i] and carton[2][i] != 0:
			return False
		if carton[0][i] >= carton[2][i] and carton[2][i] != 0:
			return False
	return True

def no_repetidos(carton):
	numeros = set()
	for fila in carton:
		for celda in fila:
			if (celda in numeros) and celda != 0:
				return False
			numeros.add(celda)
	return True

def filas_con_5(carton):
	for fila in carton:
		ocupadas = 0
		for celda in fila:
			if celda != 0:
				ocupadas += 1
		if ocupadas != 5:
			return False
	return True

def no_tres_consecutivas_vacias_o_llenas(carton):
	for b in range(3):
		for i in range(6):
			ocupadas = 0;
			if carton[b][i] != 0:
				ocupadas += 1
			if carton[b][i+1] != 0:
				ocupadas += 1
			if carton[b][i+2] != 0:
				ocupadas += 1
			if ocupadas == 0 or ocupadas == 3:
				return False
	return True
