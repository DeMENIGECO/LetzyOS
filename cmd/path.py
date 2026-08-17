"""Comandi per la gestione dei file"""
def ls():
    """Elenca i file nella directory corrente."""
    import os
    files = os.listdir('.')
    print("File in " + os.getcwd() + ":")
    for file in files:
        print("- " + file)

def make(filename):
    """Crea un nuovo file con il nome specificato."""
    with open(filename, 'w') as f:
        f.write("")  # Crea un file vuoto

def write(filename, content):
    """Scrive il contenuto specificato nel file."""
    with open(filename, 'w') as f:
        f.write(content)

def delete(filename):
    """Elimina il file specificato."""
    import os
    try:
        os.remove(filename)
        print(f"File '{filename}' eliminato.")
    except FileNotFoundError:
        print(f"File '{filename}' non trovato.")
    except Exception as e:
        print(f"Errore durante l'eliminazione del file: {e}")

def stamp(filename):
    """Stampa il contenuto del file specificato."""
    try:
        with open(filename, 'r') as f:
            content = f.read()
            print(content)
    except FileNotFoundError:
        print(f"File '{filename}' non trovato.")
    except Exception as e:
        print(f"Errore durante la lettura del file: {e}")

