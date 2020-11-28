# simulacion
Generador de números pseudoaleatorios en tkinter

main se puede correr como :
 - ./main.py: inicia el programa normalmente
 - ./main.py 17 221 101 17001 325: inicial el programa con semilla, constante, factor, modulo 
 	y tamaño dados.

para compilar a ejecutable:
	pyinstaller main.py --onefile --hidden-import=tkinter
	compilar en la plataforma donde se vaya a usar antes de entregar (windows)

este programa utiliza:
	python 3.9
	tkinter (incluido en python 3.9)
	pyinstaller (para hacer el compilador solamente)
	scipy
	matplotlib (downgrade de version, googlear si falla [TODO])
	
IMPORTANTE:
	En el folder del ejecutabla deben estar los archivos: "demanda", "factores", "espera"
	los cuales sirven para especificar las tablas de distribución de probabilidades
	de un problema, estos archivos deben tener formato tipo:
	0.01 25
	0.14 26
	0.03 27
	, donde cada par inicia una nueva linea, no dejar espacios antes o despues
	y no terminar en nueva linea.
	
	En el caso del archivo "factores, el formato es:
	1.2
	0.8
	0.9
	Este archivo no se lee como una tabla, se transforma directamente a un arreglo
	de números decimales
  
