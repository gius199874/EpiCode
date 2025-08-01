/* Traccia: 
Esercizio Programmazione in C Lo scopo di oggi è realizzare un piccolo 
gioco di domanda/risposta in C, il numero e le domande sono a vostra scelta. 
Il gioco dovrà funzionare in modo tale da:

- Presentare una rapida introduzione allʼutente con lo scopo del programma
- Mostrare allʼutente un menu di scelta iniziale tra: A) Iniziare una nuova partita; B) Uscire dal gioco
 - Ricevere in input la scelta dellʼutente
 - Creare o meno una nuova partita in base allʼinput utente
 - Ricevere in input nome dellʼutente in caso di nuova partita
 - Presentare un set di domande allʼutente a risposta multipla
 (almeno 3 risposte a domanda)
 - Valutare la risposta utente per ogni domanda ed aggiornare una 
 variabile "punteggio in caso di risposta esatta"
- Scrivere a schermo a fine partita il punteggio totalizzato dal giocatore corrente
- Presentare nuovamente il testo per la scelta tra:
 A)Iniziare una nuova partita; B)Uscire dal gioco

Facoltativo:
Al completamento del precedente esercizio, sistemare il codice per far si 
che il punteggio rimanga in memoria e venga sommato partita dopo partita.

 */

#include <stdio.h>
#include <ctype.h>      // Per tolower()
#include <string.h>     // Per strcmp()
#include <stdbool.h>    // Per tipo bool

// Costante per identificare quando il nome non è stato ancora impostato
#define DEFAULT_NAME "----UNSET----"

// Dichiarazione delle funzioni
int partita();
int domanda(char*, int);
bool contains(int*, int, int);

int main()
{
    // Stampa l'introduzione del gioco
    printf("\n=== BENVENUTO AL QUIZ GAME ===\n");
    printf("Rispondi alle domande e accumula punti!\n");
    
    char *prompt_scelta = "\nScegli tra: \n\tA/1) Iniziare una nuova partita\n\tB/2) Uscire dal gioco";
    
    // Variabili principali
    char scelta;                        // La scelta dell'utente (A/B o 1/2)
    int score = 0;                      // Punteggio totale di tutte le partite
    char nome[512] = DEFAULT_NAME;      // Nome del giocatore
    bool ha_giocato = false;            // Per sapere se ha mai giocato
    
    // Ciclo principale che continua finché l'utente non esce
    while (true)
    {
        // Mostra il menu
        printf("%s", prompt_scelta);
        printf("\nComunicami la tua scelta: ");
        
        // Legge la scelta (lo spazio prima di %c pulisce il buffer)
        scanf(" %c", &scelta);
        
        // Controlla cosa ha scelto l'utente
        switch (tolower(scelta))
        {
            case 'a':
            case '1':  // Accetta sia lettere che numeri
                
                // Se è la prima volta, chiede il nome
                if (strcmp(nome, DEFAULT_NAME) == 0)
                {
                    printf("\nComunicami il tuo nome: ");
                    scanf("%s", nome);
                }
                
                // Segna che ha giocato e inizia la partita
                ha_giocato = true;
                printf("\n=== INIZIA LA PARTITA, %s! ===\n", nome);
                
                // Esegue la partita e aggiunge il punteggio al totale
                score += partita();
                
                printf("=== FINE PARTITA ===\n");
                printf("Punteggio totale: %d punti\n", score);
                break;
                
            case 'b':
            case '2':  // Accetta sia lettere che numeri
                
                // Messaggio di uscita diverso se ha giocato o no
                if (ha_giocato)
                {
                    printf("\nArrivederci %s! Il tuo punteggio finale è: %d punti\n", nome, score);
                }
                else
                {
                    printf("\nArrivederci! Non hai giocato nessuna partita.\n");
                }
                return 0; // Esce dal programma
                
            default:
                // Se scrive qualcosa di sbagliato
                printf("Scelta non valida! Riprova.\n");
                break;
        }
    }
    
    return 0;
}

// Funzione che gestisce una partita completa
int partita()
{
    int score = 0; // Punteggio di questa partita
    
    // Domanda 1
    score += domanda(
        "Domanda 1: Di che colore era il cavallo bianco di Napoleone?\n\t1) Bianco\n\t2) Nero\n\t3) Giallo",
        1  // La risposta corretta è 1
    );
    
    // Domanda 2
    score += domanda(
        "Domanda 2: Quanto fa 5 + 5?\n\t1) 10\n\t2) 37\n\t3) 42",
        1  // La risposta corretta è 1
    );
    
    // Domanda 3
    score += domanda(
        "Domanda 3: Qual è la capitale d'Italia?\n\t1) Milano\n\t2) Roma\n\t3) Napoli",
        2  // La risposta corretta è 2
    );
    
    // Domanda 4
    score += domanda(
        "Domanda 4: Qual è l'oceano più grande del mondo?\n\t1) Atlantico\n\t2) Indiano\n\t3) Pacifico",
        3  // La risposta corretta è 3
    );
    
    return score; // Restituisce il punteggio della partita
}

// Funzione che controlla se un numero è nell'array
bool contains(int *arr, int element, int size)
{
    // Controlla tutti gli elementi dell'array
    for (int i = 0; i < size; i++)
    {
        if (arr[i] == element)
        {
            return true; // Trovato!
        }
    }
    return false; // Non trovato
}

// Funzione che fa una singola domanda
int domanda(char *d, int correct)
{
    int scelta;                          // La risposta dell'utente
    int possible_answer[] = {1, 2, 3};   // Le risposte valide
    
    // Continua a chiedere finché non dà una risposta valida
    while (true)
    {
        // Stampa la domanda
        printf("\n%s\nRisposta: ", d);
        scanf("%d", &scelta);
        
        if (scelta == correct)
        {
            // Risposta giusta = 1 punto
            printf(" Risposta corretta! +1 punto\n");
            return 1;
        }
        else if (contains(possible_answer, scelta, 3))
        {
            // Risposta sbagliata ma valida = 0 punti
            printf(" Risposta sbagliata!\n");
            return 0;
        }
        else
        {
            // Risposta non valida = riprova
            printf("Opzione non valida! Scegli 1, 2 o 3.\n");
        }
    }
}