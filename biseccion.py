from math import * #Importamos la librería de math
#Deivith Zanella 28.564.281
def biseccion(f,a,b,tol,ni):
	#Variables
	Error_a = 100 #Error aproximado relativo.
	p_actual=a #Punto medio actual
	p_anterior=b # Punto medio previo
	contador=1  # Contador de numero de iteracciones
	print("\nMétodo de Bisección\n") #Titulo
	while (contador < ni and Error_a > tol):
		p_anterior = p_actual
		p_actual= (a+b)/2
		if(f(a)*f(p_actual)<0): #cambia de signo en el intervalo [a,m]
			b=p_actual
		if(f(p_actual)*f(b)<0): #cambia de signo en el intervalo [a,m]
			a=p_actual
		Error_a = abs ((p_actual-p_anterior)/p_actual)
		print('Iteraccion',contador,'intervalo: [',a,',',b,']')
		contador=contador+1
	print('\nEs la mejor solución aproximada se encuentra en m(',contador-1,') =',p_actual,'\n')	
	print("El error relativo es: ",Error_a)

if __name__ == '__main__':
	f = lambda x: sin (x) - e**-x #funcion 
	# otro ejercicio sin (x) - e**-x 0 1
	# otro ejercicio e**x - 3*x**2 0 1
	a = 0 # intervalo a
	b = 1 # intervalo B
	tol = 0.03 
	ni = 50 # Numero de iteracciones
	solucion = biseccion(f, 0, 1, 0.03, ni) 