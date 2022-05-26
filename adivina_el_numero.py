#!/usr/bin/python3
# create by: jakepy
import random
import platform
import time
import os


def clear():
    if platform.system() == 'Linux':
        os.system('clear')
    else:
        os.system('cls')


def banner():
    clear()
    print('*' * 45)
    print('   Bienvenido al juego adivina el numero')
    print('*' * 45)


def vidas():
    vida = str(input('Quieres elejir la cantidad de vidas si[S] no[N]: '))
    banner()
    if vida == 'si' or vida == 'S':
        vida = int(input('Cuantas vidas quieres: '))
        print(f'Iniciaras con {vida} vidas')
        time.sleep(1.4)
        print('Preparado!!!')
        time.sleep(1.4)
        print("GO!!!")
        time.sleep(1.3)
        banner()
        return vida

    elif vida == 'no' or vida == 'N':
        vida = 10
        print(f'Iniciaras con {vida} vidas por defecto')
        time.sleep(1.5)
        print('Preparado!!!')
        time.sleep(1.5)
        print("GO!!!")
        time.sleep(1.3)
        banner()
        return vida
    else:
        print('Ingrese una opcion valida')


def adivina_numero(n):
    vida = vidas()
    numero_random = random.randint(1, n)
    numero_user = int(input('Ingresa un numero: '))

    while numero_user != numero_random:
        print('vidas: ' + ' ❤ ️' * vida + '\n')

        if vida == 0:
            banner()
            print(f'Perdiste vidas: {vida}')
            print(f'El numero era: {numero_random}')
            break

        if numero_user < numero_random:
            print('Busca un numero mas grande')
            vida -= 1
        else:
            print('Busca un numero mas pequeño')
            vida -= 1
        numero_user = int(input('Ingresa otro numero: '))

        if numero_user == numero_random:
            banner()
            print('🥳 Ganaste el numero era: {} 🥳'.format(numero_random))
            break


def main():
    banner()
    n = int(input('Ingresa hasta que numero quieres adivinar: '))
    banner()
    adivina_numero(n)


if __name__ == '__main__':
    main()
