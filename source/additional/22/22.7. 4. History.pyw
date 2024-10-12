from PyQt6 import QtCore, QtWidgets
import sys

def on_clicked():
    print("backwardHistoryCount", textBrowser.backwardHistoryCount())
    print("forwardHistoryCount", textBrowser.forwardHistoryCount())
    print("isBackwardAvailable", textBrowser.isBackwardAvailable())
    print("isForwardAvailable", textBrowser.isForwardAvailable())

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("Класс QTextBrowser")
window.resize(320, 320)
textBrowser = QtWidgets.QTextBrowser()
textBrowser.setSource(QtCore.QUrl("test.html"))
button = QtWidgets.QPushButton("Получить параметры списка истории")
button.clicked.connect(on_clicked)
button2 = QtWidgets.QPushButton("Назад")
button2.clicked.connect(textBrowser.backward)
button3 = QtWidgets.QPushButton("Вперед")
button3.clicked.connect(textBrowser.forward)
button4 = QtWidgets.QPushButton("Очистить список истории")
button4.clicked.connect(textBrowser.clearHistory)
box = QtWidgets.QVBoxLayout()
box.addWidget(textBrowser)
box.addWidget(button)
box.addWidget(button2)
box.addWidget(button3)
box.addWidget(button4)
window.setLayout(box)
window.show()
sys.exit(app.exec())