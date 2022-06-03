#!/usr/bin/python3
# _*_ coding: utf-8 -*-
#
#    create by: jakepy Perdomo <j4kyjak3@protonmail.com>
#    This program is free software; you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation; version 2 of the License.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program; if not, write to the Free Software
#    Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA

import random
from color import Color as c
import platform
import time
import os


# ? limpia la pantalla dependiendo de el sistema operativo
def clear():
    if platform.system() == 'nt':
        os.system('cls')
    else:
        os.system('clear')


# ? crea el baner de presentacion en la terminal
def banner():
    clear()
    print(f'{c.y}*{c.off}' * 45)
    print(f'   {c.v}Bienvenido al juego adivina el numero{c.off}')
    print(f'{c.y}*{c.off}' * 45)


# ? funcion de vidas
def vidas():
    try:
        vida = str(input(f'{c.v}Quieres elejir la cantidad de vidas si{c.r}[S]{c.v} no{c.r}[N]{c.off}: '))
        banner()
        if vida == 'si' or vida == 'S' or vida == 's':
            vida = int(input(f'{c.v}Cuantas vidas quieres: {c.off}'))
            banner()
            print(f'{c.v}Iniciaras con {c.r}{vida} {c.v}vidas{c.off}')
            time.sleep(1.4)
            banner()
            print(f'{c.v}Pre{c.r}par{c.y}ado{c.b}!!!{c.off}')
            time.sleep(1.4)
            print(f"{c.b}GO{c.v}!!{c.m}!{c.off}")
            time.sleep(1.3)
            banner()
            return vida

        elif vida == 'no' or vida == 'N' or vida == 'n':
            vida = 10
            print(f'{c.v}Iniciaras con {c.r}{vida} {c.v}vidas por defecto{c.off}')
            time.sleep(1.2)
            banner()
            time.sleep(1.5)
            print(f'{c.v}Pre{c.r}par{c.y}ado{c.b}!!!{c.off}')
            time.sleep(1.5)
            print(f"{c.b}GO{c.v}!!{c.m}!{c.off}")
            time.sleep(1.3)
            banner()
            return vida
        else:
            print(f'{c.r}[!] Ingrese una opcion valida {c.off}')
            exit(1)

    except KeyboardInterrupt as e:
        print(e)
        print(f'\n{c.f} [!] Salio forzadamente{c.off}')
        exit(1)


# ? Funcion de logica principal
def adivina_numero(n):
    vida = vidas()
    numero_random = random.randint(1, n)
    numero_user = int(input(f'\n{c.y}[?]{c.v} Ingresa un numero: {c.off}'))
    banner()
    while numero_user != numero_random:
        banner()
        print(f'{c.v}tienes {c.r}{vida}{c.off} {c.v}vidas: {c.off}' + f'{c.r} ❤ ️{c.off}' * vida + '\n')
        if vida == 0:
            print(f'\n{c.v}Perdiste vidas: {c.r}{vida}{c.off}')
            print(f'{c.v}El numero era: {c.r}{numero_random}{c.off}')
            break

        if numero_user < numero_random:
            print(f'{c.v}Busca un numero mayor a {c.r}{numero_user}{c.off}')
            vida -= 1
        else:
            print(f'{c.v}Busca un numero menor a {c.r}{numero_user}{c.off}')
            vida -= 1
        numero_user = int(input('{}Ingresa otro numero: {}'.format(c.v, c.off)))

        if numero_user == numero_random:
            banner()
            print('\n🥳 {} Ganaste el numero era: {} {}🥳\n'.format(c.m, c.off, numero_random))
            break


# ? fUNCION PRINCIPAL ARRANCA EL PROGRAMA
def main():
    banner()
    try:
        n = int(input(f'\n{c.b}Ingresa hasta que numero quieres adivinar{c.off} {c.y}->{c.off} '))
        banner()
        adivina_numero(n)
    except ValueError as ve:
        banner()
        print('\n{} por favor ingrese algo. Crees que soy tonto? Sea serio {} {}XD {} '.format(c.r, c.off, c.y, c.off))
    except KeyboardInterrupt:
        banner()
        print('\n{} Salio forzado. {}'.format(c.r, c.off))


if __name__ == '__main__':
    main()
