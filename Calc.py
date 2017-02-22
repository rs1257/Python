from tkinter import *
'''
TO DO
work out dot
clear screen
display numbers entered somewhere else/calculation
'''

class MyFirstGUI:
    def __init__(self, master):
        self.master = master
        master.title("Calculator")

        self.screen = Frame(width=200, height=50, bg="black", colormap="new")
        self.screen.grid(row = 0)
        self.frame = Frame(width=200, height=50, bg="blue", colormap="new")
        self.frame.grid(row=1)
        self.T = Text(self.screen, height=1, width=10,font=("Helvetica",32))
        self.T.grid()
        self.number1 = 0
        self.number2 = 0
        self.result = 0
        self.intermediate = ""
        self.action = "-1"
        self.one = Button(self.frame, text="1", command=(lambda: getno(self,"1")), height=1, width=3, font=("Arial",20,"bold"))
        self.one.grid(row=1, column=0)
        self.two = Button(self.frame, text="2", command=(lambda: getno(self,"2")), height=1, width=3, font=("Arial",20,"bold"))
        self.two.grid(row=1, column=1)
        self.three = Button(self.frame, text="3", command=(lambda: getno(self,"3")), height=1, width=3, font=("Arial",20,"bold"))
        self.three.grid(row=1, column=2)
        self.divideb = Button(self.frame, text="/", command=(lambda: store(self, "/")), height=1, width=3, font=("Arial",20,"bold"))
        self.divideb.grid(row=1, column=3)
        self.four = Button(self.frame, text="4", command=(lambda: getno(self,"4")), height=1, width=3, font=("Arial",20,"bold"))
        self.four.grid(row=2, column=0)
        self.five = Button(self.frame, text="5", command=(lambda: getno(self,"5")), height=1, width=3, font=("Arial",20,"bold"))
        self.five.grid(row=2, column=1)
        self.six = Button(self.frame, text="6", command=(lambda: getno(self,"6")), height=1, width=3, font=("Arial",20,"bold"))
        self.six.grid(row=2, column=2)
        self.timesb = Button(self.frame, text="x", command=(lambda: store(self, "x")), height=1, width=3, font=("Arial",20,"bold"))
        self.timesb.grid(row=2, column=3)
        self.seven = Button(self.frame, text="7", command=(lambda: getno(self,"7")), height=1, width=3, font=("Arial",20,"bold"))
        self.seven.grid(row=3, column=0)
        self.eigth = Button(self.frame, text="8", command=(lambda: getno(self,"8")), height=1, width=3, font=("Arial",20,"bold"))
        self.eigth.grid(row=3, column=1)
        self.nine = Button(self.frame, text="9", command=(lambda: getno(self,"9")), height=1, width=3, font=("Arial",20,"bold"))
        self.nine.grid(row=3, column=2)
        self.minusb = Button(self.frame, text="-", command=(lambda: store(self, "-")), height=1, width=3, font=("Arial",20,"bold"))
        self.minusb.grid(row=3, column=3)
        self.dot = Button(self.frame, text=".", command=(lambda: store(self, ".")), height=1, width=3, font=("Arial",20,"bold"))
        self.dot.grid(row=4, column=0)
        self.zero = Button(self.frame, text="0", command=(lambda: getno(self,"0")), height=1, width=3, font=("Arial",20,"bold"))
        self.zero.grid(row=4, column=1)
        self.equalb = Button(self.frame, text="=", command=(lambda: final(self, self.action)), height=1, width=3, font=("Arial",20,"bold"))
        self.equalb.grid(row=4, column=2)
        self.plusb = Button(self.frame, text="+", command=(lambda: store(self, "+")), height=1, width=3, font=("Arial",20,"bold"))
        self.plusb.grid(row=4, column=3)   

    def setintermediate(self, number):
        self.intermediate += number

    def resetintermediate(self):
        self.intermediate = "" 

    def printintermediate(self):
        print (self.intermediate)          

    def answer(self):
        operation(action)

    def setresult(self, number):
        self.result = number

    def printresult(self):
        print (self.result)  

    def getno1(self):
        return self.number1

    def getno2(self):                    
        return self.number2

def getno(obj,number):
    obj.setintermediate(number)
    writetoscreen
    obj.printintermediate()

def store(obj, action):
    if obj.action == "/" or obj.action == "-" or obj.action == "x" or obj.action == "+":
        if obj.intermediate == "":
            obj.intermediate += "0"
        obj.number2 = int(obj.intermediate)
        obj.intermediate = "" 
    else:
        if obj.intermediate == "":
            obj.intermediate += "0"
        obj.number1 = int(obj.intermediate)
        obj.intermediate = ""    
    obj.action = action  

def final(obj, action):
    store(obj, action)
    #print ("1: " + str(obj.number1))
    #print ("2: " + str(obj.number2))
    if action == "/":
        if obj.getno2() == 0:
            number = "ERROR"
        else:    
            number = obj.getno1() / obj.getno2()
            print (number)
        obj.setresult(number) 
    elif action == "x": 
        number = obj.getno1() * obj.getno2()
        obj.setresult(number)  
    elif action == "-":
        number = obj.getno1() - obj.getno2()
        obj.setresult(number) 
    elif action == "+":
        number = obj.getno1() + obj.getno2()
        obj.setresult(number) 
    elif action == "-1":
        pass    
    else:
        obj.setresult("ERROR")
    print (obj.printresult())    

def writetoscreen(obj):
    obj.T.configure(state='normal')
    obj.T.delete(1.0, 'end')
    obj.T.insert('end', obj.result)
    obj.T.configure(state='disabled') 

def main():
    root = Tk()
    my_gui = MyFirstGUI(root)
    root.resizable(width=False, height=False)
    #root.after(0, writetoscreen(my_gui))
    #root.mainloop()
    while True:
        writetoscreen(my_gui)
        root.update_idletasks()
        root.update()

if __name__ == '__main__':
    main()    