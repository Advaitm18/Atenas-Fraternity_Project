import sys
from PyQt6.QtWidgets import QApplication, QFormLayout, QLineEdit, QLabel, QWidget, QPushButton, QCheckBox, QRadioButton, QComboBox
from PyQt6.QtGui import QPixmap

class FraternityApp(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("ATENAS FRATERNITY")
        self.setGeometry(100, 100, 800, 600)

        self.layout = QFormLayout()
        self.add_form_fields()
        self.ComboBox()
        self.CheckBox()
        self.RadioButton()
        self.add_buttons()
        self.setLayout(self.layout)
        
    def add_form_fields(self):
        fields = {
            "Name: ": QLineEdit(),
            "Phone Number: ": QLineEdit(),
            "Email-ID: ": QLineEdit(),
            "Institution Name: ": QLineEdit(),
            "Education qualification": QComboBox()
        }
    def ComboBox(self):
        self.cb_platform = QComboBox()
        self.cb_platform.addItems(["Secondary / High School Education", "Bachelor's Degrees", "Master's Degrees"])
        self.layout.addRow("Education qualification", self.cb_platform)

        for field, input_field in fields.items():
            if field != "Education qualification":
                self.layout.addRow(field, input_field)
                
    def CheckBox(self):
        checkbox_texts = [
            'Aviation Cabin-Crew & Ground-Staff',
            'Data Science & Analytics with Artificial Intelligence (AI), Machine Learning (ML)',
            'Full-Stack Web & Mobile Development',
            'Digital Marketing'
        ]
        for text in checkbox_texts:
            self.layout.addWidget(QCheckBox(text, self))
            
    def RadioButton(self):
        radiobutton_texts = ['Yes', 'No']
        for text in radiobutton_texts:
            self.layout.addWidget(QRadioButton(text, self))
        

    def add_buttons(self):
        submit_button = QPushButton('Submit')
        submit_button.clicked.connect(self.submit_action)

        reset_button = QPushButton('Reset')
        reset_button.clicked.connect(self.reset_action)

        exit_button = QPushButton('Exit')
        exit_button.clicked.connect(self.close)

        self.layout.addWidget(submit_button)
        self.layout.addWidget(reset_button)
        self.layout.addWidget(exit_button)

    def submit_action(self):
        print("Submit button clicked")

    def reset_action(self):
        print("Reset button clicked")

app = QApplication([])
window = FraternityApp()
window.show()
sys.exit(app.exec())

