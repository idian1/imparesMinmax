suma = 0
num1 = int(input("ingrese el numero minimo "))
num2 = int(input("ingrese el numero maximo "))
for i in range(num1, num2+1):
    if i % 2 == 1:
        suma += i

print(f"la suma de todos los numeros impares entre {num1} y {num2} es de {suma}")

# En este codigo el usuario ingresa un numero el que entra en un ciclo "for" el cual recorre todos los numeros desde
# el numero minimo ingresado (num1) hasta el numero maximo ingresado (num2) y utilizando el operador modulo
# comprueba si el numero es par o impar, si este es impar sera sumado a la variable suma,
# luego de terminar el ciclo imprime la suma total de impares
# En este codigo utilice el ciclo for por que era conveniente para la situacion requerida.
