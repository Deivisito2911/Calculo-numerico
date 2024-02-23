from math import  *
#Nombre: Ricardo Balducci.
#Cedula: 28.308.177

def f(t, y):
   return (t-y)**2+1


def metodo_euler(f, t0, y0, h, n):
    print("\nMétodo de Euler\n")
    print("|\ti\t||\tti\t||\tyi\t||\tyi+1\t|")
    resultados_t = [t0]
    resultados_y = [y0]
    for i in range(n):
        i+1
        y1 = y0 + h * f(t0, y0)
        t1 = t0 + h
        resultados_t.append(t1)
        resultados_y.append(y1)
        print("|\t",i,"\t||\t",t0,"\t||\t",y0,"\t||\t",y1,"\t|")
        t0, y0 = t1, y1
    return resultados_t, resultados_y


if __name__ == '__main__':
    t0 = 2 
    y0 = 1
    h = 0.25
    n = 5
    resultados_t, resultados_y = metodo_euler(f, t0, y0, h, n)
    print('\nfin')