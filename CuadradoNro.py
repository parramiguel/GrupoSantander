# Crear una lista con los cuadrados de los n primeros números naturales 

def cuadrados(n):
    lista = []
    for i in range(1, n + 1):
        lista.append(i ** 2)
    return lista

print(cuadrados(10))