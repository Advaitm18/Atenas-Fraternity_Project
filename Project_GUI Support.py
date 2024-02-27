
import sys
from PyQt6.QtWidgets import QApplication, QFormLayout, QLineEdit, QLabel, QWidget, QPushButton, QCheckBox, QRadioButton, QComboBox, QMessageBox
from PyQt6.QtGui import QPixmap

class FraternityApp(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("ATENAS FRATERNITY")
        self.setGeometry(100, 100, 800, 600)

        self.label = QLabel(self)
        self.label.setPixmap(QPixmap("cover.png"))
        self.label.adjustSize()
        self.label.move(0, 160)
     
        self.layout = QFormLayout()
        self.add_form_fields()
        self.add_buttons()
        self.setLayout(self.layout)

    def add_form_fields(self):
        self.fields = {
            "Name: ": QLineEdit(),
            "Phone Number: ": QLineEdit(),
            "Email-ID: ": QLineEdit(),
            "Address: ": QLineEdit()
        }
        for field, input_field in self.fields.items():
            self.layout.addRow(field, input_field)

        self.layout.addRow("Education Institution: ", QLineEdit())
        self.cb_platform = QComboBox()
        self.cb_platform.addItems(["Secondary / High School Education", "Bachelor's Degrees", "Master's Degrees"])
        self.layout.addRow("Education qualification", self.cb_platform)

        checkbox_texts = [
            'Aviation Cabin-Crew & Ground-Staff',
            'Data Science & Analytics with Artificial Intelligence (AI), Machine Learning (ML)',
            'Full-Stack Web & Mobile Development',
            'Digital Marketing'
        ]
        for text in checkbox_texts:
            self.layout.addWidget(QCheckBox(text, self))

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
        QMessageBox.information(
            self,
            'ATENAS FRATERNITY',
            'Thank you, Data Stored Successfully!'
        )

    def reset_action(self):
        answer = QMessageBox.question(
            self,
            'Confirmation',
            'Do you want to Reset? ',
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )
        if answer == QMessageBox.StandardButton.Yes:
            QMessageBox.information(
                self,
                'Information',
                "You selected 'Yes', Form will be reset! ",
                QMessageBox.StandardButton.Ok
            )
            # Clear form fields
            for field in self.fields.values():
                field.clear()
        else:
            QMessageBox.information(
                self,
                'Information',
                "You selected 'No'.",
                QMessageBox.StandardButton.Ok
            )

if __name__ == "__main__":
    app = QApplication([])
    window = FraternityApp()
    window.show()
    sys.exit(app.exec())
