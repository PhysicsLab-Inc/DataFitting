from Funciones import *

def Noise(func, args, intervalo, data_size, caos = 0.1, espaciado = 0):
	'''Este método convierte una función analítica en "datos" que podrían haber salido de un laboratorio
		
		Noise(func, args, interv, data_size, <incert, espaciado>)
		
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
	'''
	try:
		assert len(intervalo) == 2
		if data_size <= 0:
			raise ValueError("data_size debe ser un número entero positivo")
	except AssertionError:
		print("Intervalo no tiene exactamente dos parámetros")
	
	if espaciado == 0:
		data_pos = np.sort(np.random.rand(data_size-2)* data_size)	
		np.insert(data_pos, 0, intervalo[0])
		np.append(data_pos, intervalo[-1])							
		
	else:
		data_pos = np.linspace(intervalo, data_size)		#Creamos las posiciones para los datos (eje horizontal)
	
	output = func(data_pos, args)
	
	Aleatorio = False
	if len(output) == 2:
		y = output[0]
		args = output[1]
		Aleatorio = True
	else:
		y = output
		
	data = y + (2*np.random.rand(len(y))-1) * caos 	#Con caos modulamos la dispersión de los datos
	
	if Aleatorio:
		return np.vstack([data_pos,data]).T, np.vstack([data_pos, y]).T, args	#Matrices verticales con columnas x e y (Ruido // Sin Ruido)
	else: 
		return np.vstack([data_pos,data]).T, np.vstack([data_pos, y]).T		#Matrices verticales con columnas x e y (Ruido // Sin Ruido)
	
	
	
	
	
	