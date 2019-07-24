import numpy as np
import matplotlib.pyplot as plt

'''Listado de funciones disponibles:
	- Polinomios


'''
def P(x,args = 2):
	'''Función Polinomio
	P(x,<args>) = P, A o  P (solo devolvemos A si es aleatorio)
	x : valores en x;
	args : Términos A,B,C, ... del polinomio;
		type(args) == int:		Grado del polinomio (parámetros aleatorios)(default)
		type(args) != int :							(lista o array)
	'''
	nombre = 'PolinomioG'
	
	if type(args) == int:
		if args < 0:
			raise ValueError("args debe ser un entero positivo una lista o un array")
		A = np.random.rand(args)	#El formato de esto hay que cambiarlo para cada tipo de función
	elif (type(args) == list) or (type(args) == np.array):
		A = np.array(args)
	else:
		raise TypeError("args debe ser un entero positivo una lista o un array")
	
	P = np.zeros(len(x))				
	for i in range(len(A)):			#Esta es la parte única de cada tipo de función, el resto puede ser Ctrl+C, Ctrl+V
		P += A[i]*np.power(x,i)		#Aunque también hay que ajustar qué significa args int en cada una, preferiblemente aleatoriedad.
		
	if type(args) == int:
		return P, (nombre + str(args)), A
	else: 
		return P, (nombre + str(len(args) -1)), A