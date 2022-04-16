from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QPushButton, QLineEdit, QVBoxLayout, QHBoxLayout
from PyQt5.QtCore import Qt

app = QApplication([])
#первое окно
win = QWidget()
win.setWindowTitle('окно 1')
win.resize(1920, 1080)
win.show()
#скрытие первого окна
def dasd():
    win.hide()
    win2.show()
#первое окно 2
label1 = QLabel('Добро пожаловать в программу по определению состояния здоровья!')
label2 = QLabel('Данное приложение позволит вам с помощью теста Руфье провести первичную диагностику вашего здоровья.\n'
                   'Проба Руфье представляет собой нагрузочный комплекс, предназначенный для оценки работоспособности сердца при физической нагрузке.\n'
                   'У испытуемого, находящегося в положении лёжа на спине в течение 5 мин, определяют частоту пульса за 15 секунд;\n'
                   'затем в течение 45 секунд испытуемый выполняет 30 приседаний.\n'
                   'После окончания нагрузки испытуемый ложится, и у него вновь подсчитывается число пульсаций за первые 15 секунд,\n'
                   'а потом — за последние 15 секунд первой минуты периода восстановления.\n'
                   'Важно! Если в процессе проведения испытания вы почувствуете себя плохо (появится головокружение, шум в\n'
                   'ушах, сильная одышка и др.), то тест необходимо прервать и обратиться к врачу.')
button1 = QPushButton('Начать')
v_line1 = QVBoxLayout()
v_line1.addWidget(label1, alignment=Qt.AlignCenter)
v_line1.addWidget(label2, alignment=Qt.AlignCenter)
v_line1.addWidget(button1, alignment=Qt.AlignCenter)
win.setLayout(v_line1)
button1.clicked.connect(dasd)
app.exec_()
