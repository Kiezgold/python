import os
import shutil

# Pfad zum Ordner auf dem Desktop
desktop_path = os.path.expanduser("~/Desktop")
# Ordner "Alt" entsprechend anpassen
old_folder_path = os.path.join(desktop_path, "Alt")
# Ordner "Neu" entsprechend anpassen
destination_folder = os.path.join(desktop_path, "Neu")

# Erstellt den Zielordner "Neu", falls er nicht existiert
if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

# Durchsucht alle Unterordner im "Alt"-Ordner
for root, dirs, files in os.walk(old_folder_path):
    for file in files:
        # Erstellt den vollständigen Pfad zur Datei
        file_path = os.path.join(root, file)
        # Kopiert die Datei in den Zielordner
        shutil.copy(file_path, destination_folder)

print(f"Alle Dateien wurden in '{destination_folder}' kopiert.")

#Terminalbefehl: 
# cd desktop
# python3 copy_all_files.py
