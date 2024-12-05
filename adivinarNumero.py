#Exercise number 1
#adivina el numero y guarda cada intento en una lista

import random

numero = random.randrange(1, 20)
lista = []
intentos = 10

print("Adivina el numero del 1 al 10 en 10 intentos")

for i in range(intentos):
    num = int(input("Ingrese un numero del 1 al 20: "))
    lista.append(num)
    
    if num == numero:
        print("Feliciades, has ganado")
        break
    elif num < numero:
        print("El numero es muy bajo")
    elif num > 20:
        print("El numero esta fuera del rango, pierdes un intento")
    else:
        print("El numero es muy alto")
else:
    print("Te quedaste sin intentos, has perdido")
    
print(f"Estos fueron tus intentos {lista}")