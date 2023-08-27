import random
from PyQt5.QtWidgets import *
import BAZA

app = QApplication([])
window = QWidget()

window.resize(500, 500)

mainLine = QVBoxLayout()

menuBth = QPushButton("Menu")
restBth = QPushButton("Відпочити")
timeSpn = QSpinBox()
timeLbl = QLabel("хвилин")
Apple = QPushButton("Відповісти")
Apple2 = QPushButton("Наступне питання")
Apple1 = QLabel("Яблуко")


firstLine = QHBoxLayout()
firstLine.addWidget(menuBth)
firstLine.addWidget(restBth)
firstLine.addWidget(timeSpn)
firstLine.addWidget(timeLbl)
mainLine.addLayout(firstLine)
qLine = QHBoxLayout()
qLine.addWidget(Apple1)

mainLine.addLayout(qLine)


answerGroups = QGroupBox("Введи правильну відповідь!")
answerLine = QVBoxLayout()
answer1 = QRadioButton("1")
answer2 = QRadioButton("2")
answer3 = QRadioButton("3")
answer4 = QRadioButton("4")
answers = [answer1, answer2, answer3, answer4]

answerLine.addWidget(answer1)
answerLine.addWidget(answer2)
answerLine.addWidget(answer3),
answerLine.addWidget(answer4)
answerGroups.setLayout(answerLine)
mainLine.addWidget(answerGroups)

result = QLabel("Результат")
answerLine.addWidget(result)
result.hide()

qwertyLine = QHBoxLayout()
qwertyLine.addWidget(Apple)
qwertyLine.addWidget(Apple2)
mainLine.addLayout(qwertyLine)

def setQuest():
    random.shuffle(answers)
    Apple1.setText(BAZA.quest[BAZA.currentQuest]["питання"])
    answers[0].setText(BAZA.quest[BAZA.currentQuest]["Правильна відповідь"])
    answers[1].setText(BAZA.quest[BAZA.currentQuest]["Правильна відповідь"])
    answers[2].setText(BAZA.quest[BAZA.currentQuest]["Правильна відповідь"])
    answers[3].setText(BAZA.quest[BAZA.currentQuest]["Правильна відповідь"])










setQuest()







def showResult():
    answers[0].hide()
    answers[1].hide()
    answers[2].hide()
    answers[3].hide()
    result.show()
    Apple2.show()
    Apple.hide()



Apple.clicked.connect(showResult)

window.setLayout(mainLine)
window.show()
app.exec()
