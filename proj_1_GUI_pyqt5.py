import sys
import logging
import csv
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox, QDateEdit
from PyQt5.QtCore import QDate

# Konfiguracja systemu logowania
logging.basicConfig(filename='app.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class ITResource:
    def __init__(self):
        self.resources = {}
        self.csv_file = 'resources.csv'
        # Sprawdzenie, czy plik już istnieje, aby zdecydować o dodaniu nagłówków
        try:
            with open(self.csv_file, 'x', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(['Name', 'Type', 'Description', 'Status', 'Reservation Time'])
        except FileExistsError:
            pass  # Plik już istnieje, nagłówki nie są potrzebne

    def add_resource(self, name, type, description, reservation_date):
        if name not in self.resources:
            self.resources[name] = {
                "type": type,
                "description": description,
                "status": "dostępny",
                "reservation_time": reservation_date.toString('yyyy-MM-dd')
            }
            self.save_to_csv(name, type, description, reservation_date.toString('yyyy-MM-dd'))
            logging.info(f"Zasób '{name}' został dodany do systemu.")
            return True
        else:
            logging.warning(f"Próba dodania zasobu, który już istnieje: '{name}'.")
            return False

    def save_to_csv(self, name, type, description, reservation_date):
        with open(self.csv_file, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([name, type, description, 'dostępny', reservation_date])
    
    def list_resources(self):
        logging.info("Wygenerowano listę dostępnych zasobów.")
        resources_info = "Dostępne zasoby:\n"
        for name, details in self.resources.items():
            resources_info += f"{name} ({details['type']}) - {details['description']} - {details['status']} - {details['reservation_time']}\n"
        return resources_info

class ITResourceGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('System Rezerwacji Zasobów IT')
        self.setGeometry(100, 100, 400, 300)

        # Create widgets
        self.name_label = QLabel('Nazwa zasobu:')
        self.type_label = QLabel('Typ zasobu:')
        self.description_label = QLabel('Opis zasobu:')
        self.date_label = QLabel('Data rezerwacji:')
        
        self.name_input = QLineEdit()
        self.type_input = QLineEdit()
        self.description_input = QLineEdit()
        self.date_input = QDateEdit(QDate.currentDate())
        self.date_input.setCalendarPopup(True)
        
        self.add_button = QPushButton('Dodaj zasób', self)
        self.add_button.clicked.connect(self.add_resource)
        
        self.list_button = QPushButton('Wyświetl zasoby', self)
        self.list_button.clicked.connect(self.display_resources)
        
        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.name_label)
        layout.addWidget(self.name_input)
        layout.addWidget(self.type_label)
        layout.addWidget(self.type_input)
        layout.addWidget(self.description_label)
        layout.addWidget(self.description_input)
        layout.addWidget(self.date_label)
        layout.addWidget(self.date_input)
        layout.addWidget(self.add_button)
        layout.addWidget(self.list_button)
        
        self.setLayout(layout)
        self.resource_manager = ITResource()

    def add_resource(self):
        name = self.name_input.text()
        type = self.type_input.text()
        description = self.description_input.text()
        reservation_date = self.date_input.date()
        if self.resource_manager.add_resource(name, type, description, reservation_date):
            QMessageBox.information(self, 'System Rezerwacji', f"Zasób '{name}' dodany pomyślnie.")
            # Clear inputs after adding
            self.name_input.clear()
            self.type_input.clear()
            self.description_input.clear()
        else:
            QMessageBox.warning(self, 'Błąd', f"Zasób '{name}' już istnieje.")

    def display_resources(self):
        resources_info = self.resource_manager.list_resources()
        QMessageBox.information(self, 'Lista Zasobów', resources_info)

def main():
    app = QApplication(sys.argv)
    ex = ITResourceGUI()
    ex.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
