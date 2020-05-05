from src.bingo import entre_1_y_90 # agrego la funcion entre_1_y_90 de /src/bingo.py
from test.test_celdas import carton # agrego la funcion que crea el carton de prueba

def test_entre_1_y_90():
	assert entre_1_y_90(carton())
