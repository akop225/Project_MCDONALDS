import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QGridLayout, QWidget, QTableWidget, QTableWidgetItem
from PyQt5.QtCore import QSize, Qt

from PyQt5 import uic
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QMessageBox, QFormLayout, QGroupBox, \
    QVBoxLayout, QScrollArea, QMainWindow, QSpinBox, QTableWidget, QGridLayout, QTableWidget

import sqlite3

from PyQt5.uic.properties import QtWidgets, QtCore, QtGui


file_name = "макдоналдс.db"

con = sqlite3.connect(file_name)

cur = con.cursor()

result = cur.execute('''SELECT login, password, full_name FROM Users''').fetchall()

users = {}
for elem in result:
    users[elem[0]] = (elem[1], elem[2].lower())
print(users)

answers = {}
result2 = cur.execute('''SELECT login, answers FROM Users''').fetchall()

for el in result2:
    answers[el[0]] = [w.lower() for w in el[1].split(", ")]

count = 0
orders = {}


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Зададим размер и положение нашего виджета,
        self.setGeometry(0, 0, 1920, 1000)
        # А также его заголовок
        self.setWindowTitle("Mcdonald's")

        self.pixmap = QPixmap('mcdonalds.jpg')

        self.image = QLabel(self)
        self.image.move(350, 60)
        self.image.resize(1200, 880)
        self.image.setPixmap(self.pixmap)


        self.title = QLabel(" Mcdonald's", self)
        self.title.setFixedSize(400, 100)
        self.title.setGeometry(750, 250, 1100, 350)
        self.title.setMinimumHeight(72)
        self.title.setStyleSheet("color: black; font-size: 72px;")

        self.login = QLabel("Login", self)
        self.login.setGeometry(770, 400, 130, 30)
        self.login.setStyleSheet("font-size: 22px; color: black;")

        self.logint = QLineEdit(self)
        self.logint.setGeometry(920, 400, 200, 30)
        self.logint.setStyleSheet("color: black; font-size: 22px;")

        self.password = QLabel('Password', self)
        self.password.setGeometry(770, 450, 130, 30)
        self.password.setStyleSheet("font-size: 22px; color: black;")

        self.passwordt = QLineEdit(self)
        self.passwordt.setEchoMode(QLineEdit.Password)
        self.passwordt.setGeometry(920, 450, 200, 30)
        self.passwordt.setStyleSheet("color: black; font-size: 22px;")

        self.open = QPushButton('Log in', self)
        self.open.setGeometry(770, 550, 90, 40)
        self.open.setStyleSheet("font-size: 22px; color: black;")

        self.forget = QPushButton('Forgot your password?', self)
        self.forget.setGeometry(870, 550, 250, 40)
        self.forget.setStyleSheet("font-size: 22px; color: black;")

        self.reg = QPushButton('Register', self)
        self.reg.setGeometry(860, 600, 170, 40)
        self.reg.setStyleSheet('font-size: 22px; color: black;')

        self.open.clicked.connect(self.open_menu)

        self.forget.clicked.connect(self.open_pass)

        self.reg.clicked.connect(self.reger)



    def open_pass(self):
        self.real_login = self.logint.text()
        self.recovery = PasswordRecovery(self, self.real_login)
        self.recovery.show()


    def open_menu(self):
        self.real_login = self.logint.text()
        password = self.passwordt.text()
        if self.real_login in users:
            if password == users[self.real_login][0]:
                self.close()
                self.second_form = Menu(self, "Данные для второй формы")
                self.second_form.show()
            else:
                QMessageBox.critical(self, "Ошибка ", "Неверный пароль", QMessageBox.Ok)
        else:
            QMessageBox.critical(self, "Ошибка ", "Такого пользователя не существует", QMessageBox.Ok)

    def reger(self):
        self.reg = Registration(self)
        self.reg.show()
        self.close()


class Registration(QMainWindow):
    def __init__(self, *args):
        super().__init__()
        self.initUI(args)

    def initUI(self, args):
        self.setGeometry(490, 60, 1025, 940)
        self.setWindowTitle('Регистрация')
        self.setStyleSheet("background-color: white")

        self.pixmap = QPixmap('reg.jpg')

        self.image = QLabel(self)
        self.image.move(0, 0)
        self.image.resize(1023, 940)
        self.image.setPixmap(self.pixmap)

        self.pixmap2 = QPixmap('res3.bmp')

        self.image2 = QLabel(self)
        self.image2.move(10, 10)
        self.image2.resize(100, 100)
        self.image2.setPixmap(self.pixmap2)


        self.username = QLabel('ФИО:', self)
        self.username.move(277, 340)
        font = self.username.font()
        font.setBold(True)
        self.username.setFont(font)
        self.username.setStyleSheet("font-size: 22px; color: black;")
        self.username.adjustSize()


        self.full_name = QLineEdit(self)
        self.full_name.setGeometry(378, 340, 370, 30)
        self.full_name.setStyleSheet("font-size: 22px; color: black;")


        self.logint = QLabel('Логин:', self)
        self.logint.setGeometry(277, 390, 250, 30)
        font = self.logint.font()
        font.setBold(True)
        self.logint.setFont(font)
        self.logint.setStyleSheet("font-size: 22px; color: black;")
        self.logint.adjustSize()


        self.login = QLineEdit(self)
        self.login.setGeometry(528, 390, 220, 30)
        self.login.setStyleSheet("color: black; font-size: 22px;")

        self.passwordt = QLabel('Пароль:', self)
        self.passwordt.setGeometry(277, 440, 250, 50)
        font = self.passwordt.font()
        font.setBold(True)
        self.passwordt.setFont(font)
        self.passwordt.setStyleSheet("font-size: 22px; color: black;")
        self.passwordt.adjustSize()


        self.password = QLineEdit(self)
        self.password.setEchoMode(QLineEdit.Password)
        self.password.setGeometry(528, 440, 220, 35)
        self.password.setStyleSheet("font-size: 22px; color: black;")


        self.question1 = QLabel('Имя вашей матери:', self)
        self.question1.setGeometry(277, 500, 250, 30)
        font = self.question1.font()
        font.setBold(True)
        self.question1.setFont(font)
        self.question1.setStyleSheet("font-size: 22px; color: black;")
        self.question1.adjustSize()


        self.answer1 = QLineEdit(self)
        self.answer1.setGeometry(528, 500, 220, 30)
        self.answer1.setStyleSheet("color: black; font-size: 22px;")

        self.question2 = QLabel('''Название вашей\nлюбимой страны:''', self)
        self.question2.setGeometry(277, 550, 250, 50)
        font = self.question2.font()
        font.setBold(True)
        self.question2.setFont(font)
        self.question2.setStyleSheet("font-size: 22px; color: black")
        self.question2.adjustSize()


        self.answer2 = QLineEdit(self)
        self.answer2.setGeometry(528, 555, 220, 35)
        font = self.answer2.font()
        self.answer2.setStyleSheet("font-size: 22px; color: black")

        self.ok = QPushButton('Зарегистрироваться', self)
        self.ok.setGeometry(528, 610, 220, 35)
        self.ok.setStyleSheet("font-size: 22px; color: black;")


        self.ok.clicked.connect(self.checking)

    def checking(self):
        fullname = self.full_name.text()
        mother_name = self.answer1.text()
        land = self.answer2.text()
        login = self.login.text()
        password = self.password.text()
        if fullname and mother_name and land and login and password:
            if login not in users:
                if len(password) >= 8:
                    file_name = "макдоналдс.db"
                    con = sqlite3.connect(file_name)
                    cur = con.cursor()
                    result = cur.execute('''INSERT INTO Users(login, password, full_name, answers) values(?, ?, ?, ?)''',
                                         (login, password, fullname, f"{mother_name}, {land}"))
                    con.commit()
                    con.close()
                    self.close()
                    self.menu_window = Menu(self)
                    self.menu_window.show()
                else:
                    QMessageBox.critical(self, "Короткий пароль ", "Пароль должен содержать не менее 8 символов!", QMessageBox.Ok)
            else:
                QMessageBox.critical(self, "Ошибка ", "Такой логин уже занят", QMessageBox.Ok)
        else:
            QMessageBox.critical(self, "Ошибка ", "Запомните все поля!", QMessageBox.Ok)


