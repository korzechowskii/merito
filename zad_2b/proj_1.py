class ITResource:
    def __init__(self):
        self.resources = {}
    
    def add_resource(self, name, type):
        if name not in self.resources:
            self.resources[name] = {"type": type, "status": "dostępny"}
            print(f"Zasób '{name}' ({type}) dodany do systemu.")
        else:
            print(f"Zasób o nazwie '{name}' już istnieje w systemie.")
    
    def list_resources(self):
        print("Lista dostępnych zasobów:")
        for name, details in self.resources.items():
            print(f"{name} ({details['type']}) - {details['status']}")
    
    def reserve_resource(self, name):
        if name in self.resources and self.resources[name]["status"] == "dostępny":
            self.resources[name]["status"] = "zarezerwowany"
            print(f"Zasób '{name}' został zarezerwowany.")
        else:
            print(f"Zasób '{name}' jest już zarezerwowany lub nie istnieje.")
    
    def return_resource(self, name):
        if name in self.resources and self.resources[name]["status"] == "zarezerwowany":
            self.resources[name]["status"] = "dostępny"
            print(f"Zasób '{name}' jest teraz dostępny.")
        else:
            print(f"Zasób '{name}' nie jest zarezerwowany lub nie istnieje.")

# Tworzenie instancji klasy ITResource
resource_manager = ITResource()

# Dodawanie zasobów
resource_manager.add_resource("Laptop Lenovo", "laptop")
resource_manager.add_resource("Serwer HP", "serwer")
resource_manager.add_resource("Drukarka Canon", "drukarka")

# Wyświetlanie dostępnych zasobów
resource_manager.list_resources()

# Rezerwacja i zarządzanie zasobami
resource_manager.reserve_resource("Laptop Lenovo")
resource_manager.list_resources()
resource_manager.return_resource("Laptop Lenovo")
resource_manager.list_resources()
