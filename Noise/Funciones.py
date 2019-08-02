import numpy as np
import matplotlib.pyplot as plt

'''Listado de funciones disponibles:
	- Polinomios A + Bx + Cx^2 + ...
	- Coseno Acos(Bx + C) + D
	- Exponencial Ae^(Bx + C) + D

'''

def text(args):
	if type(args) == int:
		return str(args)
	else:
		return str(len(args) -1)
		
def Args(args):
	'''Función de generación de argumentos
	lista con elementos str da lugar a parámetro en esa posición aleatorio, por ej.: [0,'',1,3] => el parámetro B será aleatorio
	'''

	if type(args) == int:
	
		if args < 0:
			raise ValueError("args debe ser un entero positivo una lista o un array")
		return np.random.rand(args)
		
	elif (type(args) == list) or (type(args) == np.array):
		return [i if type(i)!=str else np.random.rand() if i != '-' else 2*np.random.rand()-1 if  for i in args]
		
	else:
		raise TypeError("args debe ser un entero positivo una lista o un array")

def P(x,args = 2):
	'''Función Polinomio
	P(x,<args>) = F, Nombre, A 
	x : valores en x;
	args : Términos A,B,C, ...;
		type(args) == int:		Grado del polinomio (parámetros aleatorios)(default)
		type(args) != int :							(lista o array)
	'''
	nombre = 'PolinomioG'
	
	A = Args(args)
	
	F = np.zeros(len(x))	
	for i in range(len(A)):
		F += A[i]*np.power(x,i)
		
	return F, (nombre + text(args)), A
		
def fexp(x,args = 4):
	
	nombre = 'Exponencial'
		
	A = Args(args)
	
	F = A[0]*np.e**(A[1]*x+A[2])+A[3]
		
	return F, nombre, A
		
def fcos(x,args = 4):
	'''Función Coseno
	'''
	nombre = 'Coseno'
	
	A = Args(args)
	
	F = A[0]*np.cos(A[1]*x + A[2]) + A[3]
		
	return F, nombre, A
	