#  Категории еды, меню
class Menu(QMainWindow):
    def __init__(self, *args):
        super().__init__()
        self.initUI(args)

    def initUI(self, args):
        self.setGeometry(0, 0, 1920, 1000)
        self.setWindowTitle('Меню')
        self.setStyleSheet("background-color: white")

        self.pixmap = QPixmap('back_menu.bmp')

        self.image = QLabel(self)
        self.image.move(0, 0)
        self.image.resize(1920, 1000)
        self.image.setPixmap(self.pixmap)


        self.line3 = QLabel(self)
        self.line3.setGeometry(0, 10, 1920, 100)
        self.line3.setStyleSheet("background-color: #D90009")

        self.pixmap2 = QPixmap('logo_menu.bmp')

        self.image2 = QLabel(self)
        self.image2.move(910, 10)
        self.image2.resize(100, 100)
        self.image2.setPixmap(self.pixmap2)

        self.order = QPixmap('корзина.bmp')

        self.imageord = QLabel(self)
        self.imageord.move(1700, 870)
        self.imageord.resize(200, 100)
        self.imageord.setPixmap(self.order)

        # Корзина

        self.btnorder = QPushButton('Ваш заказ:', self)
        self.btnorder.setGeometry(1700, 820, 200, 30)
        self.btnorder.setStyleSheet('font-size: 22px; color: black; background-color: white;')

        # Категория "Бургеры"

        self.btnburger = QPushButton(self)
        self.btnburger.setGeometry(112, 230, 340, 270)
        self.btnburger.setStyleSheet('font-size: 22px; color: black;')
        self.btnburger.setStyleSheet('background-image: url(бигтейсти.bmp)')

        self.btnburger2 = QPushButton('Бургеры', self)
        self.btnburger2.setGeometry(112, 460, 340, 40)
        self.btnburger2.setStyleSheet('font-size: 22px; color: black;')

        self.btnburger.clicked.connect(self.burgers)
        self.btnburger2.clicked.connect(self.burgers)

        # Категория "Картофель и стартеры"

        self.btnpotatoe = QPushButton(self)
        self.btnpotatoe.setGeometry(564, 230, 340, 270)
        self.btnpotatoe.setStyleSheet('background-image: url(фри.bmp)')

        self.btnpotatoe2 = QPushButton('Картофель и стартеры', self)
        self.btnpotatoe2.setGeometry(564, 460, 340, 40)
        self.btnpotatoe2.setStyleSheet('font-size: 22px; color: black;')

        self.btnpotatoe.clicked.connect(self.starters)
        self.btnpotatoe2.clicked.connect(self.starters)

        # Категория "Напитки"

        self.drink = QPushButton(self)
        self.drink.setGeometry(1016, 230, 340, 270)
        self.drink.setStyleSheet('background-image: url(напитки.bmp)')

        self.btndrink2 = QPushButton('Напитки', self)
        self.btndrink2.setGeometry(1016, 460, 340, 40)
        self.btndrink2.setStyleSheet('font-size: 22px; color: black;')

        self.btndrink2.clicked.connect(self.drinks)
        self.drink.clicked.connect(self.drinks)

        # Категория "Роллы"

        self.roll = QPushButton(self)
        self.roll.setGeometry(1468, 230, 340, 270)
        self.roll.setStyleSheet('background-image: url(бигтейстиролл.bmp)')

        self.btnroll = QPushButton('Роллы', self)
        self.btnroll.setGeometry(1468, 460, 340, 40)
        self.btnroll.setStyleSheet('font-size: 22px; color: black;')

        self.roll.clicked.connect(self.rolls)
        self.btnroll.clicked.connect(self.rolls)

        # Приветствие

        self.welcome = QLabel('Добро пожаловать', self)
        self.welcome.setGeometry(730, 700, 440, 70)
        self.welcome.setStyleSheet('font-size: 50px; color: black;')

        # Категория "Десерты и выпечка"

        self.btndessert = QPushButton(self)
        self.btndessert.setGeometry(338, 615, 340, 270)
        self.btndessert.setStyleSheet('background-image: url(десерты.bmp)')

        self.btndessert2 = QPushButton('Десерты и выпечка', self)
        self.btndessert2.setGeometry(338, 845, 340, 40)
        self.btndessert2.setStyleSheet('font-size: 22px; color: black;')

        self.btndessert.clicked.connect(self.dessert)
        self.btndessert2.clicked.connect(self.dessert)

        # Категория "Соусы"

        self.btnsauces = QPushButton(self)
        self.btnsauces.setGeometry(1242, 615, 340, 270)
        self.btnsauces.setStyleSheet('background-image: url(соусы.bmp)')

        self.btnsauces2 = QPushButton('Соусы', self)
        self.btnsauces2.setGeometry(1242, 845, 340, 40)
        self.btnsauces2.setStyleSheet('font-size: 22px; color: black;')

        self.btnsauces.clicked.connect(self.sauces)
        self.btnsauces2.clicked.connect(self.sauces)

        self.btnorder.clicked.connect(self.packer)

    def packer(self):
        self.my_packet = Packet(self)
        self.my_packet.show()


    def burgers(self):
        self.my_burgers = Burgers(self, 'SMTH')
        self.my_burgers.show()

    def drinks(self):
        self.my_drinks = Drinks(self, 'SMTH')
        self.my_drinks.show()

    def starters(self):
        self.my_starters = Starters(self, 'SMTH')
        self.my_starters.show()

    def sauces(self):
        self.my_sauces = Sauces(self, 'SMTH')
        self.my_sauces.show()

    def rolls(self):
        self.my_rolls = Rolls(self, 'SMTH')
        self.my_rolls.show()

    def dessert(self):
        self.my_dessert = Desserts(self, 'SMTH')
        self.my_dessert.show()


class Sauces(QMainWindow):
    def __init__(self, *args):
        super().__init__()
        self.setUp(args)

    def setUp(self, args):
        self.setGeometry(0, 0, 1461, 939)

        self.pixmap = QPixmap('backburg.bmp')

        self.image = QLabel(self)
        self.image.move(0, 0)
        self.image.resize(1461, 939)
        self.image.setPixmap(self.pixmap)

        self.back = QPushButton('Назад', self)
        self.back.setGeometry(1361, 35, 70, 30)
        self.back.setStyleSheet('background-color: black; color: white; font-size: 16px;')
        self.back.clicked.connect(self.backer)

        self.pushButton = QPushButton('\n\n\n\n\n\n\n\n\n\n\n\n\nСоус Сырный', self)
        self.pushButton.setGeometry(370, 70, 200, 181)
        self.pushButton.setStyleSheet("background-image: url(сырный.bmp); font-size: 25px")
        self.label = QLabel('Соус Сырный', self)
        font = self.label.font()
        font.setBold(True)
        self.label.setFont(font)
        self.label.setGeometry(400, 270, 200, 20)
        self.label.setStyleSheet('color: white; font-size: 16px')
        self.pushButton.clicked.connect(self.redactor)

        self.pushButton_2 = QPushButton('\n\n\n\n\n\n\n\n\n\n\n\n\nСоус Кисло-Сладкий', self)
        self.pushButton_2.setGeometry(640, 70, 200, 181)
        self.pushButton_2.setStyleSheet("background-image: url(кисло-сладкий.bmp); font-size: 16px")
        self.label2 = QLabel('Соус Кисло-Сладкий', self)
        font = self.label2.font()
        font.setBold(True)
        self.label2.setFont(font)
        self.label2.setGeometry(660, 270, 250, 20)
        self.label2.setStyleSheet('color: white; font-size: 16px')
        self.pushButton_2.clicked.connect(self.redactor)

        self.pushButton_3 = QPushButton('\n\n\n\n\n\n\n\n\n\n\n\n\nСоус 1000 Островов', self)
        self.pushButton_3.setGeometry(910, 70, 200, 181)
        self.pushButton_3.setStyleSheet("background-image: url(тысяча.bmp); font-size: 16px")
        self.label3 = QLabel('Соус 1000 Островов', self)
        font = self.label3.font()
        font.setBold(True)
        self.label3.setFont(font)
        self.label3.setGeometry(915, 270, 250, 20)
        self.label3.setStyleSheet('color: white; font-size: 16px')
        self.pushButton_3.clicked.connect(self.redactor)

        self.pushButton_4 = QPushButton('\n\n\n\n\n\n\n\n\n\n\n\n\nКетчуп', self)
        self.pushButton_4.setGeometry(370, 331, 200, 181)
        self.pushButton_4.setStyleSheet("background-image: url(кетчуп.bmp); font-size: 16px")
        self.label4 = QLabel('Кетчуп', self)
        font = self.label4.font()
        font.setBold(True)
        self.label4.setFont(font)
        self.label4.setGeometry(430, 531, 250, 20)
        self.label4.setStyleSheet('color: white; font-size: 16px')
        self.pushButton_4.clicked.connect(self.redactor)

        self.pushButton_5 = QPushButton("\n\n\n\n\n\n\n\n\n\n\n\n\nСоус Сладкий Чили", self)
        self.pushButton_5.setGeometry(640, 331, 200, 181)
        self.pushButton_5.setStyleSheet("background-image: url(чили.bmp); font-size: 16px")
        self.label5 = QLabel('Соус Сладкий Чили', self)
        font = self.label5.font()
        font.setBold(True)
        self.label5.setFont(font)
        self.label5.setGeometry(660, 531, 200, 20)
        self.label5.setStyleSheet('color: white; font-size: 16px')
        self.pushButton_5.clicked.connect(self.redactor)

        self.pushButton_6 = QPushButton("\n\n\n\n\n\n\n\n\n\n\n\n\nСоус Барбекю", self)
        self.pushButton_6.setGeometry(910, 331, 200, 181)
        self.pushButton_6.setStyleSheet("background-image: url(барбекю.bmp); font-size: 16px")
        self.label6 = QLabel("Соус Барбекю", self)
        font = self.label6.font()
        font.setBold(True)
        self.label6.setFont(font)
        self.label6.setGeometry(940, 531, 200, 20)
        self.label6.setStyleSheet('color: white; font-size: 16px')
        self.pushButton_6.clicked.connect(self.redactor)

        self.pushButton_7 = QPushButton("\n\n\n\n\n\n\n\n\n\n\n\n\nСоус Горчичный", self)
        self.pushButton_7.setGeometry(370, 592, 200, 181)
        self.pushButton_7.setStyleSheet("background-image: url(горчичный.bmp);")
        self.label7 = QLabel("Соус Горчичный", self)
        font = self.label7.font()
        font.setBold(True)
        self.label7.setFont(font)
        self.label7.setGeometry(395, 792, 200, 20)
        self.label7.setStyleSheet('color: white; font-size: 16px')
        self.pushButton_7.clicked.connect(self.redactor)

        self.pushButton_8 = QPushButton("\n\n\n\n\n\n\n\n\n\n\n\n\nСоус Терияки", self)
        self.pushButton_8.setGeometry(640, 592, 200, 181)
        self.pushButton_8.setStyleSheet("background-image: url(терияки.bmp)")
        self.label8 = QLabel("Соус Терияки", self)
        font = self.label8.font()
        font.setBold(True)
        self.label8.setFont(font)
        self.label8.setGeometry(675, 792, 250, 20)
        self.label8.setStyleSheet('color: white; font-size: 16px')
        self.pushButton_8.clicked.connect(self.redactor)

        self.pushButton_9 = QPushButton("\n\n\n\n\n\n\n\n\n\n\n\n\nСоус Чесночный", self)
        self.pushButton_9.setGeometry(910, 592, 200, 181)
        self.pushButton_9.setStyleSheet("background-image: url(чеснок.bmp);")
        self.label9 = QLabel("Соус Чесночный", self)
        font = self.label9.font()
        font.setBold(True)
        self.label9.setFont(font)
        self.label9.setGeometry(935, 792, 200, 20)
        self.label9.setStyleSheet('color: white; font-size: 16px')
        self.pushButton_9.clicked.connect(self.redactor)

        self.packet = QPushButton('Ваша корзина:\n\n\n\n', self)
        self.packet.setGeometry(1180, 820, 200, 111)
        self.packet.setStyleSheet("background-image: url(корзина.bmp); font-size: 14px")

        self.packet.clicked.connect(self.packer)

    def packer(self):
        self.my_packet = Packet(self)
        self.my_packet.show()

    def backer(self):
        self.close()

    def redactor(self):
        sauce = self.sender().text().strip()
        self.widget = Count(self, sauce)
        self.widget.show()


