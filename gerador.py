from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from Design import Ui_Gerador

import random
import string

class Loteria(QMainWindow, Ui_Gerador):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.numbers_list = []
        self.balls = [self.num1, self.num2, self.num3, self.num4, self.num5, self.num6]
        self.btn_gerar.clicked.connect(self.gerador_sena)
        self.label.setText('')

    def gerador_sena(self):
        for index in range(6):
            self.balls[index].setText('')
            self.numbers_list = []
        sorte1 = self.sorte1.text()
        sorte2 = self.sorte2.text()
        sorte3 = self.sorte3.text()

        if sorte1 != '':
            for ind in range(len(sorte1)):
                if sorte1[ind] not in string.digits:
                    QMessageBox.information(self, "Erro", "Coloque um numero")
                    return
            if not 1 <= int(sorte1) <= 60:
                QMessageBox.information(self, "Erro", "Coloque um numero entre 1 e 60")
                return

        if sorte2 != '':
            for ind in range(len(sorte2)):
                if sorte2[ind] not in string.digits:
                    QMessageBox.information(self, "Erro", "Coloque um numero")
                    return
            if not 1 <= int(sorte2) <= 60:
                QMessageBox.information(self, "Erro", "Coloque um numero entre 1 e 60")
                return

        if sorte3 != '':
            for ind in range(len(sorte3)):
                if sorte3[ind] not in string.digits:
                    QMessageBox.information(self, "Erro", "Coloque um numero")
                    return
            if not 1 <= int(sorte3) <= 60:
                QMessageBox.information(self, "Erro", "Coloque um numero entre 1 e 60")
                return

        if len(sorte1) != 0 and 1 <= int(sorte1) <= 60:
            self.numbers_list.append(int(self.sorte1.text()))
        if len(sorte2) != 0 and 1 <= int(sorte2) <= 60:
            self.numbers_list.append(int(self.sorte2.text()))
        if len(sorte3) != 0 and 1 <= int(sorte3) <= 60:
            self.numbers_list.append(int(self.sorte3.text()))

        self.numbers_list = set(self.numbers_list)
        self.numbers_list = list(self.numbers_list)

        while len(self.numbers_list) < 6:
            num = random.randint(1, 60)
            if num not in self.numbers_list:
                self.numbers_list.append(num)

        self.numbers_list.sort()

        for index in range(len(self.numbers_list)):
            self.balls[index].setText(str(self.numbers_list[index]))
        self.label.setText('Boa sorte!!!')


app = QApplication([])
window = Loteria()
window.show()
app.exec_()
