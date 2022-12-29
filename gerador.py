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
        self.btn_gerar.clicked.connect(self.take_info)
        self.lbl_boa.setText('')

    def take_info(self):
        if (not self.radio_nao.isChecked()) and (not self.radio_sim.isChecked()):
            QMessageBox.information(self, 'Erro', 'Escolha a opção de repetição.')
            return
        elif self.radio_nao.isChecked():
            self.verify_numbers()

        elif self.radio_sim.isChecked():
            self.verify_numbers()

    def verify_numbers(self):
        if (self.qtd_num.text() == '') or (self.qtd_num.text() not in string.digits):
            QMessageBox.information(self, 'Erro', 'Digite a quantidade de números sorteados.')
            return
        else:
            if self.qtd_num.text() == '6' and self.radio_nao.isChecked():
                self.gerador_sena()
            elif 2 <= int(self.qtd_num.text()) <= 4:
                self.gerador_quadra()

    def verify_lucks(self, max):
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
            if not 1 <= int(sorte1) <= max:
                QMessageBox.information(self, "Erro", f"Coloque um numero entre 1 e {max}")
                return

        if sorte2 != '':
            for ind in range(len(sorte2)):
                if sorte2[ind] not in string.digits:
                    QMessageBox.information(self, "Erro", "Coloque um numero")
                    return
            if not 1 <= int(sorte2) <= max:
                QMessageBox.information(self, "Erro", f"Coloque um numero entre 1 e {max}")
                return

        if sorte3 != '':
            for ind in range(len(sorte3)):
                if sorte3[ind] not in string.digits:
                    QMessageBox.information(self, "Erro", "Coloque um numero")
                    return
            if not 1 <= int(sorte3) <= max:
                QMessageBox.information(self, "Erro", f"Coloque um numero entre 1 e {max}")
                return

        if len(sorte1) != 0 and 1 <= int(sorte1) <= max:
            self.numbers_list.append(int(self.sorte1.text()))
        if len(sorte2) != 0 and 1 <= int(sorte2) <= max:
            self.numbers_list.append(int(self.sorte2.text()))
        if len(sorte3) != 0 and 1 <= int(sorte3) <= max:
            self.numbers_list.append(int(self.sorte3.text()))

    def sort_end(self, arg='', ran=False):
        if ran:
            random.shuffle(self.numbers_list)
        for index in range(len(self.numbers_list)):
            if 1 <= self.numbers_list[index] <= 9:
                self.numbers_list[index] = '0' + str(self.numbers_list[index])
            if arg == 'pode':
                self.numbers_list[index] = int(self.numbers_list[index])
            self.balls[index].setText(str(self.numbers_list[index]))
        self.lbl_boa.setText('Boa sorte!!!')

    def gerador_quadra(self):
        if self.radio_nao.isChecked():
            self.verify_lucks(99)
            while len(self.numbers_list) < 2:
                num = random.randint(1, 99)
                if num not in self.numbers_list:
                    self.numbers_list.append(num)
            self.sort_end(ran=True)

        else:
            self.verify_lucks(9)
            while len(self.numbers_list) < 4:
                num = random.randint(1, 9)
                self.numbers_list.append(num)
            self.sort_end(arg='pode', ran=True)

    def gerador_sena(self):
        self.verify_lucks(60)

        self.numbers_list = set(self.numbers_list)
        self.numbers_list = list(self.numbers_list)

        while len(self.numbers_list) < 6:
            num = random.randint(1, 60)
            if num not in self.numbers_list:
                self.numbers_list.append(num)
        self.numbers_list.sort()
        self.sort_end()


app = QApplication([])
window = Loteria()
window.show()
app.exec_()