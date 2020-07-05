#!/bin/bash
# ------------------------------------------------------------------
# [Author] Santiago Rotman
#          Crea un archivo html con un carton de bingo o lo muestra por consola
# ------------------------------------------------------------------

USAGE="Usar: ./pull.sh -h (help)  -w (web)  -c (consola)"

#--- Procesamiento de Opciones --------------------------------------------
if [ $# == 0 ] ; then
   echo $USAGE
    exit 1;
fi

cd ./src

while getopts ":wch" option
do
    case "${option}"
        in
            w)  FILE="web.py"
                TMP=$(python web.py)
                cd ..
                touch bingo.html
                echo $TMP > bingo.html
                RES="Creado carton en bingo.html"
            ;;
            c)  FILE=bingo.py
                RES=$(python -c 'import bingo; print (bingo.imprimirCarton(bingo.generar_carton()))')
            ;;
            h)  cd ..
                cat README.md
                exit 0;
            ;;
            "?")
                echo "Opcion desconocida $OPTARG"
                exit 0;
            ;;
            *)
                echo "Error inesperado en el procesamiento de opciones"
                exit 0;
            ;;
    esac
done

echo -e $RES;
