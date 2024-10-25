import sys

from PyQt6.QtWidgets import QDialog, QApplication

from layout import Ui_Dialog

class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.button_clicked)
        self.show()

    def button_clicked(self):
        size = ""
        toppings = ""

        if self.ui.smallButton.isChecked():
            size = "mała"
        elif self.ui.mediumButton.isChecked():
            size = "średnia"
        elif self.ui.largeButton.isChecked():
            size = "duża"

        if self.ui.pieczarki.isChecked():
            toppings += "pieczarkami "
        if self.ui.kukurydza.isChecked():
            toppings += "kukurydzą "
        if self.ui.ananas.isChecked():
            toppings += "ananasem "
        if self.ui.szynka.isChecked():
            toppings += "szynką "
        else:
            toppings = "Nie wybrano dodatków"

        if size != '':
            self.ui.resultLabel.setText(f'Wybrałeś pizze: {size}, z: {toppings}')
        else:
            self.ui.resultLabel.setText("Nie wybrano dodatków")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyForm()
    sys.exit(app.exec())