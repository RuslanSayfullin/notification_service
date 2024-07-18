from PyQt6 import QtWidgets
import sys

# Использование контейнера QFormLayout
app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("QFormLayout")
window.resize(300, 150)
lineEdit = QtWidgets.QLineEdit()
textEdit = QtWidgets.QTextEdit()
button1 = QtWidgets.QPushButton("О&тправить")
button2 = QtWidgets.QPushButton("О&чистить")
hbox = QtWidgets.QHBoxLayout()
hbox.addWidget(button1)
hbox.addWidget(button2)
form = QtWidgets.QFormLayout()
form.addRow("&Название:", lineEdit)
form.addRow("&Описание:", textEdit)
form.addRow(hbox)
window.setLayout(form)
window.show()
sys.exit(app.exec())