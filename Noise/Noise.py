from Funciones import *
import matplotlib.pyplot as plt


def Noise(func, args, intervalo, data_size, caos = 0.1, espaciado = 0, iter = 1):
	'''Este método convierte una función analítica en "datos" que podrían haber salido de un laboratorio
		
		Noise(func, args, interv, data_size, <incert, espaciado>, <iter>)
		
		func: función a utilizar (function);
		args: argumentos de la función;
		intervalo: intervalo del que obtendremos "datos" (array ou lista);
		data_size: número de "datos a generar"
		
		caos: ruido en la medida (int > 0);
			caos == 0: 				Sin Ruido
			caos == 0.1: 			(default)
		espaciado: espaciado entre datos (número); 
			espaciado == 0:		random (default)
			espaciado != 0:		número introducido
		iter: número de iteraciones (int);
			iter = 1			(default)
	'''
	try:
		assert len(intervalo) == 2
		if data_size <= 0:
			raise ValueError("data_size debe ser un número entero positivo")
		if (type(iter) != int) or (iter <= 0):
			raise TypeError("iter debe ser un número entero positivo")
	except AssertionError:
		print("Intervalo no tiene exactamente dos parámetros")
	
	randput = lambda y: y + (2*np.random.rand(len(y))-1) * caos		#Con caos modulamos la dispersión de los datos
	
	Datos = []
	Output = []
	
	for i in range(iter):
		if espaciado == 0:
			data_pos = np.sort(np.random.rand(data_size-2) * (abs(intervalo[0]) + abs(intervalo[-1])) - abs(intervalo[0]))	
			np.insert(data_pos, 0, intervalo[0])
			np.append(data_pos, intervalo[-1])							
			
		else:
			data_pos = np.linspace(intervalo, data_size)		#Creamos las posiciones para los datos (eje horizontal)
		
		output = func(data_pos, args)		#datos, nombre, argumentos 
		
		Datos.append(data_pos)
		Output.append([list(np.vstack([data_pos,randput(output[0])]).T), output[1]]) #, output[2]
	
	return Output

def plotter(Output):
    Data = np.vstack(Output[0])
    x = Data[:,0]
    y = Data[:,1]
    plt.figure(); plt.clf()
    plt.plot(x,y,'.')
    plt.show(True)
