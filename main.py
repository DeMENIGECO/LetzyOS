"""Import file"""
from vars import *
from commands import handle_command

"""Messaggio di benvenuto"""
def welcome_message():
    """Stampa un messaggio di benvenuto."""
    print(f"{name} {version}")
    print("Digita help per visualizzare i comandi disponibili.")

"""Loop dei comandi"""
def command_loop():
    """Loop principale per l'inserimento dei comandi."""
    while True:
        command = input("> ")
        handle_command(command)

"""Funzione principale"""
def main():
    welcome_message()
    command_loop()

"""Esecuzione del programma"""
if __name__ == "__main__":
    main()
