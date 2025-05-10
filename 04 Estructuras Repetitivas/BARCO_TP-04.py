'''
# Ejercicio 1
for i in range(0, 101, 1):
    print(i)

'''
'''
# Ejercicio 2: 
num_digitos = input("Ingrese un número entero: ")
digitos = 0
for i in range(0, len(num_digitos),1):
    digitos += 1
print("el numero tiene ", digitos, " digitos")

'''
'''
#Ejercicio 3:
primer_num= int(input("Ingrese un numero entero: "))
segundo_num= int(input("Ingrese el segundo número entero: "))
contador = 0
for i in range(primer_num +1, segundo_num, 1):
    contador += 1
print("La cantidad de números enteros entre ", primer_num, " y ", segundo_num, " es: ", contador)

'''

'''
#Ejercicio 4:
sumatoria = 0
numero = int(input("Ingrese un número entero: "))
while numero != 0:
    sumatoria += numero
    numero = int(input("Ingrese otro número entero o 0 para detener: "))
print("La sumatoria de los números ingresados es ", sumatoria)
'''

'''
#Ejercicio 5: 
import random

al_azar = random.randint(0, 9)
num_usuario = int(input("Adivine el número entre 0 y 9: "))
intentos = 1
while num_usuario != al_azar:
    intentos += 1
    num_usuario = int(input("El número es incorrecto, intente nuevamente: "))
print(f"Felicitaciones, adivinó el número en {intentos} intentos")
'''

'''
#Ejercicio 6:
num = 100
while num > 2:
    num -= 2
    print(num) 
'''

'''
#Ejercicio 7:
num_usuario = int(input("Ingrese un número entero positivo: "))
sumatoria = 0
if num_usuario < 0:
    print("El número ingresado no es positivo")
else: 
    for i in range(0, num_usuario +1, 1):
        sumatoria += i                      #i representa cada uno de los numeros entre 0 y el numero ingresado por el usuario
print(f"La sumatoria de los números enteros positivos es: {sumatoria}")
'''

'''
#Ejercicio 8:
pares = 0
impares = 0
positivos = 0
negativos = 0
contador = 0
while contador < 100:
    num = int(input("Ingrese un numero entero: "))
    if num % 2 == 0:
        pares += 1
    else:
        impares += 1
    
    if num > 0:
        positivos += 1
    else: 
        negativos += 1
    contador += 1
print(f"Cantidad de números pares: {pares}")
print(f"Cantidad de números impares: {impares}")
print(f"Cantidad de números positivos: {positivos}")
print(f"Cantidad de números negativos: {negativos}")
'''

'''
#Ejercicio 9:
contador = 0
sumatoria = 0
while contador < 10:
    num = int(input("Ingrese un número entero: "))
    sumatoria += num
    contador += 1
print(f"el promedio de los números ingresados es: {sumatoria/contador}")
'''

'''
#Ejercicio 10:
num = int(input("Ingrese un número entero: "))
inverso = 0
while num > 0:
    digito = num % 10
    inverso = inverso * 10 + digito
    num //= 10
print(f"El número invertido es: {inverso}")
'''
#En el último ejercicio, el operador // se utiliza para realizar una división entera, es decir, se descartan los decimales.