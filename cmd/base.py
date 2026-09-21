"""Comandi base per Letzy OS."""

import os
import time
import sys

def echo(text):
    """Stampa il testo inserito dall'utente."""
    print(text)

def help():
    """Stampa la lista dei comandi disponibili."""
    print("Comandi disponibili:")
    print("echo <testo> - Stampa il testo inserito dall'utente.")
    print("help - Stampa la lista dei comandi disponibili.")
    print("exit - Esce dal programma.")
    print("ls - Elenca i file nella directory corrente.")
    print("make <nome_file> - Crea un nuovo file.")
    print("write <nome_file> <contenuto> - Scrive il contenuto nel file.")
    print("delete <nome_file> - Elimina il file.")
    print("stamp <nome_file> - Stampa il contenuto del file.")

def exit():
    """Esce dal programma."""
    os.system("clear" if os.name == "posix" else "cls") 
    print("Disconnessione da 'user'...")
    time.sleep(0.5)
    print("Chiudendo /letzy/core/cmd...")
    print("Chiudendo CmdTermRecognize...")
    time.sleep(2)
    print("Chiudendo CmdRunCommands...")
    time.sleep(0.7)
    print("Smontando filesystem: /letzy/*...")
    time.sleep(3)
    print("Chiudendo SigtermServiceMSG...")
    print("Chiudendo SigtermServiceLand...")
    print("Smontando filesystem: :/network/*...")
    time.sleep(1)
    print("Chiudendo LetzyUserInterface...")
    print("Chiudendo LTemp...")
    print("Smontando filesystem :/tmp/*")
    print("\nChiusura completata.")

    os.system("clear" if os.name == "posix" else "cls")
    sys.exit(0)
