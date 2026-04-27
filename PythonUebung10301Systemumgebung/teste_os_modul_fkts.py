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
