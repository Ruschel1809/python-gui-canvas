import os

def erstelle_datei(datei:str, text:str, verzeichnis:str = "."):
    if not os.path.exists(verzeichnis):
        os.makedirs(verzeichnis)
    else:
        datei_mit_pfad = os.path.join(verzeichnis,datei)
        try:
            with open(datei_mit_pfad,'w') as d:
                d.write(text)
        except FileNotFoundError:
            pass
        except PermissionError:
            print(f"Keine Schreibberechtigung für die Datei {datei_mit_pfad}.")
        except IOError as e:
            print("Fehler beim Speichern der Datei: ", e)


def list_dir(verzeichnis:str,endung:str):
    return [datei for datei in os.listdir(verzeichnis) if datei.endswith(endung) and os.path.isfile(datei)]

def umbenennen_dateien (verzeichnis:str, endung:str, praefix:str):
    for d in list_dir(verzeichnis,endung):
        os.renames(d, praefix+d)

#Musterlösung

# a) Funktion erstelle_datei:
#
# import os
# def erstelle_datei(dateiname, inhalt, verzeichnis='.'):
#     voller_pfad = os.path.join(verzeichnis, dateiname)
#     try:
#         with open(voller_pfad, 'w') as datei:
#             datei.write(inhalt)
#         print(f"Datei '{dateiname}' wurde erfolgreich erstellt.")
#     except Exception as e:
#         print(f"Fehler beim Erstellen der Datei '{dateiname}': {e}")
# Beispielaufruf
#
# erstelle_datei('test.txt', 'Das ist ein Test.', 'meinVerzeichnis')
# b) Funktion listdir_filter:
#
# def listdir_filter(verzeichnis, endung):
#     return [datei for datei in os.listdir(verzeichnis) if datei.endswith(endung)]
# Beispielaufruf
#
# print(listdir_filter('.', '.txt'))
# c) Funktion umbenennen_dateien:
#
# def umbenennen_dateien(verzeichnis, alte_endung, präfix):
#     for datei in os.listdir(verzeichnis):
#         if datei.endswith(alte_endung):
#             neuer_name = präfix + datei
#             os.rename(os.path.join(verzeichnis, datei), os.path.join(verzeichnis, neuer_name))
#     print(f"Dateien wurden umbenannt.")
# Beispielaufruf
#
# umbenennen_dateien('.', '.txt', 'neu_')
# d) Funktion json_speichern:
#
# import json
# def json_speichern(daten, dateiname):
#     with open(dateiname, 'w') as datei:
#         json.dump(daten, datei)
# Beispielaufruf
#
# meine_daten = [{'name': 'Anna', 'alter': 28}, {'name': 'Bernd', 'alter': 35}]
# json_speichern(meine_daten, 'daten.json')
# e) Funktion json_laden:
#
# def json_laden(dateiname):
#     with open(dateiname, 'r') as datei:
#         return json.load(datei)
# Beispielaufruf
#
# geladene_daten = json_laden('daten.json')
# print(geladene_daten)
# f) Funktion regex_suche:
#
# import re
# def regex_suche(verzeichnis, regex):
#     passende_dateien = []
#     for datei in os.listdir(verzeichnis):
#         if datei.endswith('.txt'):
#             with open(os.path.join(verzeichnis, datei), 'r') as f:
#                 inhalt = f.read()
#                 if re.search(regex, inhalt):
#                     passende_dateien.append(datei)
#     return passende_dateien
# Beispielaufruf
#
# print(regex_suche('.', r'\bTest\b'))


