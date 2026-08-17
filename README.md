# LetzyOS

**LetzyOS** è un piccolo sistema operativo da terminale, progettato per essere semplice, leggero e facile da utilizzare.
L'interazione con il sistema avviene completamente tramite una **shell testuale**, attraverso comandi digitati dall'utente.

## ✨ Caratteristiche

* 🖥️ Funziona tramite terminale
* 📁 Gestione dei file
* ✏️ Creazione e modifica dei file
* 📖 Lettura del contenuto dei file
* 🧩 Comandi semplici e intuitivi
* ⚡ Leggero e minimale

## 📋 Comandi disponibili

| Comando                         | Descrizione                                      |
| ------------------------------- | ------------------------------------------------ |
| `echo <testo>`                  | Stampa il testo inserito dall'utente.            |
| `help`                          | Mostra la lista dei comandi disponibili.         |
| `exit`                          | Esce dal programma.                              |
| `ls`                            | Elenca i file presenti nella directory corrente. |
| `make <nome_file>`              | Crea un nuovo file.                              |
| `write <nome_file> <contenuto>` | Scrive il contenuto nel file.                    |
| `delete <nome_file>`            | Elimina un file.                                 |
| `stamp <nome_file>`             | Stampa il contenuto di un file.                  |

## 🚀 Esempi

### Stampare un messaggio

```text
echo Hello World
```

### Visualizzare i file

```text
ls
```

### Creare un file

```text
make hello.txt
```

### Scrivere in un file

```text
write hello.txt Ciao dal mio file!
```

### Leggere un file

```text
stamp hello.txt
```

### Eliminare un file

```text
delete hello.txt
```

### Visualizzare l'aiuto

```text
help
```

### Uscire da LetzyOS

```text
exit
```

## 📂 Gestione dei file

LetzyOS permette di gestire semplicemente i file direttamente dalla shell.

Un esempio di utilizzo completo:

```text
make testo.txt
write testo.txt Ciao LetzyOS!
stamp testo.txt
delete testo.txt
```

Questo crea `testo.txt`, inserisce del contenuto, lo visualizza e infine lo elimina.

## 🎯 Obiettivo del progetto

L'obiettivo di LetzyOS è creare un'esperienza simile a quella di un piccolo sistema operativo, mantenendo però l'interfaccia estremamente semplice.

Il progetto è pensato anche come esperimento per imparare come funzionano:

* le shell;
* i comandi da terminale;
* la gestione dei file;
* l'interazione tra utente e sistema.

## 📜 Licenza

Questo progetto è distribuito secondo i termini della licenza indicata nel repository.
