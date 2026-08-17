# Contributing to LetzyOS

Grazie per il tuo interesse nel contribuire a **LetzyOS**! 🦎

LetzyOS è un piccolo sistema operativo da terminale e ogni contributo può aiutare a renderlo più semplice, stabile e interessante.

## 🤝 Come contribuire

Puoi contribuire in diversi modi:

* 🐛 Segnalando bug
* 💡 Proponendo nuovi comandi
* ⚡ Migliorando i comandi esistenti
* 📚 Migliorando la documentazione
* 🧹 Sistemando o migliorando il codice
* ✨ Aggiungendo nuove funzionalità

## 🐛 Segnalare un bug

Prima di aprire una segnalazione, controlla che il problema non sia già stato segnalato.

Quando apri una issue, cerca di includere:

* Una descrizione del problema
* I comandi utilizzati
* Il comportamento ottenuto
* Il comportamento che ti aspettavi
* Eventuali messaggi di errore

Esempio:

```text
Comando:
write test.txt Hello

Problema:
Il file non viene creato.

Comportamento atteso:
Il file test.txt dovrebbe essere creato e contenere "Hello".
```

## 💡 Proporre una funzionalità

Hai un'idea per migliorare LetzyOS?

Apri una issue descrivendo:

1. Qual è la nuova funzionalità.
2. Perché potrebbe essere utile.
3. Come potrebbe funzionare.
4. Eventuali esempi di utilizzo.

Per esempio:

```text
Nuovo comando: pwd

Descrizione:
Mostra il percorso della directory corrente.

Esempio:
pwd

Output:
C:/LetzyOS
```

## 🔀 Pull Request

Per contribuire tramite una Pull Request:

1. Fai un fork del repository.
2. Crea un nuovo branch per le tue modifiche.
3. Effettua le modifiche.
4. Testa LetzyOS.
5. Fai commit delle modifiche.
6. Pusha il branch.
7. Apri una Pull Request.

Un possibile nome per il branch è:

```text
feature/nuovo-comando
```

oppure:

```text
fix/correzione-file
```

## 🧪 Test

Prima di inviare una Pull Request, assicurati che LetzyOS continui a funzionare correttamente.

Testa soprattutto:

* `echo`
* `help`
* `exit`
* `ls`
* `make`
* `write`
* `delete`
* `stamp`

Se hai aggiunto un nuovo comando, verifica anche che funzioni correttamente in diversi casi.

## 📝 Stile del codice

Cerca di mantenere il codice:

* semplice;
* leggibile;
* organizzato;
* coerente con il resto del progetto.

Evita modifiche inutilmente complicate quando è possibile ottenere lo stesso risultato con una soluzione più semplice.

## 📖 Documentazione

Se aggiungi o modifichi una funzionalità, aggiorna anche la documentazione quando necessario.

In particolare, se aggiungi un nuovo comando, ricordati di documentare:

```text
comando <argomenti> - Descrizione del comando.
```

e di aggiungere almeno un esempio di utilizzo.

## ✅ Checklist per le Pull Request

Prima di aprire una Pull Request, controlla:

* [ ] Il codice funziona.
* [ ] Ho testato le modifiche.
* [ ] Non ho introdotto errori nei comandi esistenti.
* [ ] Ho aggiornato la documentazione se necessario.
* [ ] La Pull Request descrive chiaramente le modifiche.
* [ ] Ho mantenuto il codice semplice e leggibile.

## 🌟 Grazie!

Ogni contributo, anche piccolo, è utile per migliorare LetzyOS.

**Grazie per aver contribuito a LetzyOS!** 🦎💻
