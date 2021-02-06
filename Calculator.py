from tkinter import *
from math import *
win = Tk() 
win.title("Calculator") # this title will be displayed on the top of the app
#win.geometry("300x400") # this defines the size of the app of window
input_box = StringVar() # It gets the contents of the entry box
e = Entry(win,width = 50,  borderwidth = 5, textvariable = input_box) # this defines the size of the entry box for user input
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10) # this displays the entry box on the top
expression = "" # Initiate the variable expression

def button_click(num): # this function generates expression when any button is clicked
    global expression
    expression = expression + str(num)
    input_box.set(expression)
    return

def Button_Clear(): # clears the contents of the entry box
    global expression
    expression = ""
    input_box.set(expression)
    return

def Button_Equal(): # evaluates the expression in the entr box and displays the result
    global expression
    result = str(eval(expression))
    round(result,2)
    expression = result
    input_box.set(expression)
    return

def Button_Factor():
    result = str(eval(expression))
    a=int(result)
    Factors=[]
    for i in range(1,a+1):
        if a% i==0:
            Factors.append(i)
            Factors.append(',')   
    e.insert(0,Factors)
    return
def Button_Fctrl():
    global expression
    result = str(eval(expression))
    num =int(result)
    factorial = 1
    if num == 0:
         e.insert(0,1)
    else:
        for i in range(1,num + 1):
           factorial = factorial*i
           e.delete(0,END)
           e.insert(0,factorial)
    expression = str(factorial)
    return
def Button_PrimeOrComposite():
    a = int(eval(e.get()))
    Button_Clear()
    factors = []
    for i in range(1,a+1):
            if a % i== 0:
                factors.append(a)
    if len(factors)==2:
        input_box.set("Is prime.")
    else:
        input_box.set("Is composite.")
    return

def Button_Abs(): 
    result = abs(eval(e.get()))
    e.delete(0,END)
    global expression
    expression = result
    input_box.set(expression)
    return

#Defining Buttons (what they should display and what they should do)
button_1 = Button(win, text="1", padx=40, pady=20, font=("Courier",11), fg='turquoise', bg='white', command = lambda: button_click(1))
button_2 = Button(win, text="2", padx=40, pady=20, font=("Arial",11), fg='purple', bg='white', command = lambda: button_click(2))
button_3 = Button(win, text="3", padx=40, pady=20, font=("Arial",11), fg='turquoise', bg='white', command = lambda: button_click(3))
button_4 = Button(win, text="4", padx=40, pady=20, font=("Arial",11), fg='purple', bg='white', command = lambda: button_click(4))
button_5 = Button(win, text="5", padx=40, pady=20, font=("Arial",11), fg='turquoise', bg='white', command = lambda: button_click(5))
button_6 = Button(win, text="6", padx=40, pady=20, font=("Arial",11), fg='purple', bg='white', command = lambda: button_click(6))
button_7 = Button(win, text="7", padx=40, pady=20, font=("Arial",11), fg='turquoise', bg='white', command = lambda: button_click(7))
button_8 = Button(win, text="8", padx=40, pady=20, font=("Arial",11), fg='purple', bg='white', command = lambda: button_click(8))
button_9 = Button(win, text="9", padx=40, pady=20, font=("Arial",11), fg='turquoise', bg='white', command = lambda: button_click(9))
button_0 = Button(win, text="0", padx=40, pady=20, font=("Arial",11), fg='purple', bg='white', command = lambda: button_click(0))
button_sum = Button(win, text="+", padx=40, pady=20, font=("Arial",11), fg='purple', bg='white', command = lambda: button_click('+'))
button_diff = Button(win, text="-", padx=40, pady=20, font=("Arial",11), fg='turquoise', bg='white', command = lambda: button_click('-'))
button_equal = Button(win, text="=", padx=40, pady=20, font=("Arial",11), fg='purple', bg='white', command = lambda: Button_Equal())
button_clear = Button(win, text="AC", padx=40, pady=20, font=("Arial",11), fg='purple', bg='white', command = lambda: Button_Clear())
button_mul = Button(win, text="*", padx=40, pady=20, font=("Arial",11), fg='purple', bg='white', command = lambda: button_click('*'))
button_div = Button(win, text="/", padx=40, pady=20, font=("Arial",11), fg='turquoise', bg='white', command = lambda: button_click('/'))
button_fac = Button(win, text=" factor", padx=40, pady=20, font=("Arial",11), fg='purple', bg='white', command = lambda: Button_Factor())
button_fctrl = Button(win, text="fctrl", padx=40, pady=20, font=("Arial",11), fg='turquoise', bg='white', command = lambda: Button_Fctrl())
button_bracket = Button(win, text="(", padx=40, pady=20, font=("Arial",11), fg='purple', bg='white', command = lambda: button_click("("))
button_bracket1 = Button(win, text=")", padx=40, pady=20, font=("Arial",11), fg='purple', bg='white', command = lambda: button_click(')'))
button_primeorcomp = Button(win, text="CheckPrime", padx=40, pady=20, font=("Arial",11), fg='turquoise', bg='white', command = lambda: Button_PrimeOrComposite())
button_abs = Button(win, text="Abs", padx=40, pady=20, font=("Arial",11), fg='purple', bg='white', command = lambda: Button_Abs())

#To display buttons
#The following code displays the buttons created
button_1.grid(row=1, column=0)
button_2.grid(row=1, column=1)
button_3.grid(row=1, column=2)
button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_7.grid(row=3, column=0)
button_8.grid(row=3, column=1)
button_9.grid(row=3, column=2)
button_0.grid(row=4, column=0)
button_sum.grid(row=2, column=3)
button_diff.grid(row=3, column=3)
button_equal.grid(row=4, column=2)
button_clear.grid(row=4, column=1)
button_mul.grid(row=1, column=3)
button_div.grid(row=4, column=3)
button_fac.grid(row=5, column=2)
button_bracket.grid(row=5, column=0)
button_bracket1.grid(row=5, column=1)
button_fctrl.grid(row=5, column=3)
button_primeorcomp.grid(row=6, column=0)
button_abs.grid(row=6, column=1)
win.mainloop()
