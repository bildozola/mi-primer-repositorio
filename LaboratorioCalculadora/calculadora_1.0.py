print("=== CALCULADORA EN PYTHON ===")
print("Selecciona una operación:")
print("1. Suma")
print("2. Resta")
print("3. Multiplicación")
print("4. División")
opcion = input("Ingresa el número para seleccionar tu operacion: ")

num1 = int(input("Ingresa el primer número:"))
num2 = int(input("Ingresa el segundo número:"))

if opcion == '1':
    resultado = num1 + num2
    operacion = "Suma"
elif opcion == '2':
    resultado = num1 - num2
    operacion = "Resta"
elif opcion == '3':
    resultado = num1 * num2
    operacion = "Multiplicación"
elif opcion == '4':
    if num2 != 0:
        resultado = num1 / num2
        operacion = "División"
    else:
        print("Error: No se puede dividir entre 0.")
        exit()
else:
    print( "Opción no válida.")
    exit ()
print (f"\n{operacion}: {num1} y {num2} = {resultado}")