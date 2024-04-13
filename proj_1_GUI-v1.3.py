import os
import tkinter as tk
from tkinter import messagebox
import logging
from tkinter import ttk  # Import ttk module for styled widgets

style.theme_use('alt')  # Zmień na inne dostępne motywy jak 'alt', 'default', 'classic

# Konfiguracja systemu logowania
logging.basicConfig(filename='app.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class ITResource:
    def __init__(self):
        self.resources = {}
        logging.info("System zarządzania zasobami został zainicjowany.")

    def add_resource(self, name, type, description):
        if name not in self.resources:
            self.resources[name] = {
                "type": type,
                "description": description,
                "status": "dostępny",
                "reservation_time": None
            }
            logging.info(f"Zasób '{name}' został dodany do systemu.")
            return True
        else:
            logging.warning(f"Próba dodania zasobu, który już istnieje: '{name}'.")
            return False
    
    def list_resources(self):
        logging.info("Wygenerowano listę dostępnych zasobów.")
        resources_info = "Dostępne zasoby:\n"
        for name, details in self.resources.items():
            resources_info += f"{name} ({details['type']}) - {details['description']} - {details['status']}\n"
        return resources_info

class ITResourceGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("System Rezerwacji Zasobów IT")
        
        self.resource_manager = ITResource()

        tk.Label(master, text="Nazwa zasobu:").grid(row=0, column=0)
        tk.Label(master, text="Typ zasobu:").grid(row=1, column=0)
        tk.Label(master, text="Opis zasobu:").grid(row=2, column=0)

        self.name_var = tk.StringVar()
        self.type_var = tk.StringVar()
        self.description_var = tk.StringVar()

        tk.Entry(master, textvariable=self.name_var).grid(row=0, column=1)
        tk.Entry(master, textvariable=self.type_var).grid(row=1, column=1)
        tk.Entry(master, textvariable=self.description_var).grid(row=2, column=1)

        tk.Button(master, text="Dodaj zasób", command=self.add_resource).grid(row=3, column=0, columnspan=2)
        tk.Button(master, text="Wyświetl zasoby", command=self.display_resources).grid(row=4, column=0, columnspan=2)

    def add_resource(self):
        if self.resource_manager.add_resource(self.name_var.get(), self.type_var.get(), self.description_var.get()):
            messagebox.showinfo("System Rezerwacji", f"Zasób '{self.name_var.get()}' dodany pomyślnie.")
            logging.info(f"Zasób '{self.name_var.get()}' został pomyślnie dodany przez użytkownika.")
        else:
            messagebox.showerror("Błąd", f"Zasób '{self.name_var.get()}' już istnieje.")
            logging.error(f"Błąd podczas dodawania zasobu: '{self.name_var.get()}' już istnieje.")

    def display_resources(self):
        resources_info = self.resource_manager.list_resources()
        messagebox.showinfo("Lista Zasobów", resources_info)
        logging.info("Wyświetlono listę zasobów.")

# Uruchomienie GUI
root = tk.Tk()
app = ITResourceGUI(root)
root.mainloop()
