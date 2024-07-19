from PyQt6 import QtWidgets
import sys

# использование клласса QToolBox
app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("QToolBox")
window.resize(250, 100)
toolBox = QtWidgets.QToolBox()
toolBox.addItem(QtWidgets.QLabel("Содержимое вкладки 1"), "Вкладка &1")
toolBox.addItem(QtWidgets.QLabel("Содержимое вкладки 2"), "Вкладка &2")
toolBox.addItem(QtWidgets.QLabel("Содержимое вкладки 3"), "Вкладка &3")
toolBox.setCurrentIndex(0)
vbox = QtWidgets.QVBoxLayout()
vbox.addWidget(toolBox)
window.setLayout(vbox)
window.show()
sys.exit(app.exec())
