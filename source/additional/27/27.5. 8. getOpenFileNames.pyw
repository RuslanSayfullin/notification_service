from PyQt6 import QtCore, QtWidgets
import sys

def on_clicked():
    arr, l = QtWidgets.QFileDialog.getOpenFileNames(parent=window,
               caption="Заголовок окна", directory=QtCore.QDir.currentPath(),
               filter="All (*);;Images (*.png *.jpg)")
    print(arr)

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("Класс QFileDialog")
window.resize(300, 70)

button = QtWidgets.QPushButton("Отобразить диалоговое окно...")
button.clicked.connect(on_clicked)

box = QtWidgets.QVBoxLayout()
box.addWidget(button)
window.setLayout(box)
window.show()

sys.exit(app.exec())