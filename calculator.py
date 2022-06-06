import math 
import sys
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QGridLayout,QTextEdit,QLineEdit,QMessageBox,QAction
from PyQt5.QtGui import QIcon
class Calculator(QWidget):
    
    def __init__(self):
      
        
        super().__init__()
        self.setUI()
    def setUI(self):
      
        
       
        self.btn1=QPushButton("x!",self)
        self.btn1.setStyleSheet("background-color: orange")
        self.btn1.move(5,20)
        self.btn1.resize(80,30)
        self.btn1.clicked.connect(self.fact)
        
        self.btn2=QPushButton("ln",self)
        self.btn2.setStyleSheet("background-color: orange")
        self.btn2.move(110,20)
        self.btn2.resize(80,30)
        self.btn2.clicked.connect(self.ln)
        
        self.btn3=QPushButton("EXP",self)
        self.btn3.setStyleSheet("background-color: orange")
        self.btn3.move(5,60)
        self.btn3.resize(80,30)
        self.btn3.clicked.connect(self.exp)
        
        
        self.btn4=QPushButton("sin",self)
        self.btn4.setStyleSheet("background-color: orange")
        self.btn4.move(110,60)
        self.btn4.resize(80,30)
        self.btn4.clicked.connect(self.sinn)
        
        self.btn5=QPushButton("cos",self)
        self.btn5.setStyleSheet("background-color: orange")
        self.btn5.move(5,100)
        self.btn5.resize(80,30)
        self.btn5.clicked.connect(self.coos)
        
        self.btn6=QPushButton("tan",self)
        self.btn6.setStyleSheet("background-color: orange")
        self.btn6.move(110,100)
        self.btn6.resize(80,30)
        self.btn6.clicked.connect(self.ttan)
        
        self.btn7=QPushButton("+",self)
        self.btn7.setStyleSheet("background-color: gray")
        self.btn7.move(300,20)
        self.btn7.resize(80,30)
        self.btn7.clicked.connect(self.plus)
        
        self.btn8=QPushButton("-",self)
        self.btn8.setStyleSheet("background-color: gray")
        self.btn8.move(300,60)
        self.btn8.resize(80,30)
        self.btn8.clicked.connect(self.moins)
        
        self.btn9=QPushButton("*",self)
        self.btn9.setStyleSheet("background-color: gray")
        self.btn9.move(230,20)
        self.btn9.resize(80,30)
        self.btn9.clicked.connect(self.fois)
        
        self.btn10=QPushButton("/",self)
        self.btn10.setStyleSheet("background-color: gray")
        self.btn10.move(230,60)
        self.btn10.resize(80,30)
        self.btn10.clicked.connect(self.div)
        
        self.btn11=QPushButton("=",self)
        self.btn11.move(260,100)
        self.btn11.resize(100,30)
        self.btn11.setStyleSheet("background-color: purple")
        self.btn11.clicked.connect(self.egal)
        
        self.btn12=QPushButton('CE',self)
        self.btn12.setStyleSheet("background-color: BLUE")
        self.btn12.clicked.connect(self.CE)
        
        self.btn12.resize(60,80)
        self.btn12.move(400,20)
       
      
        
        self.setGeometry(300,300,500,250)
        self.setWindowTitle('scientific calculator')
       
        self.textbox=QLineEdit(self)
        self.textbox.move(5,150)
        self.textbox.resize(400,50)
        self.text=self.textbox.text()
        
        
       
        
        
       
        self.show()
        
        #addition
    def plus(self):
        
        self.text=self.textbox.text()
        
        self.op =1
        self.l=float(self.text)
        self.sum=self.l
        self.textbox.setText('')
        
        #soustraction
    def moins(self):
        self.text=self.textbox.text()
        self.op =2
        self.l=float(self.text)
        self.sum=self.l
        self.textbox.setText('')
        
        #multiplication
    def fois(self):
        
        self.text=self.textbox.text()
        self.op =3
        self.l=float(self.text)
        self.sum=self.l
        
        
        self.textbox.setText('')

        
        #log
    def ln(self):
        
        text=self.textbox.text()
        self.op =5
    
        self.textbox.setText('')
        
        
        #factoriel
    def fact(self):
        
        text=self.textbox.text()
        self.op =6
        self.textbox.setText('')
        
        #SINUS
    def sinn(self):
        
        text=self.textbox.text()
        self.op =7
        self.textbox.setText('')

        
        #COS
    def coos(self):
        
        text=self.textbox.text()
        self.op =8
        self.textbox.setText('')
        
        #TG
    def ttan(self):
        
        text=self.textbox.text()
        self.op =9
        self.textbox.setText('')        
        
        #EXP
    def exp(self):
        self.op =10
        text=self.textbox.text()
        self.textbox.setText('')
        
        #DIVISION
    def div(self):
        
        text=self.textbox.text()
        
        self.text=self.textbox.text()
        self.op =4
        self.MU=float(self.text)
        self.sum=self.MU
        
        
        self.textbox.setText('+')
        
        
        #return null
    def CE(self):
        self.text=self.textbox.text()
        self.textbox.setText('0')
        self.op=0
        self.sum=0.0
        self.text2=''
        self.k=0.0
        self.l=0.0
    
        

        #result
    def egal(self):
        
        if(self.op==1):
            self.text2=self.textbox.text()
            self.k=float(self.text2)
            self.sum+=(self.k)
            self.textbox.setText(str(self.sum))
        if(self.op==2):
            
            self.text2=self.textbox.text()
            self.k=float(self.text2)
            self.sum=(self.sum) - (self.k)
            self.textbox.setText(str(self.sum))
            
        if(self.op==3):
            self.text2=self.textbox.text()
            self.k=float(self.text2)
            self.sum*=(self.k)
            self.textbox.setText(str(self.sum))
            
        if(self.op==4):
            self.text2=self.textbox.text()
            self.k=float(self.text2)
            self.sum/=(self.k)
            self.textbox.setText(str(self.sum))
        if(self.op==5):
            self.text2=self.textbox.text()
            self.k=float(self.text2)
            self.sum=math.log(self.k)
            self.textbox.setText(str(self.sum))
        if(self.op==6):
            self.text2=self.textbox.text()
            self.k=float(self.text2)
            self.sum=math.factorial(self.k)
            self.textbox.setText(str(self.sum))             
        if(self.op==7):
            self.text2=self.textbox.text()
            self.k=float(self.text2)
            self.sum=math.sin(self.k)
            self.textbox.setText(str(self.sum))            
        if(self.op==8):
            self.text2=self.textbox.text()
            self.k=float(self.text2)
            self.sum=math.cos(self.k)
            self.textbox.setText(str(self.sum))          
        if(self.op==9):
            self.text2=self.textbox.text()
            self.k=float(self.text2)
            self.sum=math.tan(self.k)
            self.textbox.setText(str(self.sum))      
        if(self.op==10):
            self.text2=self.textbox.text()
            self.k=float(self.text2)
            self.sum=math.exp(self.k)
            self.textbox.setText(str(self.sum))

    
       
        
        
if __name__ == '__main__':
    monApp=QApplication(sys.argv)
    fenetre=Calculator()
    sys.exit(monApp.exec_())
