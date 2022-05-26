#!/bin/bash

# create by: jakepy

function saludar() {
    clear
    echo "Descargando dependencias"
    sleep 1
    brew install cowsay
    brew install lolcat
    pip3 install -r requirements.txt
    sleep 1
    echo "Descargado :)"
}


function run() {
    saludar
    echo ''
    sleep 1
    cowsay -f tux "Dios ayudanos a mejorar cada dias mas." | lolcat
    sleep 1

    echo "Ejecutando juego" | lolcat
    sleep 2
    clear
    python3 adivina_el_numero.py
}

run