import logging
import argparse
import hashlib
import getpass
import os


def main():

    # Logging konfigurieren
    def logging():  
        logging.basicConfig(
            level = logging.DEBUG,
            format = "%(asctime)s %(levelname)s %(message)s",
            datefmt = "%Y-%m-%d %H:%M:%S",
            filename ="log.pw"
            )
    print("Das Prgrogramm pw kann benutzt werden um neue Passwörter zu prüfen, oder bestehende Passwörter zu überprüfen.")
    print("")

     
    while auswahl != 'n' or auswahl != 'p':
        auswahl = input("Bitte wähle ob du ein neues Passwort anlegen möchtest(n), oder ein bestehendes Passwort prüfen möchtest (p).")

    if auswahl == 'n':
        neues_passwort()
    elif auswahl == 'p':
        passwort_pruefen()

    # logging.debug("This is a debug message.")
    # logging.info("This is a info message.")
    # logging.warning("This ia warning message")
    # logging.error("This is an error message.")
    # logging.critical("This is an critical message.")

# neues passwort anlegen
def neues_passwort():
    logging.info("Der Benutzer hat die Funktion neues Passwort aufgerufen.")
    laenge_min = 8 # Minimallänge des Passowortes definieren

    print("Bitte wähle ein Passwort.")
    print("")
    print("Anforderungen an das Passwort:")
    print("Das Passwort muss mindestens " , laenge_min , " Zeichen Lang sein.")
    print("Das Passwort muss mindesten einen Großbuchstaben (A,B,C,...) enthalten.")
    print("Das Passwort muss mindesten einen Kleibuchstaben (a,b,c,...) enthalten.")
    print("Das Passwort muss mindesten eine Ziffer (0,1,2,...) enthalten.")   
    print("Das Passwort muss mindesten einen Sonderzeichen (*,',§,...) enthalten.")
    print("")

    neues_passwort = getpass.getpass("Bitte gib dein Passwort ein.")

    passwort_ok = False # Bedingung für die while-Schleife

    while passwort_ok == False:

        laenge_ok = False
        großbuchstaben = False
        kleinbuchstaben = False
        ziffern = False
        sonderzeichen = False

        # Passwort auf Länge prüfen
        laenge_passwort = len(neues_passwort)
        if laenge_passwort >= laenge_min:
            laenge_ok = True
            logging.info("Die Länge das Passwortes war ok.")
        else:
            print("Das Passwort ist zu kurz. Es muss mindestens >" , laenge_min , "< Zeichen lang sein.")    
            logging.info("Das ausgewählt Passwort war zu kurz.")

        # Paswort auf Großbuchstaben prüfen
        if any(char.isupper() for char in neues_passwort):
            großbuchstaben = True
            logging.info("Das Passwort hatte Großbuchstaben wie gefordert.")
        else:
            print("Das Passwort enthält keinen >Großbuchstaben<. es Passwort muss mindestens einen Großbuchstaben enthalten.")
            logging.info("Im Passwort fehlten Großbuchstaben.")

        # Passwort auf Kleinbuchstaben prüfen
        if any(char.islower() for char in neues_passwort):
            kleinbuchstaben = True
            logging.info("Das Passwort hatte Kleinbuchstaben wie gefordert.")
        else:
            print("Das Passwort enthält keinen >Kleinbuchstaben<. Es muss mindestens einen Kleinbuchstaben enthalten.")
            logging.info("Im Passwort fehlen Kleinbuchstaben.")

        # Passwort auf Ziffern prüfen
        if any(char.isdigit() for char in neues_passwort):
            ziffern = True
            logging.info("Das Passwort hatte Ziffern wie gefordert.")
        else:
            print("Das Passwort enthält keine >Ziffern<. Es muss mindestens eine Ziffer enthalten.")
            logging.info("Das Passwort hatte keine Ziffern.")    

        # Passwort auf Sonderzeichen prüfen 
        erlaubte_zeichen = neues_passwort.ascii_letters and neues_passwort.digits + ' '

        if any(char not in erlaubte_zeichen):
            sonderzeichen = True

        else:
            print("Das Passwort enthält keine >Sonderzeichen<. Es muss mindestens ein Sonderzeichen enthalten.") 

        if (laenge_ok == True and 
            laenge_ok == True and 
            großbuchstaben == True and 
            kleinbuchstaben == True and 
            ziffern == True and 
            sonderzeichen == False):
                passwort_ok = True

    print("Das Passwort ist ok.")
    logging.info("Das Passwort ist ok.")

    while neues_passwort != neues_passwort_wiederholen:
        neues_passwort_wiederholen = getpass.getpass("Bitte wiederhole dein Passwort")
        logging.info("Der Nutzer muss sein Passwort wiederholen.")
    

    # Passwort hashen     

    neues_passwort_bytes = neues_passwort.encode('utf-8') #Wandele den String in Bytes um
    logging.info("Passwort wurde in auf ganze Bytes erweitert.") 
    salt = os.urandom(16) # zufälligen Salt erzeugen 
    logging.info("Ein zufälliger Salt wurde erzeugt.")
    passwort_salt = neues_passwort_bytes + salt # encodiertes passwort und Salt kombinieren
    logging.info("Passwort und Salt wurden kombiniert.")
    hashobjekt = hashlib.sha512(passwort_salt) #Hashobjekt mit SHA-512 erzeugen
    logging.info("Ein sha512 Hashobjekt wurde mit Passwort und Salt erzeugt")
    passwort_neu_hashed = hashobjekt.hexdigest() #Erhalte die hexadezimale Darstellung des Hashwertes
    logging.info("")
    return passwort_neu_hashed, salt 

# passwort prüfen
def passwort_pruefen(zu_pruefendes_passwort, salt, password_gespeichert):    
    zu_pruefendes_passwort = getpass.getpass("Bitte gib dein Passwort ein.")
    zu_pruefendes_passwort_passwort_bytes = zu_pruefendes_passwort.encode('utf-8') # Wandele den String in Bytes um
    passwort_salt = zu_pruefendes_passwort_passwort_bytes + salt # encodiertes passwort und Salt kombinieren

    if password_gespeichert == passwort_salt:
        return True
    else:
        False 

if __name__ == "__main__":

    print("Hier ist noch nichts los.")
# Dieses Python Modul verarbeitet Passwörter.

