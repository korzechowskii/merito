import tkinter as tk
from tkinter import messagebox
from datetime import datetime

class ITResource:
    def __init__(self):
        self.resources = {}
    
    def add_resource(self, name, type):
        if name not in self.resources:
            self.resources[name] = {"type": type, "status": "dostępny", "reservation_time": None}
            return True
        else:
            return False
    
    def list_resources(self):
        resources_info = "Dostępne zasoby:\n"
        for name, details in self.resources.items():
            status_info = f"{details['status']}"
            if details["reservation_time"]:
                status_info += f" do {details['reservation_time']}"
            resources_info += f"{name} ({details['type']}) - {status_info}\n"
        return resources_info
    
    def reserve_resource(self, name, time):
        if name in self.resources and self.resources[name]["status"] == "dostępny":
            self.resources[name]["status"] = "zarezerwowany"
            self.resources[name]["reservation_time"] = time
            return True
        else:
            return False
    
    def return_resource(self, name):
        if name in self.resources and self.resources[name]["status"] == "zarezerwowany":
            self.resources[name]["status"] = "dostępny"
            self.resources[name]["reservation_time"] = None
            return True
        else:
            return False

class ITResourceGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("System Rezerwacji Zasobów IT")
        
        self.resource_manager = ITResource()
        
        # Elementy GUI
        tk.Label(master, text="Nazwa zasobu:").grid(row=0)
        tk.Label(master, text="Typ zasobu:").grid(row=1)
        tk.Label(master, text="Czas rezerwacji (DD-MM-YYYY HH:MM):").grid(row=2)
        
        self.name_var = tk.StringVar()
        self.type_var = tk.StringVar()
        self.time_var = tk.StringVar()
        
        tk.Entry(master, textvariable=self.name_var).grid(row=0, column=1)
        tk.Entry(master, textvariable=self.type_var).grid(row=1, column=1)
        tk.Entry(master, textvariable=self.time_var).grid(row=2, column=1)
        
        tk.Button(master, text="Dodaj zasób", command=self.add_resource).grid(row=3, column=1)
        tk.Button(master, text="Rezerwuj zasób", command=self.reserve_resource).grid(row=4, column=1)
        tk.Button(master, text="Zwrot zasobu", command=self.return_resource).grid(row=5, column=1)
        tk.Button(master, text="Wyświetl zasoby", command=self.display_resources).grid(row=6, column=1)

    def add_resource(self):
        if self.resource_manager.add_resource(self.name_var.get(), self.type_var.get()):
            messagebox.showinfo("System Rezerwacji", f"Zasób '{self.name_var.get()}' dodany.")
        else:
            messagebox.showerror("Błąd", f"Zasób '{self.name_var.get()}' już istnieje.")

    def reserve_resource(self):
        if self.resource_manager.reserve_resource(self.name_var.get(), self.time_var.get()):
            messagebox.showinfo("System Rezerwacji", f"Rezerwacja zasobu '{self.name_var.get()}' na czas {self.time_var.get()} została dokonana.")
        else:
            messagebox.showerror("Błąd", "Rezerwacja nieudana, zasób jest już zarezerwowany lub nie istnieje.")

    def return_resource(self):
        if self.resource_manager.return_resource(self.name_var.get()):
            messagebox.showinfo("System Rezerwacji", f"Zasób '{self.name_var.get()}' jest teraz dostępny.")
        else:
            messagebox.showerror("Błąd", "Zwrot nieudany, zasób nie jest zarezerwowany lub nie istnieje.")

    def display_resources(self):
        resources_info = self.resource_manager.list_resources()
        messagebox.showinfo("Lista Zasobów", resources_info)

# Uruchomienie GUI
root = tk.Tk()
app = ITResourceGUI(root)
root.mainloop()
