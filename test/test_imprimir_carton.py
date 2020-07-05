from src.bingo import imprimirCarton # agrego la funcion imprimirCarton de /src/bingo.py
from test.test_celdas import carton # agrego la funcion que crea el carton de prueba

def test_imprimirCarton():
    assert imprimirCarton(carton())
