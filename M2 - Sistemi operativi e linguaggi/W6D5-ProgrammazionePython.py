'''
Traccia: 

Si scriva un programma in Python che in base alla scelta dellʼutente permetta 
di calcolare il perimetro di diverse figure geometriche 
(scegliete pure quelle che volete voi). 
Per la risoluzione dellʼesercizio abbiamo scelto:

-Quadrato (perimetro = (lato*4)
-Cerchio (circonferenza = (2*pi greco*r)
-Rettangolo (perimetro= (base*2 + altezza*2)

Facoltativo: 

Si adatti il precedente esercizio in modo che acquisisca da tastiera 
il valore immesso dallʼutente, calcoli il perimetro e lʼarea di una figura geometrica 
scelta dallʼutente, e utilizzi automaticamente il valore dellʼarea come valore 
per calcolare il perimetro e lʼarea della prossima figura geometrica scelta nuovamente 
dallʼutente. 

● Creare dunque una selezione multipla di figure da proporre allʼutente 
ad ogni nuovo calcolo. 

● Il valore iniziale viene immesso dallʼutente solo la prima volta allo start del software.
● Ogni volta che lʼutente seleziona una figura, questa viene tolta 
dalle prossime opzioni presentate. Ripetere il procedimento per 
almeno 3 figure geometriche (es. quadrato, rettangolo, cerchio). 

Es.

1° figura: Quadrato → lato = 3; perimetro = 12; area = 9. 
2° figura: Rettangolo → lato = 9; perimetro = 27 (9*2 + 4,5*2); area = 40,5 (9*4,5).

'''

import math

def scelta_utente(scelte_possibili:list[int]) -> int:

# Nella funzione scelta_utente succede che, ci sarà una domanda che
# ti chiede cosa vuoi tra i seguenti, se 1 è tra le opzioni
# delle scelte possibili comparirà l'opzione 1 e calcolerà
# il perimetro e l'area del quadrato, se 2 è tra le opzioni
# delle scelte possibili comparirà l'opzione 2 e calcolerà
# il perimetro e l'area del cerchio, se 3 è tra le opzioni
# delle scelte possibili comparirà l'opzione 3 e calcolerà
# il perimetro e l'area del rettangolo.

    print("Dimmi che vuoi tra")
    if 1 in scelte_possibili:
        print("\t1) Perimetro e area del quadrato")
    if 2 in scelte_possibili:
        print("\t2) Perimetro e area del cerchio")
    if 3 in scelte_possibili:
        print("\t3) Perimetro e area del rettangolo")
    
# Come prima ci sarà un while per controllare la scelta dell'utente,
# se mette un valore non valido (non numerico), ci sarà l'eccezione
# e farà richiedere di nuovo all'utente di scegliere.

    ok = False
    while not ok:
        try:
            opzione:int = int(input("Scegli: "))

# Abbiamo un controllo ulteriore, perché l'utente può
# scegliere soltanto qualcosa che non è stato scelto, quindi qualcosa
# tra le scelte possibili, quindi se l'opzione scelta è tra
# le scelte possibili, il valore booleano ok passa a true e si esce
# dal ciclo while e si ritorna l'opzione scelta

            if opzione in scelte_possibili:
                ok = True
            else:

                # altrimenti la scelta non andava bene e si ricomincia il ciclo while
                # finché l'utente non sceglierà un valore tra le scelte possibili

                print(f"La tua scelta ({opzione}) non andava bene!")
        except ValueError:
            print("Dammi un valore numerico!!")
    return opzione

# Iniziamo con un while che chiede di scegliere un valore,
# finché non viene fornito un valore numerico. Questo lo fa convertendo
# il valore in float, se non riesce perché la stringa passata non contiene
# un numero ma dei caratteri, questa conversione lancerà un'eccezione
# che noi catturiamo con questa struttura, try except e diciamo di darci
# un valore numerico, la variabile booleana ok verrà passata a true quando
# verrà passato un valore numerico.

ok = False
while not ok:
    try:
        valore:float = float(input("Scegli un valore: "))
        ok = True
    except ValueError:
        print("Dammi un valore numerico!!")

# Non appena abbiamo il nostro valore che è un float inizializziamo perimetro e area a 0

perimetro: float = 0.0
area: float = 0.0

# Definiamo delle scelte possibili (1,2,3). Perché abbiamo scelta 1,
# scelta 2 e scelta 3,
# perché possiamo fare perimetro e area del quadrato,
# perimetro e area del cerchio e perimetro e area del rettangolo.

scelte_possibili = [1, 2, 3]

# In un altro ciclo while andremo a rimuovere elementi dalla lista
# di scelte possibili a seconda della scelta utente.
# Quindi l'utente sceglierà l'opzione 1, rimuoveremo da
# scelte possibili il valore 1 e così via (questo ciclo itererà tre volte).

while len(scelte_possibili) > 0:

    # questa opzione arriverà dove abbiamo richiamato la nostra funzione
    opzione = scelta_utente(scelte_possibili)

    # e verrà rimossa tra le scelte possibili

    scelte_possibili.remove(opzione)
    
    # e poi si svolge il calcolo vero e proprio,
    # se è l'opzione 1, si calcola il perimetro e l'area del quadrato

    if opzione == 1:
        perimetro = valore * 4
        area = valore * valore

    # se è l'opzione 2, si calcola il perimetro e l'area del cerchio
   
    elif opzione == 2:
        perimetro = 2 * math.pi * valore
        area = valore * valore * math.pi

    # se è l'opzione 3, si calcola il perimetro e l'area del rettangolo
    
    elif opzione == 3:
        # lato corto (l) è metà lato lungo (L)
        # (2 * L + 2 * l) = (2 * L + L) = (3 * L)
        perimetro = 3 * valore
        area = valore * valore / 2

    else:

        # Se dovesse fallire tutto il resto, c'è l'eccezione impossibile,
        # in realtà non dovremo mai arrivare qua perché le scelte possibili
        # sono 1,2,3 che andiamo a togliere da queste scelte possibili,
        # quindi non ci dovrebbe essere nessun'altra scelta

        raise Exception("Eccezzione Impossibile!!!!!!!!!")
    
    # dopodiché impostiamo il valore che sarà usato alla prossima iterazione,
    # sarà impostato come area dell'iterazione precedente

    valore = area
    
    # stampiamo perimetro e area e si ricomincia il ciclo
    
    print(f"Perimetro: {perimetro:.2f}")
    print(f"Area: {area:.2f}")