from PyQt6 import QtWidgets
import sys

# Первая nроrрамма на PyQt6
app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("Пepвaя программа на PyQt")
window.resize(300, 70)
label = QtWidgets.QLabel("<center>Пpивeт, миp!</center>")
ЬtnQuit = QtWidgets.QPushButton("&Закрыть окно")
vbox = QtWidgets.QVBoxLayout()
vbox.addWidget(label)
vbox.addWidget(ЬtnQuit)
window.setLayout(vbox)
ЬtnQuit.clicked.connect(app.quit)
window.show()
sys.exit(app.exec())