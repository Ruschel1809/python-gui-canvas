import os


def erstelle_verzeichnis(verzeichnis:str):
    try:
        os.makedirs(verzeichnis)
        print(f"Verzeichnis: \"{verzeichnis}\" wurde erstellt.")
    except OSError as e:
        print(f"Das Verzeichnis {verzeichnis} existiert bereits: {e}")


def speichere_text_in_datei(dateiname:str, text:str):
    try:
        with open(dateiname,"w") as f:
            f.write(text)
    except FileNotFoundError:
        pass
    except IOError as e:
        print(f"Fehler beim Speichern der Datei: {e}")

def lese_datei(dateiname:str) -> str | None:
    try:
        with open(dateiname,"r") as f:
            return f.read()
    except FileNotFoundError:
        print("Datei nicht gefund!")
    except IOError as e:
        print(f"Fehler beim Lesen der Datei: {e}")
    return None

def liste_dateien_in_verzeichnis(verzeichnis:str):
    liste = []
    for v, _, d in os.walk(verzeichnis):
        for datei in d:
            liste.append(os.path.join(v,datei))
    return liste

def main():
    erstelle_verzeichnis("MeineDaten")
    speichere_text_in_datei("MeineDaten/beispiel.txt","meine daten in einer textdatei")
    print(lese_datei("MeineDaten/beispiel.txt"))
    print(liste_dateien_in_verzeichnis("MeineDaten"))

if __name__ == "__main__":
    main()


# Musterlösung
#
# import os
# def erstelle_verzeichnis(verzeichnisname):
#     if not os.path.exists(verzeichnisname):
#         os.makedirs(verzeichnisname)
#         print(f"Verzeichnis '{verzeichnisname}' wurde erstellt.")
#     else:
#         print(f"Verzeichnis '{verzeichnisname}' existiert bereits.")
#
#
# def speichere_text_in_datei(dateiname, text):
#     with open(dateiname, 'w') as datei:
#         datei.write(text)
#     print(f"Text wurde in '{dateiname}' gespeichert.")
#
#
# def lese_datei(dateiname):
#     try:
#         with open(dateiname, 'r') as datei:
#             inhalt = datei.read()
#             print(f"Inhalt von '{dateiname}':\n{inhalt}")
#     except FileNotFoundError:
#         print(f"Die Datei '{dateiname}' wurde nicht gefunden.")
#
#
# def liste_dateien_in_verzeichnis(verzeichnisname):
#     dateien = os.listdir(verzeichnisname)
#     print(f"Dateien in '{verzeichnisname}':")
#     for datei in dateien:
#         print(datei)
#
#
# Hauptprogramm
#
# verzeichnisname = "MeineDaten"
# dateiname = os.path.join(verzeichnisname, "beispiel.txt")
# text = "Das ist ein Beispieltext."
#
#
# erstelle_verzeichnis(verzeichnisname)
# speichere_text_in_datei(dateiname, text)
# lese_datei(dateiname)
# liste_dateien_in_verzeichnis(verzeichnisname)