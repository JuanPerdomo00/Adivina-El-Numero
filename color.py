#!/usr/bin/python3
# _*_ coding: utf-8 -*-
# Copyright (c) 2022 Jakepy Perdomo <j4kyjak3@protonmail.com>.
from colorama import Fore


class Color:
    # ? Colores para la salida de la terminal
    # * rojo
    r: str = Fore.RED
    # * verde
    v: str = Fore.GREEN
    # * azul
    b: str = Fore.BLUE
    # * amarillo
    y: str = Fore.YELLOW

    m: str = Fore.MAGENTA

    # ! Detiene la ejecucion dedl color
    off: str = Fore.RESET
