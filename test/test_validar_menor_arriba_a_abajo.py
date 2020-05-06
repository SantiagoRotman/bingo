from src.bingo import menor_arriba_a_abajo # agrego la funcion menor_arriba_a_abajo de /src/bingo.py
from test.test_celdas import carton # agrego la funcion que crea el carton de prueba

def test_menor_arriba_a_abajo():
	assert menor_arriba_a_abajo(carton())
