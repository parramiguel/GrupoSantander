# calcular el factorial de un numero

numero = int(input("Ingrese un numero: "))
factorial = 1

for i in range(1, numero + 1):
    factorial = factorial * i

print(f"El factorial de {numero} es {factorial}")
# También podemos calcular el factorial usando recursión
def factorial_recursivo(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_recursivo(n - 1)

print(f"(Recursivo) El factorial de {numero} es {factorial_recursivo(numero)}")

