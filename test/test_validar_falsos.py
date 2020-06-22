from src.bingo import dimensiones
from src.bingo import no_mayor_15
from src.bingo import no_menor_15
from src.bingo import columnas_ni_vacias_ni_llenas
from src.bingo import entre_1_y_90
from src.bingo import menor_izq_a_der
from src.bingo import menor_arriba_a_abajo
from src.bingo import no_repetidos
from src.bingo import filas_con_5
from src.bingo import no_tres_consecutivas_vacias_o_llenas

def carton_falso():
    mi_carton = (
        (0  ,0  ,0  ,58 ,12 ,0  ,14 ,0  ,19),
        (0  ,15 ,0  ,27 ,71 ,58 ,69 ,0  ,72),
        (13 ,0  ,20 ,0  ,26 ,71 ,0  ,0  ,0 )
    )
    return mi_carton

def test_falsos():

    carton = carton_falso()

    assert not (dimensiones(carton) and
    no_mayor_15(carton) and
    no_menor_15(carton) and
    columnas_ni_vacias_ni_llenas(carton) and
    entre_1_y_90(carton) and
    menor_izq_a_der(carton) and
    menor_arriba_a_abajo(carton) and
    no_repetidos(carton) and
    filas_con_5(carton) and
    no_tres_consecutivas_vacias_o_llenas(carton))
