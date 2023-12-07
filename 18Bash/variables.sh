#!/bin/bash
# definición de variables
una_variable=666
MI_NOMBRE="Yeimi"
NOMBRES="YeiC NoemiC"
BOOLEANO=true
echo "Veamos las variables "
echo "Un número: ${una_variable}"
echo "Un nombre ${MI_NOMBRE}"
echo "Un grupo de nombres: ${NOMBRES}"
# Al script se le pueden pasar argumentos. Para recogerlos
# hay que usar : ${número} donde:
# ${0} : nombre del script
# ${1} : primer argumento
# ${2} : segundo argumento
# ...etc.
echo "Has invocado el script pasándome ${0} estos ${1} "
# $# : Número de argumentos
echo "Me has pasado $# argumentos"
# $@ : grupo de parámetros del script
echo IDa: ${!} y $@
# Variables de entorno
echo "Directorio actual: ${PWD} y Usuario ${UID}"
