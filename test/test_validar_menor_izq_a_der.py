from src.bingo import menor_izq_a_der # agrego la funcion menor_izq_a_der de /src/bingo.py
from test.test_celdas import carton # agrego la funcion que crea el carton de prueba

def test_menor_izq_a_der():
	assert menor_izq_a_der(carton())
