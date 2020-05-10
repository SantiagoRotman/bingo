from src.bingo import no_repetidos # agrego la funcion no_repetidos de /src/bingo.py
from test.test_celdas import carton # agrego la funcion que crea el carton de prueba

def test_no_repetidos():
	assert no_repetidos(carton())
