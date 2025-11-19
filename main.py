import os
import time
from colorama import init, Fore, Style
from Option import PingIP
from Option import CheckMDP
from Option import GenererMDP
from Option import phishing
#from Option import Scan
#from Option import keylog
from Option import pswd
from Option import quizzmdp
from Option import quizzsecurity
from Option import si
from Option import test_speed
from Option import script

# Initialisation de Colorama
init(autoreset=True)

# Efface le terminal
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# Affiche le menu principal en FR
def afficher_menuFR():
    clear()
    print(f"""{Fore.CYAN}{Style.BRIGHT}
═══════════════════════════════════════════════════════════════════════
{Fore.GREEN}
             @                                                                                                                  
          @@@@@@                                                                                                                
        @@@@@@@                                                                                                                 
     @@@@@@@@   @@                @@@@           @@@@@       @@@@@@@@@@     @@@@@@@@                                                          
  @@@@@@@@   @@@@@@@           @@@@@@@@@@@    @@@@   @@@@    @@@    @@@   @@@    @@@                                             
  @@@@@@@@@@@@@@@@            @@@            @@@       @@@   @@@    @@@   @@@    @@@                                            
    @@@@@@@@@@@@   @@@@@      @@@           @@@         @@@  @@@@@@@@@    @@@@@@@@@                                             
      @@@@@@@@   @@@@@@@@     @@@            @@@       @@@   @@@   @@@    @@@                                                   
       @@@@@@@@@@@@@@@         @@@@@@@@@@@    @@@@   @@@@    @@@    @@@   @@@                                                   
         @@@@@@@@@@                @@@@          @@@@@       @@@    @@@@  @@@                                                   
           @@@@@@                                                                                                               
            @@               @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@        

{Fore.CYAN}═══════════════════════════════════════════════════════════════════════

{Fore.MAGENTA}[1] 🔐 Mot de passe
    {Fore.YELLOW}├── [11] Générateur de mot de passe
    ├── [12] Vérificateur de mot de passe
    ├── [13] Quizz mot de passe
    └── [14] Mot de passe compromis

{Fore.MAGENTA}[2] 🛡 Pentest
    {Fore.YELLOW}├── [21] Virus (désactivé pour des raisons éthiques)
    ├── [22] Outil DDoS (désactivé pour des raisons éthiques)
    ├── [23] Générateur de fausse page HTML
    ├── [24] Keylogger (en dévoloppement)
    └── [25] Quizz sécurité
    └── [26] Scanner de sites web (à venir)

{Fore.MAGENTA}[3] 📊 Réseau
    {Fore.YELLOW}├── [31] Ping IP
    ├── [32] Scan Réseau (à venir)
    ├── [33] Journal / Logs
    ├── [34] Quizz réseau 
    └── [35] Speedtest Internet

{Fore.MAGENTA} [4] PC
├── [41] Informations système
├── [42] Gestionnaire de tâches (à venir)
├── [43] Nettoyeur de fichiers temporaires (à venir)
├── [44] Moniteur de ressources (à venir)
└── [45] Création de faux fichier

{Fore.MAGENTA}[5] ⚙️ Paramètres
    {Fore.YELLOW}├── [51] Mode sombre / clair
    ├── [52] Choix de langue (FR/EN)
    └── [53] Quitter

{Fore.MAGENTA}[6] ⚖️ Aide & Légalité
    {Fore.YELLOW}├── [61] Documentation utilisateur
    ├── [62] FAQ
    ├── [63] Mentions légales
    └── [64] Informations RGPD
═══════════════════════════════════════════════════════════════════════
{Style.RESET_ALL}""")

