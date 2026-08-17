"""Import file"""
from cmd.base import *
from cmd.path import *

"""Gestione dei comandi"""
def handle_command(command):
    """Gestisce i comandi inseriti dall'utente."""
    if command.startswith("echo "):
        echo(command[5:])
    elif command == "help":
        help()
    elif command == "exit" or command == "quit":
        exit()
    elif command == "ls":
        ls()
    elif command.startswith("make "):
        make(command[5:])
    elif command.startswith("write "):
        parts = command[6:].split(' ', 1)
        if len(parts) == 2:
            filename, content = parts
            write(filename, content)
        else:
            print("Utilizzo: write <nome_file> <contenuto>")
    elif command.startswith("delete "):
        delete(command[7:])
    elif command.startswith("stamp "):
        stamp(command[6:])
    elif command == "":
        pass  # Ignora comandi vuoti
    else:
        print(f"Comando non riconosciuto: {command}")