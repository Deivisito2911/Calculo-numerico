from math import  *
#Deivith Zanella 28.564.281

'''Funcion'''
def f(x):
    return sqrt(x+1)

'''Suma de riemann'''
def suma_riemann(f,a,b,n):
	h = (b-a)/n
	acum = 0
	for i in range (n):
		x=a+i*h
		acum = acum+h*f(x)
	return acum

'''Metodo de trapecio'''
def trapecio(a, b, n):
    h = (b - a) / n
    suma = 0.5 * (f(a) + f(b))
    for i in range(1, n):
        x = a + i*h
        suma += f(x)
    return h * suma

if __name__ == '__main__':
    a = -1      # inicio del intervalo
    b = 1     # fin del intervalo
    n = 5   # numero de participaciones

    riemann = suma_riemann(f, a, b, n)
    trapecio = trapecio(a, b, n)

    print("\t.:Integracion Numerica:.")
    print("-------------------------------------")
    print("Suma de Riemann en funcion f(x) para",a," y ",b, "en ", n, " intentos: ",riemann)
    print("-------------------------------------")
    print("Metodo de Trapecio en funcion f(x) para",a," y ",b," en ",n,"intentos: ",trapecio)
