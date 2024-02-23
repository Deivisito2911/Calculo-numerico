from math import  *
#Nombre: Ricardo Balducci.
#Cedula: 28.308.177

def f(x):
    return e**x-3*x**2 #  sin(x) - e**-x 

def df(x):
    return e**x-6*x #  cos(x) + e**-x

def newthon_raphson(f, df, x0, tol, max_iter=5):
    i = 0
    Error_a = 100
    print("\nMétodo de Newton-Raphson\n")
    print ("| i | xi | xi+1 |")
    print ("----------------------")
    while (i < max_iter and Error_a > tol):
        x1 = x0 - f(x0) / df(x0)
        print ('|',i, '|', x0, '|','|',x1, '|' )
        if abs(x1 - x0) < tol * abs(x1):
            return x1
        x0 = x1
        i += 1
    print('\nEs la mejor solución aproximada se encuentra en m(',i-1,') =',x1,'\n')    
    raise ValueError("El método de Newton-Raphson no converge después de %d iteraciones." % max_iter)#en caso de no poder

if __name__ == '__main__':
    x0 = 0.7  # valor inicial de x
    tol = 0.02 # margen de error
    raiz = newthon_raphson(f, df, x0, tol)  # encontramos la raíz de f
    print('\nfin')