
import os
import random

MAX_intentos = 5
incognitas = ["Camino", "Comida","Abrazo","Carne","Beso","Rock","Party",
            "Casa","Musica", "Music","Algoritmo", "Libreria", "Framework",
            "Programador", "Dev", "Flow", "Luck", "Big", "Smoot", "Get Luky",
            "Version", "Video", "System", "Code", "Down", "Adriana"]

def cambio_palabra():
    palabra = random.choice(incognitas)
    secreto = "_"*len(palabra)
    return palabra, secreto


def reemplazar_palabra(palabra, secreto, letra):
    cantidad = palabra.count(letra)
    inicio = 0
    for i in range(cantidad):
        posicion = palabra.find(letra, inicio)
        secreto = secreto[:posicion] + letra + secreto[posicion+1:]
        inicio = posicion + 1
    return secreto

def ahorcado():
    print(f"Hola, vamos a jugar el juego del ahorcado.\n La palabra secreta sera el nombre de una de las {len(incognitas)} palabras. \n Tienes {MAX_intentos} intentos maximos para descurbrir la plabra. ")
    input("Presiona enter si estas listo...")
    palabra, secreto = cambio_palabra()
    fallos = 0 
    while secreto != palabra and fallos < MAX_intentos:
        os.system('cls')
        print(f'Palabra : {secreto}')
        insertar = input('Que letras deseas insertar? ')
        if insertar in palabra:
            secreto = reemplazar_palabra(palabra, secreto, insertar)
            print('Bien hecho')
        else:
            print('Lo siento la letra no esta en la palabra')
            fallos += 1
            print(f'Has fallado {fallos} veces')
        input('Presiona enter para continuar')
    if secreto == palabra:
        os.system('cls')
        print(f'\nFelicidades has ganado! La palabra es {secreto}')
    else:
        os.system('cls')
        print(f'\nPerdiste! La palabra era {palabra}')
    print('Hasta pronto...')


# def main():
#     ahorcado()
# if __name__ == '__main__':
#     main()

ahorcado()