class Count(QMainWindow):
    def __init__(self, *args):
        super().__init__()
        self.setUp(args)

    def setUp(self, args):
        self.name = args[-1]
        self.setGeometry(650, 400, 161, 100)
        self.setStyleSheet('background-color: black')

        self.count = QSpinBox(self)
        self.count.setValue(1)
        self.count.setGeometry(20, 10, 120, 50)
        self.count.setStyleSheet("color: white")

        self.btnok = QPushButton('OK', self)
        self.btnok.setGeometry(111, 69, 30, 30)
        self.btnok.setStyleSheet('font-size: 16px; color: white;')

        self.btnok.clicked.connect(self.save)

    def save(self):
        n = int(self.count.text())
        file_name = "макдоналдс.db"
        con = sqlite3.connect(file_name)
        cur = con.cursor()
        result = cur.execute(f'''SELECT price FROM Dishes WHERE dish LIKE ?''', (self.name,)).fetchall()
        orders[self.name] = (result[0][0], n, int(result[0][0]) * n)
        self.close()


# Класс Десерты и выпечка
class Desserts(QMainWindow):
    def __init__(self, *args):
        super().__init__()
        self.setUp(args)

    def setUp(self, args):
        self.setGeometry(0, 0, 1461, 939)

        self.pixmap = QPixmap('backburg.bmp')

        self.image = QLabel(self)
        self.image.move(0, 0)
        self.image.resize(1461, 939)
        self.image.setPixmap(self.pixmap)

        self.back = QPushButton('Назад', self)
        self.back.setGeometry(1361, 35, 70, 30)
        self.back.setStyleSheet('background-color: black; color: white; font-size: 16px;')
        self.back.clicked.connect(self.backer)

        self.pushButton = QPushButton("\n\n\n\n\n\n\n\n\n\n\n\nМакфлурри Тирамису", self)
        self.pushButton.setGeometry(100, 70, 200, 181)
        self.pushButton.setStyleSheet("background-image: url(терамису.bmp); font-size: 16px")
        self.label = QLabel('Макфлурри Тирамису', self)
        font = self.label.font()
        font.setBold(True)
        self.label.setFont(font)
        self.label.setGeometry(115, 270, 200, 20)
        self.label.setStyleSheet('color: white; font-size: 16px')
        self.pushButton.clicked.connect(self.redactor)

        self.pushButton_2 = QPushButton("\n\n\n\n\n\n\n\n\n\n\n\nМакфлурри Де Люкс Клуб-Шок", self)
        self.pushButton_2.setGeometry(370, 70, 200, 181)
        self.pushButton_2.setStyleSheet("background-image: url(шокклуб.bmp); font-size: 16px")
        self.label2 = QLabel('Макфлурри Де Люкс\n        Клуб-Шок', self)
        font = self.label2.font()
        font.setBold(True)
        self.label2.setFont(font)
        self.label2.setGeometry(380, 270, 200, 40)
        self.label2.setStyleSheet('color: white; font-size: 16px')
        self.pushButton_2.clicked.connect(self.redactor)


        self.pushButton_3 = QPushButton("\n\n\n\n\n\n\n\n\n\n\n\nМакфлурри Де Люкс Карам-Шок", self)
        self.pushButton_3.setGeometry(640, 70, 200, 181)
        self.pushButton_3.setStyleSheet("background-image: url(шоккар.bmp); font-size: 16px")
        self.label3 = QLabel('Макфлурри Де Люкс\n       Карам-Шок', self)
        font = self.label3.font()
        font.setBold(True)
        self.label3.setFont(font)
        self.label3.setGeometry(650, 270, 200, 40)
        self.label3.setStyleSheet('color: white; font-size: 16px')
        self.pushButton_3.clicked.connect(self.redactor)

        self.pushButton_4 = QPushButton("\n\n\n\n\n\n\n\n\n\n\n\nМороженное Манго-Маракуйя", self)
        self.pushButton_4.setGeometry(910, 70, 200, 181)
        self.pushButton_4.setStyleSheet("background-image: url(санмаракуйя.bmp); font-size: 16px")
        self.label4 = QLabel('Мороженное Манго-Маракуйя', self)
        font = self.label4.font()
        font.setBold(True)
        self.label4.setFont(font)
        self.label4.setGeometry(890, 270, 250, 20)
        self.label4.setStyleSheet('color: white; font-size: 16px')
        self.pushButton_4.clicked.connect(self.redactor)

        self.pushButton_5 = QPushButton("\n\n\n\n\n\n\n\n\n\n\n\nМороженное Карамельное", self)
        self.pushButton_5.setGeometry(1180, 70, 200, 181)
        self.pushButton_5.setStyleSheet("background-image: url(санкарамель.bmp); font-size: 16px")
        self.label5 = QLabel('Мороженное Карамельное', self)
        font = self.label5.font()
        font.setBold(True)
        self.label5.setFont(font)
        self.label5.setGeometry(1180, 270, 250, 20)
        self.label5.setStyleSheet('color: white; font-size: 16px')
        self.pushButton_5.clicked.connect(self.redactor)

        self.pushButton_6 = QPushButton("\n\n\n\n\n\n\n\n\n\n\n\nМороженное Шоколадное", self)
        self.pushButton_6.setGeometry(100, 331, 200, 181)
        self.pushButton_6.setStyleSheet("background-image: url(саншоколад.bmp); font-size: 16px")
        self.label6 = QLabel('Мороженное Шоколадное', self)
        font = self.label6.font()
        font.setBold(True)
        self.label6.setFont(font)
        self.label6.setGeometry(90, 531, 250, 20)
        self.label6.setStyleSheet('color: white; font-size: 16px')
        self.pushButton_6.clicked.connect(self.redactor)

        self.pushButton_7 = QPushButton("\n\n\n\n\n\n\n\n\n\n\n\nМороженное Клубничное", self)
        self.pushButton_7.setGeometry(370, 331, 200, 181)
        self.pushButton_7.setStyleSheet("background-image: url(санклубника.bmp); font-size: 16px")
        self.label7 = QLabel('Мороженное Клубничное', self)
        font = self.label7.font()
        font.setBold(True)
        self.label7.setFont(font)
        self.label7.setGeometry(360, 531, 250, 20)
        self.label7.setStyleSheet('color: white; font-size: 16px')
        self.pushButton_7.clicked.connect(self.redactor)

        self.pushButton_8 = QPushButton("\n\n\n\n\n\n\n\n\n\n\n\nШоколадный Донат", self)
        self.pushButton_8.setGeometry(640, 331, 200, 181)
        self.pushButton_8.setStyleSheet("background-image: url(шокдонат.bmp); font-size: 16px")
        self.label8 = QLabel('Шоколадный Донат', self)
        font = self.label8.font()
        font.setBold(True)
        self.label8.setFont(font)
        self.label8.setGeometry(660, 531, 200, 20)
        self.label8.setStyleSheet('color: white; font-size: 16px')
        self.pushButton_8.clicked.connect(self.redactor)

        self.pushButton_9 = QPushButton("\n\n\n\n\n\n\n\n\n\n\n\nВанильный Донат", self)
        self.pushButton_9.setGeometry(910, 331, 200, 181)
        self.pushButton_9.setStyleSheet("background-image: url(вандонат.bmp); font-size: 16px")
        self.label9 = QLabel("Ванильный Донат", self)
        font = self.label9.font()
        font.setBold(True)
        self.label9.setFont(font)
        self.label9.setGeometry(935, 531, 200, 20)
        self.label9.setStyleSheet('color: white; font-size: 16px')
        self.pushButton_9.clicked.connect(self.redactor)

        self.pushButton_10 = QPushButton("\n\n\n\n\n\n\n\n\n\n\n\nЧизкейк по-американски", self)
        self.pushButton_10.setGeometry(1180, 331, 200, 181)
        self.pushButton_10.setStyleSheet("background-image: url(ньюйорк.bmp); font-size: 16px")
        self.label10 = QLabel("Чизкейк по-американски", self)
        font = self.label10.font()
        font.setBold(True)
        self.label10.setFont(font)
        self.label10.setGeometry(1180, 531, 250, 20)
        self.label10.setStyleSheet('color: white; font-size: 16px')
        self.pushButton_10.clicked.connect(self.redactor)

        self.pushButton_11 = QPushButton("\n\n\n\n\n\n\n\n\n\n\n\nШоколадный мусс", self)
        self.pushButton_11.setGeometry(100, 592, 200, 181)
        self.pushButton_11.setStyleSheet("background-image: url(мусс.bmp)")
        self.label11 = QLabel("Шоколадный мусс", self)
        font = self.label11.font()
        font.setBold(True)
        self.label11.setFont(font)
        self.label11.setGeometry(115, 792, 200, 20)
        self.label11.setStyleSheet('color: white; font-size: 16px')
        self.pushButton_11.clicked.connect(self.redactor)

        self.pushButton_12 = QPushButton("\n\n\n\n\n\n\n\n\n\n\n\nВафельный Рожок", self)
        self.pushButton_12.setGeometry(370, 592, 200, 181)
        self.pushButton_12.setStyleSheet("background-image: url(рожок.bmp);")
        self.label12 = QLabel("Вафельный Рожок", self)
        font = self.label12.font()
        font.setBold(True)
        self.label12.setFont(font)
        self.label12.setGeometry(390, 792, 200, 20)
        self.label12.setStyleSheet('color: white; font-size: 16px')
        self.pushButton_12.clicked.connect(self.redactor)

        self.pushButton_13 = QPushButton("\n\n\n\n\n\n\n\n\n\n\n\nПирожок Лесные ягоды Крем-чиз", self)
        self.pushButton_13.setGeometry(640, 592, 200, 181)
        self.pushButton_13.setStyleSheet("background-image: url(кремчиз.bmp)")
        self.label13 = QLabel("Пирожок Лесные ягоды\n     Крем-чиз", self)
        font = self.label13.font()
        font.setBold(True)
        self.label13.setFont(font)
        self.label13.setGeometry(640, 792, 250, 40)
        self.label13.setStyleSheet('color: white; font-size: 16px')
        self.pushButton_13.clicked.connect(self.redactor)

        self.pushButton_14 = QPushButton('\n\n\n\n\n\n\n\n\n\n\n\nПирожок Вишнёвый', self)
        self.pushButton_14.setGeometry(910, 592, 200, 181)
        self.pushButton_14.setStyleSheet("background-image: url(вишня.bmp);")
        self.label14 = QLabel("Пирожок Вишнёвый", self)
        font = self.label14.font()
        font.setBold(True)
        self.label14.setFont(font)
        self.label14.setGeometry(920, 792, 200, 20)
        self.label14.setStyleSheet('color: white; font-size: 16px')
        self.pushButton_14.clicked.connect(self.redactor)

        self.pushButton_16 = QPushButton('Ваша корзина:\n\n\n\n', self)
        self.pushButton_16.setGeometry(1180, 820, 200, 111)
        self.pushButton_16.setStyleSheet("background-image: url(корзина.bmp); font-size: 14px")

        self.pushButton_16.clicked.connect(self.packer)

    def packer(self):
        self.my_packet = Packet(self)
        self.my_packet.show()

    def backer(self):
        self.close()

    def redactor(self):
        dessert = self.sender().text().strip()
        self.widget = Count(self, dessert)
        self.widget.show()

