from PyQt5.QtWidgets import *

import BAZA

def editwindow():
    window = QDialog()



    asdf = QLabel("Питання")
    asdf1 = QLabel("Правильна відповідь")
    asdf2 = QLabel("не правильна1")
    asdf3 = QLabel("не правльна2")
    asdf4 = QLabel("не правильна3")
    fdsa = QLineEdit()
    fdsa.setText(BAZA.qeust[BAZA.currentQuest]["питання"])
    fdsa1 = QLineEdit()
    fdsa1.setText(BAZA.qeust[BAZA.currentQuest]["Правильна відповідь"])
    fdsa2 = QLineEdit()
    fdsa2.setText(BAZA.qeust[BAZA.currentQuest]["не правильна1"])
    fdsa3 = QLineEdit()
    fdsa3.setText(BAZA.qeust[BAZA.currentQuest]["не правильна2"])
    fdsa4 = QLineEdit()
    fdsa4.setText(BAZA.qeust[BAZA.currentQuest]["не правильна3"])

    addBth = QPushButton("Добавити")
    mainLine = QVBoxLayout()
    def mama():
        BAZA.qeust[BAZA.currentQuest] = (
            {
                "питання": fdsa.text(),
                "Правильна відповідь": fdsa1.text(),
                "не правильна1": fdsa2.text(),
                "не правильна2": fdsa3.text(),
                "не правильна3": fdsa4.text()
            }
        )

    mainLine.addWidget(asdf)
    mainLine.addWidget(fdsa)
    mainLine.addWidget(asdf1)
    mainLine.addWidget(fdsa1)

    mainLine.addWidget(asdf2)
    mainLine.addWidget(fdsa2)
    mainLine.addWidget(asdf3)
    mainLine.addWidget(fdsa3)
    mainLine.addWidget(asdf4)
    mainLine.addWidget(fdsa4)
    mainLine.addWidget(addBth)
    addBth.clicked.connect(mama)
    window.setLayout(mainLine)
    window.show()
    window.exec()






