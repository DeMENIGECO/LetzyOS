"""Comandi base per Letzy OS."""
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
    print("Uscita dal programma...")
    quit()