# Menu en anglais
def afficher_menuEN():
    clear()
    print(f"""{Fore.CYAN}{Style.BRIGHT}
═══════════════════════════════════════════════════════════════════════
{Fore.GREEN}
             @                                                                                                                  
          @@@@@@                                                                                                                
        @@@@@@@                                                                                                                 
     @@@@@@@@   @@                @@@@           @@@@@       @@@@@@@@@@     @@@@@@@@                                                          
  @@@@@@@@   @@@@@@@           @@@@@@@@@@@    @@@@   @@@@    @@@    @@@   @@@    @@@                                             
  @@@@@@@@@@@@@@@@            @@@            @@@       @@@   @@@    @@@   @@@    @@@                                            
    @@@@@@@@@@@@   @@@@@      @@@           @@@         @@@  @@@@@@@@@    @@@@@@@@@                                             
      @@@@@@@@   @@@@@@@@     @@@            @@@       @@@   @@@   @@@    @@@                                                   
       @@@@@@@@@@@@@@@         @@@@@@@@@@@    @@@@   @@@@    @@@    @@@   @@@                                                   
         @@@@@@@@@@                @@@@          @@@@@       @@@    @@@@  @@@                                                   
           @@@@@@                                                                                                               
            @@               @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@        

{Fore.CYAN}═══════════════════════════════════════════════════════════════════════

{Fore.MAGENTA}[1] 🔐 Password
    {Fore.YELLOW}├── [11] Password Generator
    ├── [12] Vérificateur de mot de passe
    ├── [12] Password Checker
    ├── [13] Password Quiz
    └── [14] Compromised Passwords

{Fore.MAGENTA}[2] 🛡 Pentest
    {Fore.YELLOW}├── [21] Virus (disabled for ethical reasons)
    ├── [22] DDoS Tool (disabled for ethical reasons)
    ├── [23] Fake HTML Page Generator
    ├── [24] Keylogger (in development)
    └── [25] Security Quiz

{Fore.MAGENTA}[3] 📊 Network
    {Fore.YELLOW}├── [31] Ping IP
    ├── [32] Scan Network (upcoming)
    ├── [33] Logs
    ├── [34] Network Quiz
    └── [35] Internet Speedtest

{Fore.MAGENTA} [4] PC
    {Fore.YELLOW}├── [41] System Information
    ├── [42] Task Manager (upcoming)
    ├── [43] Temporary File Cleaner (upcoming)
    ├── [44] Resource Monitor (upcoming)
    └── [45] Fake File Creator

{Fore.MAGENTA}[4] ⚙️ Settings
    {Fore.YELLOW}├── [41] Dark / Light Mode
    ├── [42] Language Selection (FR/EN)
    └── [43] Quit

{Fore.MAGENTA}[5] ⚖️ Help & Legal
    {Fore.YELLOW}├── [51] User Documentation
    ├── [52] FAQ
    ├── [53] Legal Notice
    └── [54] GDPR Information
═══════════════════════════════════════════════════════════════════════
{Style.RESET_ALL}""")

# execution securisé
def lancer(fonction, nom="Fonction"):
    clear()
    print(Fore.YELLOW + f"[ {nom} ]")
    try:
        fonction()
    except Exception as e:
        print(Fore.RED + f"❌ Erreur : {e}")
    input(Fore.GREEN + "\n✅ Appuyez sur Entrée pour revenir au menu...")

# Langue
clear()
langue_actuelle = input(Fore.CYAN + "🌐 Choisissez votre langue / Choose your language (FR/EN) : ").upper()
if langue_actuelle != "EN":
    langue_actuelle = "FR"  # FR par défaut

