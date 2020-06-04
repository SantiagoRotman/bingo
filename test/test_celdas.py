from src.bingo import no_menor_15  #Agrego la funcion no_menor_15  de src/bingo.py
from src.bingo import no_mayor_15 #Agrego la funcion no_mayor_15 de src/bingo.py
from src.bingo import dimensiones #Agrego la funcion dimensiones de src/bingo.py
from src.bingo import columnas_ni_vacias_ni_llenas #Agrego la funcion columnas_ni_vacias_ni_llenas de src/bingo.py
from src.bingo import filas_con_5
#Funcion carton: 0 celda desocupada, 1 celda ocupada
def carton():
    mi_carton = (
        (2,0 ,0 ,10,12,0 ,14 ,0  ,19),
        (0,15,0 ,27,0 ,58,69 ,0 ,72),
        (13,0 ,20,0 ,26,71,0  ,82 ,0)
    )
    return mi_carton

#Compruebo que la cantidad de celdas ocupadas sean mayor o igual a 15
def test_no_menor_15():
	assert no_menor_15(carton())

#Compruebo que la cantidad de celdas ocupadas sean menor o igual a 15
def test_no_mayor_15():
	assert no_mayor_15(carton())


#Compruebo que las dimensiones sean 9x3.
def test_dimensiones():
	assert dimensiones(carton())


#Compruebo que las columnas no esten ni vacias ni llenas
def test_columnas_ni_vacias_ni_llenas():
	assert columnas_ni_vacias_ni_llenas(carton())

#Compruebo que todas las filas tengan 5 elementos
def test_filas_con_5():
	assert filas_con_5(carton())




