from numpy import random

ordenador = random.randint(1,101)
intentos = 0
while True:
    intentos += 1
    jugador = int(input("Introduce un número del 1 al 100: "))
    if jugador > ordenador:
        print('Demasiado alto')
    elif jugador < ordenador:
        print('Demasiado bajo')
    else: 
        print(f'Has acertado en {intentos} intentos')
        break