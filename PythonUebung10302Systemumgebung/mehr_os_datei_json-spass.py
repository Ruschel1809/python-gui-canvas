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



