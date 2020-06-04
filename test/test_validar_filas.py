from src.bingo import no_tres_consecutivas_vacias_o_llenas
from test.test_celdas import carton

def test_no_tres_consecutivas_vacias_o_llenas():
	assert no_tres_consecutivas_vacias_o_llenas(carton())