# Класс Стартеры(Картошка)
class Starters(QMainWindow):
    def __init__(self, *args):
        super().__init__()
        self.setUp(args)

    def setUp(self, args):
        self.setGeometry(0, 0, 1461, 939)

        self.pixmap = QPixmap('backburg.bmp')
        self.image = QLabel(self)
        self.image.move(0, 0)
        self.image.resize(1461, 939)
        self.image.setPixmap(self.pixmap)

        self.back = QPushButton('Назад', self)
        self.back.setGeometry(1361, 35, 70, 30)
        self.back.setStyleSheet('background-color: black; color: white; font-size: 16px;')
        self.back.clicked.connect(self.backer)


        self.pushButton = QPushButton('\n\n\n\n\n\n\n\n\n\n\n\n\nКартофель Фри', self)
        self.pushButton.setGeometry(100, 180, 200, 181)
        self.pushButton.setStyleSheet("background-image: url(фри2.bmp); font-size: 22px")
        self.label = QLabel('Картофель Фри', self)
        font = self.label.font()
        font.setBold(True)
        self.label.setFont(font)
        self.label.setGeometry(140, 380, 181, 20)
        self.label.setStyleSheet('color: white; font-size: 16px')
        self.pushButton.clicked.connect(self.redactor)

        self.pushButton_2 = QPushButton('\n\n\n\n\n\n\n\n\n\n\n\n\nКартофель по-деревенски', self)
        self.pushButton_2.setGeometry(370, 180, 200, 181)
        self.pushButton_2.setStyleSheet("background-image: url(деревня.bmp); font-size: 22px")
        self.label2 = QLabel('Картофель по-деревенски', self)
        font = self.label2.font()
        font.setBold(True)
        self.label2.setFont(font)
        self.label2.setGeometry(360, 380, 250, 20)
        self.label2.setStyleSheet('color: white; font-size: 16px')
        self.pushButton_2.clicked.connect(self.redactor)

        self.pushButton_3 = QPushButton('\n\n\n\n\n\n\n\n\n\n\n\n\nМакфлэйвор Фрайз', self)
        self.pushButton_3.setGeometry(640, 180, 200, 181)
        self.pushButton_3.setStyleSheet("background-image: url(макфри.bmp); font-size: 22px")
        self.label3 = QLabel('Макфлэйвор Фрайз', self)
        font = self.label3.font()
        font.setBold(True)
        self.label3.setFont(font)
        self.label3.setGeometry(665, 380, 181, 20)
        self.label3.setStyleSheet('color: white; font-size: 16px')
        self.pushButton_3.clicked.connect(self.redactor)

        self.pushButton_4 = QPushButton('\n\n\n\n\n\n\n\n\n\n\n\n\nМакфлэйвор Фрайз Д.', self)
        self.pushButton_4.setGeometry(910, 180, 200, 181)
        self.pushButton_4.setStyleSheet("background-image: url(макдеревня.bmp); font-size: 22px")
        self.label4 = QLabel('Макфлэйвор Фрайз Д.', self)
        font = self.label4.font()
        font.setBold(True)
        self.label4.setFont(font)
        self.label4.setGeometry(925, 380, 181, 20)
        self.label4.setStyleSheet('color: white; font-size: 16px')
        self.pushButton_4.clicked.connect(self.redactor)

        self.pushButton_5 = QPushButton('\n\n\n\n\n\n\n\n\n\n\n\n\nСнэк Бокс', self)
        self.pushButton_5.setGeometry(1180, 180, 200, 181)
        self.pushButton_5.setStyleSheet("background-image: url(снэкбокс.bmp); font-size: 16px")
        self.label5 = QLabel('Снэк Бокс', self)
        font = self.label5.font()
        font.setBold(True)
        self.label5.setFont(font)
        self.label5.setGeometry(1239, 380, 181, 20)
        self.label5.setStyleSheet('color: white; font-size: 16px')
        self.pushButton_5.clicked.connect(self.redactor)

        self.pushButton_6 = QPushButton('\n\n\n\n\n\n\n\n\n\n\n\n\nНагетс Бокс', self)
        self.pushButton_6.setGeometry(100, 560, 200, 181)
        self.pushButton_6.setStyleSheet("background-image: url(нагетсбокс.bmp); font-size: 16px")
        self.label6 = QLabel('Нагетс Бокс', self)
        font = self.label6.font()
        font.setBold(True)
        self.label6.setFont(font)
        self.label6.setGeometry(150, 760, 200, 20)
        self.label6.setStyleSheet('color: white; font-size: 16px')
        self.pushButton_6.clicked.connect(self.redactor)

        self.pushButton_7 = QPushButton('\n\n\n\n\n\n\n\n\n\n\n\n\nСтрипсы', self)
        self.pushButton_7.setGeometry(370, 560, 200, 181)
        self.pushButton_7.setStyleSheet("background-image: url(стрипсы.bmp); font-size: 16px")
        self.label7 = QLabel("Стрипсы", self)
        font = self.label7.font()
        font.setBold(True)
        self.label7.setFont(font)
        self.label7.setGeometry(440, 760, 250, 20)
        self.label7.setStyleSheet('color: white; font-size: 16px')
        self.pushButton_7.clicked.connect(self.redactor)

        self.pushButton_8 = QPushButton('\n\n\n\n\n\n\n\n\n\n\n\n\nКреветки', self)
        self.pushButton_8.setGeometry(640, 560, 200, 181)
        self.pushButton_8.setStyleSheet("background-image: url(креветки.bmp); font-size: 16px")
        self.label8 = QLabel('Креветки', self)
        font = self.label8.font()
        font.setBold(True)
        self.label8.setFont(font)
        self.label8.setGeometry(704, 760, 200, 20)
        self.label8.setStyleSheet('color: white; font-size: 16px')
        self.pushButton_8.clicked.connect(self.redactor)

        self.pushButton_9 = QPushButton("\n\n\n\n\n\n\n\n\n\n\n\n\nЧикен Макнаггетс", self)
        self.pushButton_9.setGeometry(910, 560, 200, 181)
        self.pushButton_9.setStyleSheet("background-image: url(нагетсы.bmp); font-size: 22px")
        self.label9 = QLabel("Чикен Макнаггетс", self)
        font = self.label9.font()
        font.setBold(True)
        self.label9.setFont(font)
        self.label9.setGeometry(940, 760, 200, 20)
        self.label9.setStyleSheet('color: white; font-size: 16px')
        self.pushButton_9.clicked.connect(self.redactor)

        self.pushButton_10 = QPushButton('\n\n\n\n\n\n\n\n\n\n\n\n\nКуриные крылышки', self)
        self.pushButton_10.setGeometry(1180, 560, 200, 181)
        self.pushButton_10.setStyleSheet("background-image: url(крылышки.bmp); font-size: 22px")
        self.label10 = QLabel("Куриные крылышки", self)
        font = self.label10.font()
        font.setBold(True)
        self.label10.setFont(font)
        self.label10.setGeometry(1204, 760, 200, 20)
        self.label10.setStyleSheet('color: white; font-size: 16px')
        self.pushButton_10.clicked.connect(self.redactor)

        self.packet = QPushButton('Ваша корзина:\n\n\n\n', self)
        self.packet.setGeometry(1185, 820, 200, 111)
        self.packet.setStyleSheet("background-image: url(корзина.bmp); font-size: 14px")

        self.packet.clicked.connect(self.packer)

    def packer(self):
        self.my_packet = Packet(self)
        self.my_packet.show()

    def backer(self):
        self.close()

    def redactor(self):
        sauce = self.sender().text().strip()
        self.widget = Count(self, sauce)
        self.widget.show()


