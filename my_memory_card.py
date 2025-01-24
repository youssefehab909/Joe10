from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QRadioButton , QApplication, QWidget, QLabel, QPushButton, QGroupBox, QVBoxLayout, QHBoxLayout

from random import shuffle , randint

class Questions():
    def __init__(self, question, rightAnswer, wrong1, wrong2, wrong3):
        self.question = question
        self.rightAnswer = rightAnswer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3
app =QApplication([])
main_win =QWidget()
main_win.setWindowTitle("Memory card")
Q = QLabel ("What is the capital of Egypt?")
QGroup = QGroupBox("Answer option")

r1 = QRadioButton("Cairo")
r2 = QRadioButton("Giza")
r3 = QRadioButton("Alex")
r4 = QRadioButton("Suez")
ans = QPushButton("Answer")

layout1 = QHBoxLayout()
layout2 = QVBoxLayout()
layout3 = QVBoxLayout()

layout2.addWidget(r1)
layout2.addWidget(r2)
layout3.addWidget(r3)
layout3.addWidget(r4)

layout1.addLayout(layout2)
layout1.addLayout(layout3)

QGroup.setLayout(layout1)

Mainlayout = QVBoxLayout()
Mainlayout.addWidget(Q)
Mainlayout.addWidget(QGroup)

ansgroup = QGroupBox("result")
result = QLabel("Correct")

anslayout = QVBoxLayout()
anslayout.addWidget(result)
ansgroup.setLayout(anslayout)

Mainlayout.addWidget(ansgroup)
Mainlayout.addWidget(ans)


ansgroup.hide()


def show_result():
    QGroup.hide()
    ansgroup.show()
    ans.setText("NEXT Question")

def show_question():
    QGroup.show()
    ansgroup.hide()
    ans.setText("Answer")
    
answers =[ r1, r2, r3, r4]
main_win.score = 0 
def test():
    if answers[0].isChecked():
        check_answer("correct")
        main_win.score +=1
    else:
        check_answer("incorrect")


def ask (q: Questions):
    shuffle(answers)
    answers[0].setText(q.rightAnswer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    Q.setText(q.question)
    result.setText(q.rightAnswer)
    show_question()

def check_answer(res):
    result.setText(res)
    show_result()

question_list = []
q1 = Questions("What is the capital of Egypt ?","Cairo","Giza","Alex","Suez" )
q2 = Questions("Who win the UEFA chapions league ?","Real Madrid","Bayern Manchen","Arsnel","Man city" )
q3 = Questions("Which Club is the best in Africa ?","AL Ahaly","Sundons","AL Wedad","EL Zamalk" )
q4 = Questions("Who is the graetest player of all time?","Cristiano ronaldo","Lional messi","pele","Ronaldinio" )
q5 = Questions("Who deserves to take the ballon dor this year?","Vini jounir","lamyen yamal","Belingham","Klian mppape")
q6 = Questions('who is the most skillful player ever?',"Ronaldinio", 'Cristiano ronaldo', 'Lional messi', 'Maradona')
q7 = Questions('who is the most player had scored goals?','Cristiano ronaldo', 'Lional messi', 'Van basten', 'Ronaldo nazario')
question_list.append(q1)
question_list.append(q2)
question_list.append(q3)
question_list.append(q4)
question_list.append(q5)
question_list.append(q6)
question_list.append(q7)

main_win.total = 1
def next_question():
    print
    print("total questions:", main_win.total)
    print
    print("correct questions:",main_win.score)
    print
    print("percentage:", main_win.score/main_win.total*100,"%")
    main_win.total += 1
    current_question = randint(0, len(question_list) - 1)      

    q = question_list[current_question]
    ask(q)

def click_ok():
    if ans.text() =="Answer":
        test()
    else:
        next_question()




ans.clicked.connect(click_ok)




main_win.setLayout(Mainlayout)
main_win.show()
app.exec_()