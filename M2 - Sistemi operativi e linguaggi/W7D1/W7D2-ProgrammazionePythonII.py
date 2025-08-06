'''
Traccia:
Scrivi una funzione che data in ingresso una lista A contenente n parole,
restituisca in output una lista B di interi che rappresentano la 
lunghezza delle parole contenute in A.

'''

def metodo_uno(a: list[str]) -> list[int]:
# Metodo uno : usa un ciclo for esplicito per calcolare le lunghezze.
# I parametri della funzione sono:
# una lista vuota di stringhe 
# 
# La funzione ci restuisce una lista di interi che rappresentano 
# la lunghezza delle parole contenute in a

# Inizializziamo una lista vuota che conterrà le lunghezze
    b = []
    
# Iteriamo su ogni parola nella lista di input
    for parola in a:
# len() restituisce il numero di caratteri della stringa
# append() aggiunge la lunghezza alla fine della lista
        b.append(len(parola))
    
    return b


# Lista di test con parole di lunghezze diverse
a = ["Ciao", "sono", "Giuseppe", "di", "EPICODE"]

# Chiamiamo il metodo
b = metodo_uno(a)

# Output dei risultati
print("Lista originale:", a)
print("Lunghezze parole:", b)
