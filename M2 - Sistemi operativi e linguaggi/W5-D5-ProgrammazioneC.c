/*Traccia: 
Si scriva un programma in linguaggio C che, 
dato un numero reale D immesso da tastiera, calcoli e stampi: 

● l’area del quadrato di lato D
● l’area del cerchio di diametro D  
● l’area del triangolo equilatero di lato D 

Facoltativo:
 Si scriva un programma in linguaggio C che permetta di far inserire da tastiera 
 una serie di numeri (a vostra scelta ma minimo 3) 
 e si vada poi a calcolare la media aritmetica facendo stampare
il risultato sia con 2 cifre decimali e sia senza cifre decimali,
arrotondando quindi il risultato. Unendo i due esercizi, 
entrambi i risultati sopra citati verranno utilizzati per presentare all’utente: 

● l’area del quadrato (sia utilizzando il valore decimale che quello arrotondato)
● l’area del cerchio (sia utilizzando il valore decimale che quello arrotondato) 
● l’area del triangolo equilatero (sia utilizzando il valore decimale che quello arrotondato)
*/

#include <stdio.h>
#include <math.h>

int main()
{
    double D;
    double D1, D2, D3;
    
    printf("\n Inserisci un numero: ");
    scanf("%lf", &D);  
    

    printf("\n Inserisci tre numeri: ");
    scanf("%lf %lf %lf", &D1, &D2, &D3);  

    double media = (D1 + D2 + D3) / 3;
    
    // Calcolo e stampa delle aree 
    printf("\n L'area del quadrato è %.0f %.2f", D * D, D * D);
    printf("\n L'area del triangolo è %.0f %.2f", sqrt(3)/4 * D * D, sqrt(3)/4 * D * D);
    printf("\n L'area del cerchio è %.0f %.2f", M_PI * D * D / 4, M_PI * D * D / 4);

    // STampa del risultato del calcolo della media
    printf("\n La media aritmetica è %.0f %.2f" ,media ,media);
    
    return 0;
}