# Класс Напитки
class Drinks(QMainWindow):
    def __init__(self, *args):
        super().__init__()
        self.setUp(args)

    def setUp(self, args):
        self.setGeometry(0, 0, 1461, 939)

        self.pixmap = QPixmap('backburg.bmp')
        self.image = QLabel(self)
        self.image.move(0, 0)
        self.image.resize(1461, 939)
        self.image.setPixmap(self.pixmap)

        self.back = QPushButton('Назад', self)
        self.back.setGeometry(1361, 35, 70, 30)
        self.back.setStyleSheet('background-color: black; color: white; font-size: 16px;')
        self.back.clicked.connect(self.backer)

        self.btnhot = QPushButton(self)
        self.btnhot.setGeometry(220, 250, 400, 400)
        self.btnhot.setStyleSheet("background-image: url(hotdrinks.bmp);")
        self.labelhot = QLabel('Горячие напитки', self)
        self.labelhot.setGeometry(280, 650, 400, 30)
        self.labelhot.setStyleSheet('color: white; font-size: 25px')
        font = self.labelhot.font()
        font.setBold(True)
        self.labelhot.setFont(font)
        self.btnhot.clicked.connect(self.hot)


        self.btncold = QPushButton(self)
        self.btncold.setGeometry(840, 250, 400, 400)
        self.btncold.setStyleSheet("background-image: url(colddrinks.bmp)")
        self.labelcold = QLabel('Холодные напитки', self)
        self.labelcold.setGeometry(900, 650, 400, 30)
        self.labelcold.setStyleSheet('color: white; font-size: 25px')
        font = self.labelcold.font()
        font.setBold(True)
        self.labelcold.setFont(font)
        self.btncold.clicked.connect(self.cold)

    def hot(self):
        self.my_hot_drinks = HotDrinks(self, 'SMTH')
        self.my_hot_drinks.show()

    def cold(self):
        self.my_cold_drinks = ColdDrinks(self, 'SMTH')
        self.my_cold_drinks.show()

    def backer(self):
        self.close()


# Класс Горячие напитки
class HotDrinks(QMainWindow):
    def __init__(self, *args):
        super().__init__()
        self.setUp(args)

    def setUp(self, args):
        self.setGeometry(0, 0, 1461, 939)

        self.pixmap = QPixmap('backburg.bmp')
        self.image = QLabel(self)
        self.image.move(0, 0)
        self.image.resize(1461, 939)
        self.image.setPixmap(self.pixmap)

        self.back = QPushButton('Назад', self)
        self.back.setGeometry(1361, 35, 70, 30)
        self.back.setStyleSheet('background-color: black; color: white; font-size: 16px;')
        self.back.clicked.connect(self.backer)

        self.pushButton = QPushButton('Ягодный пунш\n\n\n\n\n\n\n\n\n\n\n\n\n', self)
        self.pushButton.setGeometry(100, 180, 181, 200)
        self.pushButton.setStyleSheet("background-image: url(ягода.bmp); font-size: 16px")
        self.label = QLabel('Ягодный пунш', self)
        font = self.label.font()
        font.setBold(True)
        self.label.setFont(font)
        self.label.setGeometry(135, 390, 181, 20)
        self.label.setStyleSheet('color: white; font-size: 16px')
        self.pushButton.clicked.connect(self.redactor)

        self.pushButton_2 = QPushButton('\n\n\n\n\n\n\n\n\n\n\n\n\n\nЧай Чёрный', self)
        self.pushButton_2.setGeometry(370, 180, 181, 200)
        self.pushButton_2.setStyleSheet("background-image: url(чайчерный.bmp); font-size: 16px")
        self.label2 = QLabel('Чай Чёрный', self)
        font = self.label2.font()
        font.setBold(True)
        self.label2.setFont(font)
        self.label2.setGeometry(420, 390, 181, 20)
        self.label2.setStyleSheet('color: white; font-size: 16px')
        self.pushButton_2.clicked.connect(self.redactor)

        self.pushButton_3 = QPushButton('\n\n\n\n\n\n\n\n\n\n\n\n\n\nЧай Зелёный', self)
        self.pushButton_3.setGeometry(640, 180, 181, 200)
        self.pushButton_3.setStyleSheet("background-image: url(чайзеленый.bmp); font-size: 16px")
        self.label3 = QLabel('Чай Зелёный', self)
        font = self.label3.font()
        font.setBold(True)
        self.label3.setFont(font)
        self.label3.setGeometry(680, 390, 181, 20)
        self.label3.setStyleSheet('color: white; font-size: 16px')
        self.pushButton_3.clicked.connect(self.redactor)

        self.pushButton_4 = QPushButton('\n\n\n\n\n\n\n\n\n\nЧай Чёрный Эрл Грей', self)
        self.pushButton_4.setGeometry(910, 180, 181, 200)
        self.pushButton_4.setStyleSheet("background-image: url(чайэрл.bmp); font-size: 16px")
        self.label4 = QLabel('Чай Чёрный Эрл Грей', self)
        font = self.label4.font()
        font.setBold(True)
        self.label4.setFont(font)
        self.label4.setGeometry(910, 390, 181, 20)
        self.label4.setStyleSheet('color: white; font-size: 16px')
        self.pushButton_4.clicked.connect(self.redactor)

        self.pushButton_5 = QPushButton('\n\n\n\n\n\n\n\n\n\n\nАйриш Капучино', self)
        self.pushButton_5.setGeometry(1180, 180, 181, 200)
        self.pushButton_5.setStyleSheet("background-image: url(айриш.bmp); font-size: 16px")
        self.label5 = QLabel('Айриш Капучино', self)
        font = self.label5.font()
        font.setBold(True)
        self.label5.setFont(font)
        self.label5.setGeometry(1200, 390, 181, 20)
        self.label5.setStyleSheet('color: white; font-size: 16px')
        self.pushButton_5.clicked.connect(self.redactor)

        self.pushButton_6 = QPushButton('\n\n\n\n\n\n\n\n\n\n\n\n\n\nКапучино', self)
        self.pushButton_6.setGeometry(100, 560, 181, 200)
        self.pushButton_6.setStyleSheet("background-image: url(капучино.bmp); font-size: 16px")
        self.label6 = QLabel('Капучино', self)
        font = self.label6.font()
        font.setBold(True)
        self.label6.setFont(font)
        self.label6.setGeometry(140, 770, 200, 20)
        self.label6.setStyleSheet('color: white; font-size: 16px')
        self.pushButton_6.clicked.connect(self.redactor)

        self.pushButton_7 = QPushButton('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nЛатте', self)
        self.pushButton_7.setGeometry(370, 560, 181, 200)
        self.pushButton_7.setStyleSheet("background-image: url(латте.bmp); font-size: 16px")
        self.label7 = QLabel("Латте", self)
        font = self.label7.font()
        font.setBold(True)
        self.label7.setFont(font)
        self.label7.setGeometry(430, 770, 250, 20)
        self.label7.setStyleSheet('color: white; font-size: 16px')
        self.pushButton_7.clicked.connect(self.redactor)

        self.pushButton_8 = QPushButton('\n\n\n\n\n\n\n\n\n\n\n\n\n\nАмерикано', self)
        self.pushButton_8.setGeometry(640, 560, 181, 200)
        self.pushButton_8.setStyleSheet("background-image: url(американо.bmp); font-size: 16px")
        self.label8 = QLabel('Американо', self)
        font = self.label8.font()
        font.setBold(True)
        self.label8.setFont(font)
        self.label8.setGeometry(685, 770, 200, 20)
        self.label8.setStyleSheet('color: white; font-size: 16px')
        self.pushButton_8.clicked.connect(self.redactor)

        self.pushButton_9 = QPushButton('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nКофе Глясе', self)
        self.pushButton_9.setGeometry(910, 560, 181, 200)
        self.pushButton_9.setStyleSheet("background-image: url(гляссе.bmp); font-size: 16px")
        self.label9 = QLabel("Кофе Глясе", self)
        font = self.label9.font()
        font.setBold(True)
        self.label9.setFont(font)
        self.label9.setGeometry(945, 770, 200, 20)
        self.label9.setStyleSheet('color: white; font-size: 16px')
        self.pushButton_9.clicked.connect(self.redactor)

        self.pushButton_10 = QPushButton('\n\n\n\n\n\n\n\n\n\n\n\n\n\nДвойной Эспрессо', self)
        self.pushButton_10.setGeometry(1180, 560, 181, 200)
        self.pushButton_10.setStyleSheet("background-image: url(эспрессо.bmp); font-size: 16px")
        self.label10 = QLabel("Двойной Эспрессо", self)
        font = self.label10.font()
        font.setBold(True)
        self.label10.setFont(font)
        self.label10.setGeometry(1190, 770, 200, 20)
        self.label10.setStyleSheet('color: white; font-size: 16px')
        self.pushButton_10.clicked.connect(self.redactor)

        self.packet = QPushButton('Ваша корзина:\n\n\n\n', self)
        self.packet.setGeometry(1180, 820, 181, 111)
        self.packet.setStyleSheet("background-image: url(корзина.bmp); font-size: 14px")

        self.packet.clicked.connect(self.packer)

    def packer(self):
        self.my_packet = Packet(self)
        self.my_packet.show()

    def redactor(self):
        sauce = self.sender().text().strip()
        self.widget = Count(self, sauce)
        self.widget.show()

    def backer(self):
        self.close()


