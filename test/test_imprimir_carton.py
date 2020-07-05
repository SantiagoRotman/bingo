from src.bingo import imprimirCarton # agrego la funcion imprimirCarton de /src/bingo.py
from src.bingo import generar_carton # agrego la funcion que crea el carton de prueba

def test_imprimirCarton():
    assert imprimirCarton(generar_carton())
