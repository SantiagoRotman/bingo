[![Build Status](https://travis-ci.org/SantiagoRotman/bingo.svg?branch=master)](https://travis-ci.org/SantiagoRotman/bingo)  [![Coverage Status](https://coveralls.io/repos/github/SantiagoRotman/bingo/badge.svg?branch=master)](https://coveralls.io/github/SantiagoRotman/bingo?branch=master)[![Scrutinizer Code Quality](https://scrutinizer-ci.com/g/SantiagoRotman/bingo/badges/quality-score.png?b=master)](https://scrutinizer-ci.com/g/SantiagoRotman/bingo/?branch=master)

# Bingo

> Un programa hecho en python que crea un archivo HTML con un carton aleatorio de bingo que sigue algunas reglas o lo imprime por consola.
> Creado para la materia Adaptación Del Ambiente De Trabajo, Instituto Politécnico Superior "Gral. San Martín"

## Reglas

- Los números del carton se encuentran en el rango 1 a 90.
- Cada columna de un carton (contando de izquierda a derecha) contiene numeros que van del 1 al 9, 10 al 19, 20 al 29 ..., 70 al 79 y 80 al 90.
- No hay números repetidos en el carton.
- Cada fila de un carton tiene exactamente 5 celdas ocupadas.
- Cada carton es una matrix de 3 x 9.
- Cada carton tiene 15 celdas ocupadas.
- Los números de las columnas izquierdas son menores que los de las columnas a la derecha.
- Para una misma columna, sus números están ordenados de menor a mayor de arriba hacia abajo.
- No pueden existir columnas vacias.
- No pueden existir columnas con sus tres celdas ocupadas.
- Cada carton debe tener 3 y solo 3 columas con solo una celda ocupada.
- En una fila no existen más de dos celdas vacías consecutivas.
- En una fila no existen más de dos celdas ocupadas consecutivas.

## Uso
Ejecutar el script bingo.sh por consola con la opcion -c
```
./bingo.sh -c
```
Para la version web:
Ejecutar el script bingo.sh por consola con la opcion -w
```
./bingo.sh -w
```
Luego abrir bingo.html con un navegador web

## Licencia
	GNU General Public License v3.0
