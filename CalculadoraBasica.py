# Calculadora
# Pide al usuario una operación (suma, resta, multiplicación, división) y dos números.
# Ejecute la operación y muestre el resultado.
# Debe repetirse hasta que el usuario escriba "salir" como operación.

print("=== CALCULADORA BÁSICA ===")
print("Operaciones disponibles: suma, resta, multiplicación, división")
print("Escriba 'salir' para terminar el programa")

while True:
    # Pedir la operación al usuario
    operacion = input("\nIngrese la operación (suma/resta/multiplicación/división/salir): ").lower().strip()
    
    # Verificar si el usuario quiere salir
    if operacion == "salir":
        print("¡Hasta luego!")
        break
    
    # Validar que la operación sea válida
    operaciones_validas = ["suma", "resta", "multiplicación", "división"]
    if operacion not in operaciones_validas:
        print("❌ Operación no válida. Use: suma, resta, multiplicación o división")
        continue
    
    try:
        # Pedir los dos números
        numero1 = float(input("Ingrese el primer número: "))
        numero2 = float(input("Ingrese el segundo número: "))
        
        # Ejecutar la operación y mostrar el resultado
        if operacion == "suma":
            resultado = numero1 + numero2
            print(f"✅ {numero1} + {numero2} = {resultado}")
            
        elif operacion == "resta":
            resultado = numero1 - numero2
            print(f"✅ {numero1} - {numero2} = {resultado}")
            
        elif operacion == "multiplicación":
            resultado = numero1 * numero2
            print(f"✅ {numero1} × {numero2} = {resultado}")
            
        elif operacion == "división":
            if numero2 == 0:
                print("❌ Error: No se puede dividir por cero")
            else:
                resultado = numero1 / numero2
                print(f"✅ {numero1} ÷ {numero2} = {resultado}")
                
    except ValueError:
        print("❌ Error: Por favor ingrese números válidos")
    except Exception as e:
        print(f"❌ Error inesperado: {e}")
