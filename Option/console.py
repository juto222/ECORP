from colorama import Fore, Style
import os 

def console():
    def clear():
        os.system('cls')

    payloads = [
        "Clipboard",
        "Screenshot",
        "Directory listing",
        "File Grabber",
        "keyboard controller",
        "Network info",
        "Open url",
        "Port Hammer",
        "Procces View",
        "Restart PC",
        "Reverse HTTP",
        "Reverse Shell",
        "Remove Directory",
        "Remove file",
        "Run Command on terminal",
        "Stealer",
        "Voice record",
        "Change wallpaper",
        "Wifi SSiD"
    ]

    captures = [
        "phishing",
        "keylogger",
    ]

    scanners = [
        "Port Scanner",
        "Vulnerability Scanner",
        "Network Scanner"
        "Directrory Scanner"
        "Localhost Scanner"
    ]

    import time
    global tps
    print(Fore.CYAN + "\n=== Console Interactive ===\n")
    print(Fore.YELLOW + "Entrez 'payload' ou 'capture' ou 'scan' pour accéder aux modules correspondants.")
    while True:
        cmd = input(Fore.GREEN + ">> " + Style.RESET_ALL)
        if cmd.lower() == "payload":
            clear()
            print(f"""{Fore.CYAN}=== Modules Payload ==={Style.RESET_ALL}

    {Fore.YELLOW}Liste des payloads disponibles :{Style.RESET_ALL}

        1. Clipboard
        2. Screenshot
        3. Directory listing
        4. File Grabber
        5. keyboard controller
        6. Network info
        7. Open url
        8. Port Hammer
        9. Procces View
        10. Restart PC
        11. Reverse HTTP
        12. Reverse Shell
        13. Remove Directory
        14. Remove file
        15. Run Command on terminal
        16. Stealer
        17. Voice record
        18. Change wallpaper
        19. Wifi SSiD

    """)
            payload_choix = input(Fore.GREEN + ">> " + Style.RESET_ALL)
            if payload_choix.lower() == "back":
                clear()
                continue
            try:
                payload_index = int(payload_choix) - 1
                if 0 <= payload_index < len(payloads):
                    print(Fore.YELLOW + f"Configuration du payload : {payloads[payload_index]}" + Style.RESET_ALL)
                else:
                    print(Fore.RED + "Numéro de payload invalide." + Style.RESET_ALL)
            except ValueError:
                print(Fore.RED + "Veuillez entrer un numéro valide." + Style.RESET_ALL)

        elif cmd.lower() == "capture":
            clear()
            print(Fore.CYAN + "=== Modules Capture ===" + Style.RESET_ALL)
            print(Fore.YELLOW + "Liste des captures disponibles :" + Style.RESET_ALL)
            print("""
                  
        1. phishing
        2. keylogger
                  
                  """)
            capture_choix = input(Fore.GREEN + ">> " + Style.RESET_ALL)
            if capture_choix.lower() == "back":
                clear()
                continue
            try:
                capture_index = int(capture_choix) - 1
                if 0 <= capture_index < len(captures):
                    print(Fore.YELLOW + f"Configuration de la capture : {captures[capture_index]}" + Style.RESET_ALL)
                else:
                    print(Fore.RED + "Numéro de capture invalide." + Style.RESET_ALL)
            except ValueError:
                print(Fore.RED + "Veuillez entrer un numéro valide." + Style.RESET_ALL)
        
        elif cmd.lower() == "scan":
            clear()
            print(Fore.CYAN + "=== Modules Scan ===" + Style.RESET_ALL)
            print(Fore.YELLOW + "Liste des scanners disponibles :" + Style.RESET_ALL)
            print("""
        1. Port Scanner
        2. Vulnerability Scanner
        3. Network Scanner
        4. Directrory Scanner
        5. Localhost Scanner
                  """)
            scan_choix = input(Fore.GREEN + ">> " + Style.RESET_ALL)
            if scan_choix.lower() == "back":
                clear()
                continue
            try:
                scan_index = int(scan_choix) - 1
                if 0 <= scan_index < len(scanners):
                    print(Fore.YELLOW + f"Configuration du scanner : {scanners[scan_index]}" + Style.RESET_ALL)
                else:
                    print(Fore.RED + "Numéro de scanner invalide." + Style.RESET_ALL)
            except ValueError:
                print(Fore.RED + "Veuillez entrer un numéro valide." + Style.RESET_ALL)

        elif cmd.lower() in ["exit", "quit"]:
            print(Fore.CYAN + "Fermeture de la console interactive." + Style.RESET_ALL)
            break
        else:
            print(Fore.RED + "Commande inconnue. Veuillez entrer 'payload', 'capture', 'scan' ou 'exit'." + Style.RESET_ALL)

    
    




console()