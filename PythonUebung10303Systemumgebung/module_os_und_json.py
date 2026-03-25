#-----------------------------------------------------------------------
# Dateiname: module_os_und_json.py
#-----------------------------------------------------------------------
# Beschreibung:
# Das Programm legt ein Verzeichnis meine_daten an, wenn sie nicht existiert
# und speichert eine json namens daten.json, die eine Wörterbuch speichert.
# Jedes Wörterbuch enthält die Schlüssel name, alter, beruf mit Werten.
# Weiterhin enthält das Programm Funktionen zur Bearbeitung der Datei.
# Autor: Helena Rusch
# Letzte Änderung: 27.06.2025
#-----------------------------------------------------------------------

import os, json

def lege_verzeichnis_an(verzeichnis: str):
    if not os.path.exists(verzeichnis):
        os.makedirs(verzeichnis)
    else:
       print("Verzeichnis existiert bereits.")


def aktualisiere_daten(d:list, dateiname:str):


   # Musterlösung - hängt bei mir keine Daten an
    # try:
    #
    #     with open(os.path.join(dateiname, 'daten.json'), 'r+') as datei:
    #         eintrag = json.load(datei)
    #         eintrag.append(neuer_eintrag)
    #         datei.seek(0)
    #         json.dump(daten, datei)
    # except FileNotFoundError:
    #     print("Die Datei wurde nicht gefunden.")

    existing = []
    try:
        with open(dateiname, "r") as f:
            existing = json.load(f)
    except FileNotFoundError:
        pass  # Datei gibt es noch nicht, nicht schlimm
    except json.JSONDecodeError as e:
        existing = []
        print("Datei existiert, enthält aber kein gültiges JSON: ", e)
    except IOError as e:
        print("Fehler beim Lesen: ", e)
    for n in d:
        existing.append(n)
    try:
        with open(dateiname, 'w', encoding="utf-8") as datei:
            json.dump(existing, datei)
    except FileNotFoundError:
        pass
    except IOError as e:
        print("Fehler beim Speichern der Datei: ",e)

def speichere_json(d:list, dateiname:str):
    try:
        with open(dateiname, 'w', encoding="utf-8") as datei:
            json.dump(d, datei)
    except FileNotFoundError:
        pass
    except IOError as e:
        print("Fehler beim Speichern der Datei: ",e)

def json_laden(dateiname:str):
    try:
        with open(dateiname, 'r',encoding="utf-8") as datei:
            return json.load(datei)
    except FileNotFoundError:
        print("Datei existiert noch nicht.")
        return None
    except IOError as e:
        print("Fehler beim Lesen der Datei: ",e)
        return None


daten = [
    {"name":"Anna", "alter":23, "beruf":"Bäcker"},
    {"name":"Bobo", "alter":34, "beruf":"Müller"},
    {"name":"Cora", "alter":43, "beruf":"Schuster"}]

lege_verzeichnis_an("meine_daten")
speichere_json(daten, "meine_daten\\daten.json")

name = input("name: ").strip()
alter = input("alter: ").strip()
beruf = input("beruf: ").strip()
neuer_eintrag = [{"name":name, "alter":alter, "beruf":beruf}]
aktualisiere_daten(neuer_eintrag, "meine_daten\\daten.json")