'''
Facoltativo: 
Scrivi una funzione generatrice di password.
La funzione deve generare una stringa alfanumerica di 8 caratteri
qualora l'utente voglia una password semplice, 
o di 20 caratteri ascii qualora desideri una password più complicata.

'''

import string
import random

def generate_password(length:int, charset:str) ->str:
# Genera una password casuale di lunghezza e caratteri specificati.

#I parametri della funzione sono:

# length: numero di caratteri della password
# charset: stringa contenente tutti i caratteri possibili da usare
    
#La funzione ritorna una stringa contenente la password generata

# Creiamo una lista vuota 
    password = []
    
# Ciclo che si ripete per il numero di caratteri richiesto
    for i in range(0, length):
# Sceglie un carattere casuale dal charset
        lettera = random.choice(charset)
# Aggiunge il carattere alla lista password
        password.append(lettera)
    
# Unisce tutti i caratteri della lista in una stringa unica
# ''.join(['a','b','c']) diventa "abc"
    return ''.join(password)

# Dizionario che mappa le scelte dell'utente a lambda functions
# Ogni lambda restituisce una tupla con (lunghezza, set_di_caratteri)
password_types = {
    's': lambda: (8, string.ascii_letters + string.digits),# Semplice: 8 char alfanumerici
    'c': lambda: (20, string.ascii_letters + string.digits + string.punctuation)  # Complessa: 20 char + simboli
}

# Chiede all'utente che tipo di password vuole
scelta = input("Complessa o Semplice? C/S: ").lower()

# Controlla se la scelta è valida (presente nel dizionario)
if scelta in password_types:
# Esegue la lambda corrispondente e ottiene lunghezza e charset
    length, charset = password_types[scelta]()
# Genera la password con i parametri ottenuti
    password = generate_password(length, charset)
else:
# Se l'input non è valido, genera una password "punitiva" di 2000 caratteri
# Usa gli stessi caratteri della versione complessa
    password = generate_password(2000, string.ascii_letters + string.digits + string.punctuation)

# Mostra la password generata
print(password)


# NOTA IMPORTANTE su if/elif/else:

#Durante l'esecuzione del codice, il programma deve seguire questo if, 
#quindi compara questa variabile con quel valore. Se trova un elif sarà 
#un else if, quindi se la scelta di prima è giusta sicuramente le altre 
#non lo sono, quindi le salta.
#Mentre se ci fosse un if al posto di elif, comparirebbe la scelta a "c" 
#e poi ad "s", anche se la scelta fosse "c".
#In questo caso usiamo if/else perché abbiamo solo due condizioni:
#- scelta valida (presente nel dizionario) 
#- scelta non valida (tutto il resto)
