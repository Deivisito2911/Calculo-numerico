import unittest
import biseccion
import newton_raphson
import Integracion_numerica
import ecuaciones_diferenciales
from math import *

'''Funcion'''
def f(x):
    return sqrt(x+1)

def f2(t, y):
   return (t-y)**2+1

class test_biseccion(unittest.TestCase):
    def test_biseccion(self):
        f = lambda x: e**x - 3*x**2
        a = 0
        b = 1
        tol = 0.02
        ni = 100
        self.assertEqual(biseccion.biseccion(f,a,b,tol,ni),None)
    def test_biseccion_segundo(self):
        f = lambda x: sin (x) - e**-x 
        a = 0
        b = 1
        tol = 0.02
        ni = 100
        self.assertEqual(biseccion.biseccion(f,a,b,tol,ni),None)

class test_newton_raphson(unittest.TestCase):
    def test_newton_raphson(self):
        f= lambda x: e**x-3*x**2 #
        df = lambda x: e**x-6*x # 
        x0 = 0.7  # valor inicial de x
        tol = 0.02 # margen
        self.assertEqual(newton_raphson.newthon_raphson(f,df,x0,tol),0.9100079800667897)

    def test_newton_raphson_dos(self):
        f= lambda x: x**2+2*x-8#
        df = lambda x: 2*x + 2 # 
        x0 = 0.7  # valor inicial de x
        tol = 0.02 # margen
        self.assertEqual(newton_raphson.newthon_raphson(f,df,x0,tol),2.00020555596486)

class test_integracion_numerica(unittest.TestCase):
    def test_suma_riemann(self):
        a = -1      # inicio del intervalo
        b = 1     # fin del intervalo
        n = 5   # numero de participaciones
        self.assertEqual(Integracion_numerica.suma_riemann(f, a, b, n),1.5548955608445105)

class test_ecucacion_diferenciales(unittest.TestCase):
    def test_metodo_euler(self):  
        pass

       
 
if __name__ == "__main__":
    unittest.main()
