from src.bingo import carton

def test_no_menor_15():
	carton1 = carton()
	contador = 0
	for fila in carton1:
		for celda in fila:
			contador += celda
	assert contador >= 15

def test_no_mayor_15():
	carton1 = carton()
	contador = 0
	for fila in carton1:
		for celda in fila:
			contador += celda
	assert contador <= 15

def test_dimensiones():
	carton1 = carton()
	contador_x = 0
	for fila in carton1:
		contador_y = 0
		contador_x += 1
		for celda in fila:
			contador_y += 1
		assert contador_y == 9

	assert contador_x == 3

def test_columnas_ocupadas():
	carton1 = carton()
	contador = 0
	for i in range(9):
		contador = 0
		contador += carton1[0][i]
		contador += carton1[1][i]
		contador += carton1[2][i]
		assert contador > 0





