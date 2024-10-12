from PyQt6 import QtWidgets, QtGui
import sys

def on_expanded(ind):
    print("on_expanded", ind.data())

def on_collapsed(ind):
    print("on_collapsed", ind.data())

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("Класс QTreeView")
window.resize(500, 400)
view = QtWidgets.QTreeView()

model = QtGui.QStandardItemModel()
model.setColumnCount(4)
parent = model.invisibleRootItem()
for i in range(0, 4):
    item = QtGui.QStandardItem("Пункт {0}-1".format(i))
    parent.appendRow(item)
    parent = item

parent = QtGui.QStandardItem(3, 4)
parent.setText("Элемент-родитель")
for row in range(0, 3):
    for column in range(0, 4):
        item = QtGui.QStandardItem("({0}, {1})".format(row, column))
        parent.setChild(row, column, item)
model.appendRow(parent)

view.setModel(model)

view.expanded["QModelIndex"].connect(on_expanded)
view.collapsed["QModelIndex"].connect(on_collapsed)

box = QtWidgets.QVBoxLayout()
box.addWidget(view)
window.setLayout(box)
window.show()
sys.exit(app.exec())