# Класс Холодные напитки
class ColdDrinks(QMainWindow):
    def __init__(self, *args):
        super().__init__()
        self.setUp(args)

    def setUp(self, args):
        self.setGeometry(0, 0, 1461, 939)

        self.pixmap = QPixmap('backburg.bmp')
        self.image = QLabel(self)
        self.image.move(0, 0)
        self.image.resize(1461, 939)
        self.image.setPixmap(self.pixmap)

        self.back = QPushButton('Назад', self)
        self.back.setGeometry(1361, 35, 70, 30)
        self.back.setStyleSheet('background-color: black; color: white; font-size: 16px;')
        self.back.clicked.connect(self.backer)

        self.pushButton = QPushButton('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nКока-Кола', self)
        self.pushButton.setGeometry(100, 70, 181, 200)
        self.pushButton.setStyleSheet("background-image: url(кола.bmp); font-size: 16px")
        self.label = QLabel('Кока-Кола', self)
        font = self.label.font()
        font.setBold(True)
        self.label.setFont(font)
        self.label.setGeometry(145, 280, 181, 20)
        self.label.setStyleSheet('color: white; font-size: 16px')
        self.pushButton.clicked.connect(self.redactor)

        self.pushButton_2 = QPushButton('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nФанта', self)
        self.pushButton_2.setGeometry(370, 70, 181, 200)
        self.pushButton_2.setStyleSheet("background-image: url(фанта.bmp); font-size: 16px")
        self.label2 = QLabel('Фанта', self)
        font = self.label2.font()
        font.setBold(True)
        self.label2.setFont(font)
        self.label2.setGeometry(435, 280, 181, 20)
        self.label2.setStyleSheet('color: white; font-size: 16px')
        self.pushButton_2.clicked.connect(self.redactor)

        self.pushButton_3 = QPushButton('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nСпрайт', self)
        self.pushButton_3.setGeometry(640, 70, 181, 200)
        self.pushButton_3.setStyleSheet("background-image: url(спрайт.bmp); font-size: 16px")
        self.label3 = QLabel('Спрайт', self)
        font = self.label3.font()
        font.setBold(True)
        self.label3.setFont(font)
        self.label3.setGeometry(700, 280, 181, 20)
        self.label3.setStyleSheet('color: white; font-size: 16px')
        self.pushButton_3.clicked.connect(self.redactor)

        self.pushButton_4 = QPushButton('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nКока-Кола Зеро', self)
        self.pushButton_4.setGeometry(910, 70, 181, 200)
        self.pushButton_4.setStyleSheet("background-image: url(колазеро.bmp); font-size: 16px")
        self.label4 = QLabel('Кока-Кола Зеро', self)
        font = self.label4.font()
        font.setBold(True)
        self.label4.setFont(font)
        self.label4.setGeometry(930, 280, 181, 20)
        self.label4.setStyleSheet('color: white; font-size: 16px')
        self.pushButton_4.clicked.connect(self.redactor)

        self.pushButton_5 = QPushButton('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nЛиптон Лимонный', self)
        self.pushButton_5.setGeometry(1180, 70, 181, 200)
        self.pushButton_5.setStyleSheet("background-image: url(липтонлим.bmp); font-size: 16px")
        self.label5 = QLabel('Липтон Лимонный', self)
        font = self.label5.font()
        font.setBold(True)
        self.label5.setFont(font)
        self.label5.setGeometry(1195, 280, 181, 20)
        self.label5.setStyleSheet('color: white; font-size: 16px')
        self.pushButton_5.clicked.connect(self.redactor)

        self.pushButton_6 = QPushButton('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nЛиптон Зелённый', self)
        self.pushButton_6.setGeometry(100, 331, 181, 200)
        self.pushButton_6.setStyleSheet("background-image: url(липтонзел.bmp); font-size: 16px")
        self.label6 = QLabel('Липтон Зелённый', self)
        font = self.label6.font()
        font.setBold(True)
        self.label6.setFont(font)
        self.label6.setGeometry(106, 541, 200, 20)
        self.label6.setStyleSheet('color: white; font-size: 16px')
        self.pushButton_6.clicked.connect(self.redactor)

        self.pushButton_7 = QPushButton('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nПитьевая вода Аква Минерале', self)
        self.pushButton_7.setGeometry(370, 331, 181, 200)
        self.pushButton_7.setStyleSheet("background-image: url(аква.bmp); font-size: 16px")
        self.label7 = QLabel("Питьевая вода Аква Минерале", self)
        font = self.label7.font()
        font.setBold(True)
        self.label7.setFont(font)
        self.label7.setGeometry(340, 541, 250, 20)
        self.label7.setStyleSheet('color: white; font-size: 16px')

        self.pushButton_8 = QPushButton('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nАпельсиновый сок', self)
        self.pushButton_8.setGeometry(640, 331, 181, 200)
        self.pushButton_8.setStyleSheet("background-image: url(апельсин.bmp); font-size: 16px")
        self.label8 = QLabel('Апельсиновый сок', self)
        font = self.label8.font()
        font.setBold(True)
        self.label8.setFont(font)
        self.label8.setGeometry(650, 541, 200, 20)
        self.label8.setStyleSheet('color: white; font-size: 16px')
        self.pushButton_8.clicked.connect(self.redactor)

        self.pushButton_9 = QPushButton('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nЯблочный сок', self)
        self.pushButton_9.setGeometry(910, 331, 181, 200)
        self.pushButton_9.setStyleSheet("background-image: url(яблоко.bmp); font-size: 16px")
        self.label9 = QLabel("Яблочный сок", self)
        font = self.label9.font()
        font.setBold(True)
        self.label9.setFont(font)
        self.label9.setGeometry(935, 541, 200, 20)
        self.label9.setStyleSheet('color: white; font-size: 16px')
        self.pushButton_9.clicked.connect(self.redactor)

        self.pushButton_10 = QPushButton('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nШейк Манго-Маракуйя', self)
        self.pushButton_10.setGeometry(1180, 331, 181, 200)
        self.pushButton_10.setStyleSheet("background-image: url(мангомаракуйя.bmp); font-size: 16px")
        self.label10 = QLabel("Шейк Манго-Маракуйя", self)
        font = self.label10.font()
        font.setBold(True)
        self.label10.setFont(font)
        self.label10.setGeometry(1170, 541, 200, 20)
        self.label10.setStyleSheet('color: white; font-size: 16px')
        self.pushButton_10.clicked.connect(self.redactor)

        self.pushButton_11 = QPushButton('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nМолочный Коктейль Клубничный', self)
        self.pushButton_11.setGeometry(370, 592, 181, 200)
        self.pushButton_11.setStyleSheet("background-image: url(коктейльклуб.bmp);")
        self.label11 = QLabel("Молочный Коктейль\n       Клубничный", self)
        font = self.label11.font()
        font.setBold(True)
        self.label11.setFont(font)
        self.label11.setGeometry(370, 802, 200, 40)
        self.label11.setStyleSheet('color: white; font-size: 16px')
        self.pushButton_11.clicked.connect(self.redactor)

        self.pushButton_12 = QPushButton('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nМолочный Коктейль Ванильный', self)
        self.pushButton_12.setGeometry(640, 592, 181, 200)
        self.pushButton_12.setStyleSheet("background-image: url(коктейльван.bmp)")
        self.label12 = QLabel("Молочный Коктейль\n       Ванильный", self)
        font = self.label12.font()
        font.setBold(True)
        self.label12.setFont(font)
        self.label12.setGeometry(640, 802, 200, 40)
        self.label12.setStyleSheet('color: white; font-size: 16px')
        self.pushButton_12.clicked.connect(self.redactor)

        self.pushButton_13 = QPushButton('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nМолочный Коктейль Шоколадный', self)
        self.pushButton_13.setGeometry(910, 592, 181, 200)
        self.pushButton_13.setStyleSheet("background-image: url(коктейльшок.bmp);")
        self.label13 = QLabel("Молочный Коктейль\n       Шоколадный", self)
        font = self.label13.font()
        font.setBold(True)
        self.label13.setFont(font)
        self.label13.setGeometry(910, 802, 200, 40)
        self.label13.setStyleSheet('color: white; font-size: 16px')
        self.pushButton_13.clicked.connect(self.redactor)

        self.packet = QPushButton('Ваша корзина:\n\n\n\n', self)
        self.packet.setGeometry(1180, 820, 181, 111)
        self.packet.setStyleSheet("background-image: url(корзина.bmp); font-size: 14px")

        self.packet.clicked.connect(self.packer)

    def packer(self):
        self.my_packet = Packet(self)
        self.my_packet.show()

    def redactor(self):
        sauce = self.sender().text().strip()
        self.widget = Count(self, sauce)
        self.widget.show()

    def backer(self):
        self.close()