# Boucle principale
while True:
    if langue_actuelle == "EN":
        afficher_menuEN()
    else:
        afficher_menuFR()

    try:
        choix = int(input(Fore.CYAN + "Entrez votre choix / Enter your choice: "))
    except ValueError:
        print(Fore.RED + "❌ Veuillez entrer un numéro valide.")
        time.sleep(1.5)
        continue

    if choix == 11:
        lancer(GenererMDP.generer, "Générateur de mot de passe" if langue_actuelle == "FR" else "Password Generator")

    elif choix == 12:
        lancer(CheckMDP.verifier, "Vérificateur de mot de passe" if langue_actuelle == "FR" else "Password Checker")

    elif choix == 14:
        clear()
        lancer(pswd.pswd_compromis, "Mot de passe compromis" if langue_actuelle == "FR" else "Compromised Passwords")

    elif choix == 13:
        clear()
        if langue_actuelle == "FR":
            level = input("Choisissez le niveau de difficulté (1-Facile, 2-Moyen, 3-Difficile) : ")
        else:
            level = input("Choose difficulty level (1-Easy, 2-Medium, 3-Hard): ")
        lancer(lambda: quizzmdp.quizz_mdp(level), "Quizz mot de passe" if langue_actuelle == "FR" else "Password Quiz")

    elif choix == 21 or choix == 22:
        clear()
        print(Fore.RED + "❌ Fonction désactivée. / Feature disabled.")
        input(Fore.GREEN + "\nRetour... / Back...")

    elif choix == 23:
        clear()
        lancer(lambda: phishing.afficher_menu_phishing(langue_actuelle),
       "Générateur de fausse page HTML" if langue_actuelle == "FR" else "Fake HTML Page Generator")
        
    #elif choix == 24:
    #    clear()
    #    lancer(keylog.keylog, "Keylogger" if langue_actuelle == "FR" else "Keylogger")

    elif choix == 25:
        clear()
        if langue_actuelle == "FR":
            level = input("Choisissez le niveau de difficulté (1-Facile, 2-Moyen, 3-Difficile) : ")
        else:
            level = input("Choose difficulty level (1-Easy, 2-Medium, 3-Hard): ")
        lancer(lambda: quizzsecurity.quizzsecurity(level), "Quizz sécurité" if langue_actuelle == "FR" else "Security Quiz")



    elif choix == 31:
        lancer(PingIP.ping, "Ping IP" if langue_actuelle == "FR" else "Ping IP")

    #elif choix == 32:
    #    clear()
    #    lancer(Scan.scan, "Scan Réseau" if langue_actuelle == "FR" else "Network Scan")
    #    input(Fore.GREEN + "\nRetour... / Back...")
    
    elif choix == 33: 
        clear()
        with open("logs.txt", "r") as f:
            logs = f.read()
            print(Fore.YELLOW + logs)
            input(Fore.GREEN + "\nRetour... / Back...")

    elif choix == 34:
        clear()
        lancer(test_speed.test_speed, "Speedtest Internet" if langue_actuelle == "FR" else "Internet Speedtest")

    elif choix == 41:
        clear()
        lancer(si.info_system, "Informations système" if langue_actuelle == "FR" else "System Information")

    elif choix == 45:
        clear()
        lancer(script.fichier, "Création de faux fichier" if langue_actuelle == "FR" else "Fake File Creator")

    elif choix == 51:
        clear()
        if langue_actuelle == "FR":
            mode = input("Choisissez le mode (sombre/clair) : ").lower()
            if mode == "sombre":
                os.system('')  # Placeholder for dark mode
                print(Fore.GREEN + "🌙 Mode sombre activé.")
            elif mode == "clair":
                os.system('')  # Placeholder for light mode
                print(Fore.GREEN + "☀️ Mode clair activé.")
            else:
                print(Fore.RED + "❌ Mode non reconnu.")
            input(Fore.GREEN + "\nRetour au menu...")
        else:
            mode = input("Choose mode (dark/light): ").lower()
            if mode == "dark":
                os.system('')  # Placeholder for dark mode
                print(Fore.GREEN + "🌙 Dark mode activated.")
            elif mode == "light":
                os.system('')  # Placeholder for light mode
                print(Fore.GREEN + "☀️ Light mode activated.")
            else:
                print(Fore.RED + "❌ Mode not recognized.")
            input(Fore.GREEN + "\nReturn to menu...")

    elif choix == 52:
        clear()
        langue_actuelle = input("Choisissez votre langue (FR/EN) : ").upper()
        if langue_actuelle not in ["FR", "EN"]:
            print(Fore.RED + "❌ Langue non reconnue. / Language not recognized.")
            langue_actuelle = "FR"
        else:
            print(Fore.GREEN + f"🌐 Langue définie sur : {langue_actuelle}")
        input(Fore.GREEN + "\nRetour au menu...")

    elif choix == 53:
        clear()
        print(Fore.CYAN + "👋 Fermeture du programme. À bientôt ! / Program closing. See you!")
        break

    elif choix == 61:
        clear()
        print(Fore.YELLOW + (
            "\n📘 Documentation utilisateur :\n- Utilisez les numéros du menu pour accéder aux outils." if langue_actuelle == "FR"
            else "\n📘 User documentation:\n- Use the menu numbers to access tools."
        ))
        input(Fore.GREEN + "\nRetour... / Back...")

    elif choix == 62:
        clear()
        print(Fore.YELLOW + (
            "\n❓ FAQ :\nQ : Est-ce légal ?\nR : Oui, pour l’apprentissage uniquement." if langue_actuelle == "FR"
            else "\n❓ FAQ:\nQ: Is it legal?\nA: Yes, for learning only."
        ))
        input(Fore.GREEN + "\nRetour... / Back...")

    elif choix == 63:
        clear()
        print(Fore.YELLOW + (
            "\n⚠️ Mentions légales :\nCe programme est fourni à titre éducatif." if langue_actuelle == "FR"
            else "\n⚠️ Legal Notice:\nThis program is for educational purposes only."
        ))
        input(Fore.GREEN + "\nRetour... / Back...")

    elif choix == 64:
        clear()
        print(Fore.YELLOW + (
            "\n🔒 Données personnelles :\nCe programme ne collecte aucune information." if langue_actuelle == "FR"
            else "\n🔒 Personal data:\nThis program does not collect any information."
        ))
        input(Fore.GREEN + "\nRetour... / Back...")

    else:
        print(Fore.RED + "❌ Option invalide.")
        time.sleep(1.5)
