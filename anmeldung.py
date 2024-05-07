import getpass
import pw

def nutzer_anmelden():
    with open(“user.txt”) as fd:
        print("Willkommen zur Anmeldung")
        nutzername = input("Bitte gib deinen Nutzernamen ein: ")
        pw.passwort_pruefen()  # You missed parentheses to call the function

def neuer_nutzer():
    print("Willkommen bei der Registrierung")

def nutzer_loeschen():
    print("TODO löschen")    

def main():
    print("Guten Tag - Willkommen bei der Anmeldung\n")
    print("Wenn du dich mit deinen Nutzerdaten anmelden möchtest, wähle >a<")
    print("Wenn du ein neues Nutzerkonto anlegen möchtest, wähle >n<")
    print("Falls du dich wieder abmelden möchtest, wähle >e<\n")

    auswahl = None  # Initialize auswahl
    while auswahl not in ('a', 'n', 'e'):
        auswahl = input("Bitte wähle zwischen >a< (Anmelden), >n< (Neues Konto) oder >e< (Ende): ").lower()
    
        if auswahl == 'a':
            nutzer_anmelden()
        elif auswahl == 'n':
            neuer_nutzer()
        elif auswahl == 'e':
            print("Programm beendet")
            exit()

if __name__ == "__main__":
    main()