# Класс Роллы
class Rolls(QMainWindow):
    def __init__(self, *args):
        super().__init__()
        self.setup(args)

    def setup(self, args):
        self.setGeometry(0, 0, 1461, 939)

        self.pixmap = QPixmap('backburg.bmp')
        self.image = QLabel(self)
        self.image.move(0, 0)
        self.image.resize(1461, 939)
        self.image.setPixmap(self.pixmap)
        self.back = QPushButton('Назад', self)
        self.back.setGeometry(1361, 35, 70, 30)
        self.back.setStyleSheet('background-color: black; color: white; font-size: 16px;')
        self.back.clicked.connect(self.backer)

        self.bigt = QPushButton('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nБиг Тейсти Ролл', self)
        self.bigt.setGeometry(140, 358, 340, 240)
        self.bigt.setStyleSheet('background-image: url(бигтейстиролл.bmp)')
        self.labelbigt = QLabel('Биг Тейсти Ролл', self)
        self.labelbigt.setGeometry(220, 608, 340, 20)
        font = self.labelbigt.font()
        font.setBold(True)
        self.labelbigt.setFont(font)
        self.labelbigt.setStyleSheet('font-size: 22px; color: white')
        self.bigt.clicked.connect(self.redactor)


        self.shrimp = QPushButton('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nШримп Ролл', self)
        self.shrimp.setGeometry(550, 358, 340, 240)
        self.shrimp.setStyleSheet('background-image: url(шримпролл.bmp)')
        self.labelshr = QLabel('Шримп Ролл', self)
        self.labelshr.setGeometry(640, 608, 340, 20)
        font = self.labelshr.font()
        font.setBold(True)
        self.labelshr.setFont(font)
        self.labelshr.setStyleSheet('font-size: 22px; color: white')
        self.shrimp.clicked.connect(self.redactor)


        self.cezar = QPushButton('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nЦезарь Ролл', self)
        self.cezar.setGeometry(960, 358, 340, 240)
        self.cezar.setStyleSheet('background-image: url(цезарьролл.bmp)')
        self.labelcez = QLabel('Цезарь Ролл', self)
        self.labelcez.setStyleSheet('font-size: 22px; color: white')
        self.labelcez.setGeometry(1040, 608, 340, 20)
        font = self.labelcez.font()
        font.setBold(True)
        self.labelcez.setFont(font)
        self.cezar.clicked.connect(self.redactor)


        self.packet = QPushButton('Ваша корзина:\n\n\n\n', self)
        self.packet.setGeometry(1180, 820, 200, 111)
        self.packet.setStyleSheet("background-image: url(корзина.bmp); font-size: 14px")

        self.packet.clicked.connect(self.packer)

    def packer(self):
        self.my_packet = Packet(self)
        self.my_packet.show()

    def redactor(self):
        sauce = self.sender().text().strip()
        self.widget = Count(self, sauce)
        self.widget.show()

    def backer(self):
        self.close()


class Burgers(QMainWindow):
    def __init__(self, *args):
        super().__init__()
        self.setupUi(args)

    def setupUi(self, args):
        self.setGeometry(0, 0, 1461, 939)

        self.pixmap = QPixmap('backburg.bmp')

        self.image = QLabel(self)
        self.image.move(0, 0)
        self.image.resize(1461, 939)
        self.image.setPixmap(self.pixmap)

        self.back = QPushButton('Назад', self)
        self.back.setGeometry(1361, 35, 70, 30)
        self.back.setStyleSheet('background-color: black; color: white; font-size: 16px;')
        self.back.clicked.connect(self.backer)

        self.pushButton = QPushButton('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nБиг Мак', self)
        self.pushButton.setGeometry(100, 70, 200, 181)
        self.pushButton.setStyleSheet("background-image: url(бигмак.bmp); font-size: 16px")
        self.label = QLabel('  Биг Мак', self)
        font = self.label.font()
        font.setBold(True)
        self.label.setFont(font)
        self.label.setGeometry(145, 270, 200, 15)
        self.label.setStyleSheet('color: white; font-size: 16px')
        self.pushButton.clicked.connect(self.redactor)

        self.pushButton_2 = QPushButton('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nБиг Тейсти', self)
        self.pushButton_2.setGeometry(370, 70, 200, 181)
        self.pushButton_2.setStyleSheet("background-image: url(бигтейсти2.bmp); font-size: 16px")
        self.label2 = QLabel(' Биг Тейсти', self)
        font = self.label2.font()
        font.setBold(True)
        self.label2.setFont(font)
        self.label2.setGeometry(420, 270, 200, 15)
        self.label2.setStyleSheet('color: white; font-size: 16px')
        self.pushButton_2.clicked.connect(self.redactor)

        self.pushButton_3 = QPushButton('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nДвойной Биг Тейсти', self)
        self.pushButton_3.setGeometry(640, 70, 200, 181)
        self.pushButton_3.setStyleSheet("background-image: url(даблбигтейсти.bmp); font-size: 16px")
        self.label3 = QLabel(' Двойной Биг Тейсти', self)
        font = self.label3.font()
        font.setBold(True)
        self.label3.setFont(font)
        self.label3.setGeometry(650, 270, 200, 15)
        self.label3.setStyleSheet('color: white; font-size: 16px')
        self.pushButton.clicked.connect(self.redactor)

        self.pushButton_4 = QPushButton('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nБиг Тейсти Джуниор', self)
        self.pushButton_4.setGeometry(910, 70, 200, 181)
        self.pushButton_4.setStyleSheet("background-image: url(бигтейстидж.bmp); font-size: 16px")
        self.label4 = QLabel('Биг Тейсти Джуниор', self)
        font = self.label4.font()
        font.setBold(True)
        self.label4.setFont(font)
        self.label4.setGeometry(925, 270, 200, 15)
        self.label4.setStyleSheet('color: white; font-size: 16px')
        self.pushButton_4.clicked.connect(self.redactor)

        self.pushButton_5 = QPushButton('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nДвойной Биг Мак', self)
        self.pushButton_5.setGeometry(1180, 70, 200, 181)
        self.pushButton_5.setStyleSheet("background-image: url(даблбигмак.bmp); font-size: 16px")
        self.label5 = QLabel('Двойной Биг Мак', self)
        font = self.label5.font()
        font.setBold(True)
        self.label5.setFont(font)
        self.label5.setGeometry(1200, 270, 200, 15)
        self.label5.setStyleSheet('color: white; font-size: 16px')
        self.pushButton_5.clicked.connect(self.redactor)

        self.pushButton_6 = QPushButton('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nРоял Де Люкс', self)
        self.pushButton_6.setGeometry(100, 331, 200, 181)
        self.pushButton_6.setStyleSheet("background-image: url(роялделюкс.bmp); font-size: 16px")
        self.label6 = QLabel('Роял Де Люкс', self)
        font = self.label6.font()
        font.setBold(True)
        self.label6.setFont(font)
        self.label6.setGeometry(125, 531, 200, 20)
        self.label6.setStyleSheet('color: white; font-size: 16px')
        self.pushButton_6.clicked.connect(self.redactor)

        self.pushButton_7 = QPushButton('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nДвойной Роял', self)
        self.pushButton_7.setGeometry(370, 331, 200, 181)
        self.pushButton_7.setStyleSheet("background-image: url(даблроял.bmp); font-size: 16px")
        self.label7 = QLabel('Двойной Роял', self)
        font = self.label7.font()
        font.setBold(True)
        self.label7.setFont(font)
        self.label7.setGeometry(405, 531, 200, 20)
        self.label7.setStyleSheet('color: white; font-size: 16px')
        self.pushButton_7.clicked.connect(self.redactor)

        self.pushButton_8 = QPushButton('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nРоял', self)
        self.pushButton_8.setGeometry(640, 331, 200, 181)
        self.pushButton_8.setStyleSheet("background-image: url(роял.bmp); font-size: 16px")
        self.label8 = QLabel('Роял', self)
        font = self.label8.font()
        font.setBold(True)
        self.label8.setFont(font)
        self.label8.setGeometry(720, 531, 200, 20)
        self.label8.setStyleSheet('color: white; font-size: 16px')
        self.pushButton_8.clicked.connect(self.redactor)

        self.pushButton_9 = QPushButton('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nДвойной Чизбургер', self)
        self.pushButton_9.setGeometry(910, 331, 200, 181)
        self.pushButton_9.setStyleSheet("background-image: url(даблчизбургер.bmp); font-size: 16px")
        self.label9 = QLabel("Двойной Чизбургер", self)
        font = self.label9.font()
        font.setBold(True)
        self.label9.setFont(font)
        self.label9.setGeometry(935, 531, 200, 20)
        self.label9.setStyleSheet('color: white; font-size: 16px')
        self.pushButton_9.clicked.connect(self.redactor)

        self.pushButton_10 = QPushButton('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nЧизбургер', self)
        self.pushButton_10.setGeometry(1180, 331, 200, 181)
        self.pushButton_10.setStyleSheet("background-image: url(чизбургер.bmp); font-size: 16px")
        self.label10 = QLabel("Чизбургер", self)
        font = self.label10.font()
        font.setBold(True)
        self.label10.setFont(font)
        self.label10.setGeometry(1245, 531, 200, 20)
        self.label10.setStyleSheet('color: white; font-size: 16px')
        self.pushButton_10.clicked.connect(self.redactor)

        self.pushButton_11 = QPushButton('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nЧикен Премьер', self)
        self.pushButton_11.setGeometry(100, 592, 200, 181)
        self.pushButton_11.setStyleSheet("background-image: url(чикенпремьер.bmp)")
        self.label11 = QLabel("Чикен Премьер", self)
        font = self.label11.font()
        font.setBold(True)
        self.label11.setFont(font)
        self.label11.setGeometry(135, 792, 200, 20)
        self.label11.setStyleSheet('color: white; font-size: 16px')
        self.pushButton_11.clicked.connect(self.redactor)

        self.pushButton_12 = QPushButton('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nМакчикен', self)
        self.pushButton_12.setGeometry(370, 592, 200, 181)
        self.pushButton_12.setStyleSheet("background-image: url(макчикен.bmp);")
        self.label12 = QLabel("Макчикен", self)
        font = self.label12.font()
        font.setBold(True)
        self.label12.setFont(font)
        self.label12.setGeometry(425, 792, 200, 20)
        self.label12.setStyleSheet('color: white; font-size: 16px')
        self.pushButton_12.clicked.connect(self.redactor)

        self.pushButton_13 = QPushButton('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nЧикенбургер', self)
        self.pushButton_13.setGeometry(640, 592, 200, 181)
        self.pushButton_13.setStyleSheet("background-image: url(чикенбургер.bmp)")
        self.label13 = QLabel("Чикенбургер", self)
        font = self.label13.font()
        font.setBold(True)
        self.label13.setFont(font)
        self.label13.setGeometry(680, 792, 200, 20)
        self.label13.setStyleSheet('color: white; font-size: 16px')
        self.pushButton_13.clicked.connect(self.redactor)

        self.pushButton_14 = QPushButton('Двойной Филе-О-Фиш', self)
        self.pushButton_14.setGeometry(910, 592, 200, 181)
        self.pushButton_14.setStyleSheet("background-image: url(даблфилеофиш.bmp);")
        self.label14 = QLabel("Двойной Филе-О-Фиш", self)
        font = self.label14.font()
        font.setBold(True)
        self.label14.setFont(font)
        self.label14.setGeometry(910, 792, 200, 20)
        self.label14.setStyleSheet('color: white; font-size: 16px')
        self.pushButton_14.clicked.connect(self.redactor)

        self.pushButton_15 = QPushButton('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nФиле-О-Фиш', self)
        self.pushButton_15.setGeometry(1180, 592, 200, 181)
        self.pushButton_15.setStyleSheet("background-image: url(филеофиш.bmp);")
        self.label15 = QLabel("Филе-О-Фиш", self)
        font = self.label15.font()
        font.setBold(True)
        self.label15.setFont(font)
        self.label15.setGeometry(1225, 792, 200, 20)
        self.label15.setStyleSheet('color: white; font-size: 16px')
        self.pushButton_15.clicked.connect(self.redactor)

        self.pushButton_16 = QPushButton('Ваша корзина:\n\n\n\n', self)
        self.pushButton_16.setGeometry(1180, 820, 200, 111)
        self.pushButton_16.setStyleSheet("background-image: url(корзина.bmp); font-size: 14px")

        self.pushButton_16.clicked.connect(self.packer)

    def packer(self):
        print(1)
        self.my_packet = Packet(self)
        print(3)
        self.my_packet.show()

    def redactor(self):
        sauce = self.sender().text().strip()
        self.widget = Count(self, sauce)
        self.widget.show()

    def backer(self):
        self.close()




class PasswordRecovery(QMainWindow):
    def __init__(self, *args):
        super().__init__()
        self.initUI(args)

    def initUI(self, args):
        self.setGeometry(720, 250, 500, 500)
        self.setWindowTitle('Восстановление пароля')

        self.real_login = args[-1]

        self.pixmap3 = QPixmap('res2.bmp')

        self.image_rec = QLabel(self)
        self.image_rec.move(0, 0)
        self.image_rec.resize(500, 500)
        self.image_rec.setPixmap(self.pixmap3)

        self.question1 = QLabel('ФИО:', self)
        self.question1.move(30, 70)
        self.question1.setStyleSheet("font-size: 22px; color: white")

        self.answer1 = QLineEdit(self)
        self.answer1.setGeometry(100, 70, 370, 30)
        self.answer1.setStyleSheet("color: black; font-size: 22px;")

        self.question2 = QLabel('Имя вашей матери:', self)
        self.question2.setGeometry(30, 120, 250, 30)
        self.question2.setStyleSheet("font-size: 22px; color: white")

        self.answer2 = QLineEdit(self)
        self.answer2.setGeometry(250, 120, 220, 30)
        self.answer2.setStyleSheet("color: black; font-size: 22px;")

        self.question3 = QLabel('''Название вашей\nлюбимой страны:''', self)
        self.question3.setGeometry(30, 170, 250, 50)
        self.question3.setStyleSheet("font-size: 22px; color: white")

        self.answer3 = QLineEdit(self)
        self.answer3.setGeometry(250, 180, 220, 35)
        self.answer3.setStyleSheet("font-size: 22px; color: black")

        self.check = QPushButton('Проверка', self)
        self.check.setGeometry(350, 240, 120, 30)
        self.check.setStyleSheet("font-size: 22px; color: black;")

        self.check.clicked.connect(self.open_menu)

    def open_menu(self):
        answer1 = self.answer1.text().strip().lower()
        answer2 = self.answer2.text().strip().lower()
        answer3 = self.answer3.text().strip().lower()

        if answer1 in users[self.real_login][1]:
            if answer2 in answers[self.real_login]:
                if answer3 in answers[self.real_login]:
                    self.close()
                    self.change = Changer(self, f'{self.real_login}')
                    self.change.show()
                else:
                    QMessageBox.critical(self, "Ошибка ", "Неправильный ответ!", QMessageBox.Ok)
            else:
                QMessageBox.critical(self, "Ошибка ", "Неправильный ответ!", QMessageBox.Ok)
        else:
            QMessageBox.critical(self, "Ошибка ", "Неправильный ответ!", QMessageBox.Ok)



class Packet(QWidget):
    def __init__(self, *args):
        super().__init__()
        self.packet_of_order(args)

    def packet_of_order(self, args):
        self.setGeometry(0, 0, 1461, 939)

        self.pixmap = QPixmap('backburg.bmp')

        self.image = QLabel(self)
        self.image.move(0, 0)
        self.image.resize(1461, 939)
        self.image.setPixmap(self.pixmap)

        self.label = QLabel('Ваш заказ', self)
        self.label.setGeometry(700, 10, 500, 30)
        self.label.setStyleSheet('color: white; font-size: 22px')

        self.setGeometry(100, 50, 900, 700)
        print(1)
        central_widget = QWidget(self)
        print(2)
        self.setCentralWidget(central_widget)
        print(3)

        grid_layout = QGridLayout()
        print(4)
        central_widget.setLayout(grid_layout)
        print(5)

        table = QTableWidget(self)
        table.setColumnCount(3)
        table.setRowCount(10)

        table.setHorizontalHeaderLabels(["Блюдо", "Количество", "Стоимость"])

        table.horizontalHeaderItem(0).setToolTip("Column 1 ")
        table.horizontalHeaderItem(1).setToolTip("Column 2 ")
        table.horizontalHeaderItem(2).setToolTip("Column 3 ")

        table.horizontalHeaderItem(0).setTextAlignment(Qt.AlignLeft)
        table.horizontalHeaderItem(1).setTextAlignment(Qt.AlignHCenter)
        table.horizontalHeaderItem(2).setTextAlignment(Qt.AlignRight)

        table.setItem(0, 0, QTableWidget("Text in column 1"))
        table.setItem(0, 1, QTableWidget("Text in column 2"))
        table.setItem(0, 2, QTableWidget("Text in column 3"))

        table.setItem(1, 0, QTableWidget("Text in column 1"))
        table.setItem(1, 1, QTableWidget("Text in column 2"))
        table.setItem(1, 2, QTableWidget("Text in column 3"))

        table.resizeColumnsToContents()

        grid_layout.addWidget(table, 0, 10)


# Просмотр пароля
class Changer(QMainWindow):
    def __init__(self, *args):
        super().__init__()
        self.initUI(args)

    def initUI(self, args):
        self.setGeometry(720, 250, 500, 500)
        self.setWindowTitle('Это макдаковский секрет')
        self.login = args[-1]
        self.pixmap4 = QPixmap('res2.bmp')

        self.image4 = QLabel(self)
        self.image4.move(0, 0)
        self.image4.resize(500, 500)
        self.image4.setPixmap(self.pixmap4)

        self.dlg = QLabel('Тсссс... Только никому!', self)
        self.dlg.setGeometry(80, 200, 350, 30)
        self.dlg.setStyleSheet('font-size: 30px; color: white;')

        self.change_pass = QLabel("Ваш пароль:", self)
        self.change_pass.setGeometry(50, 250, 250, 30)
        self.change_pass.setStyleSheet("font-size: 26px; color: white;")

        self.new_pass = QLabel(f'{users[self.login][0]}', self)
        self.new_pass.setGeometry(290, 250, 200, 30)
        self.new_pass.setStyleSheet("font-size: 26px; color: white;")



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())