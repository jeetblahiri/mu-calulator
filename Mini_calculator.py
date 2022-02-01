from tkinter import *
from tkinter.messagebox import *
import webbrowser

#defining the font size and style
font = ("Times", '14')

#function for backspace key
def clear():
    cake = textField.get()
    cake = cake[0:len(cake) - 1]
    textField.delete(0, END)
    textField.insert(0, cake)

#define what AC button would do
def all_clear():
    textField.delete(0, END)

#defining the linkedin button hyperlink
def linkedin(event):
    webbrowser.open_new(r"https://www.linkedin.com/in/jeetblahiri/")


def clickbtn(event):
    b = event.widget
    text = b['text']
    print(text) 

    if text == 'x':
        textField.insert(END, '*') 
        return

    #error handling
    if text == '=': 
        try:
            ping = textField.get()
            answer = eval(ping)
            textField.delete(0, END)
            textField.insert(0, answer) #entering the result of calculation in text field
            return
        except Exception as e:
            print("Error...", e)
            showerror("Error", e)
        return
    textField.insert(END, text)

#creating a tkinter window for the calculator with all the required attributes

window = Tk()
window.title("Jeet's Calculator") 
window.geometry("290x320")
window.resizable(0, 0)
headingLabel = Label(window,
                     text="μ Calculator",
                     font="Cambria",
                     background='white',
                     foreground='indigo')

headingLabel.pack(side=TOP, pady=10)
window.configure(background='white')

#Creating a text bar for the input field
textField = Entry(window, font=font, justify="center",relief='solid')
textField.pack(side=TOP, pady=10, padx=6, fill=X)

buttonFrame = Frame(window)
buttonFrame.pack(side=TOP)

#Creating button for numbers 1-9 in a loop
temp = 1
for i in range(0, 3):
    for j in range(0, 3):
        btn = Button(buttonFrame,
                     text=str(temp),
                     font=font,
                     width=5,
                     relief="solid",
                     background='blue',
                     foreground='white',
                     activebackground='yellow',
                     activeforeground='black')
        btn.grid(row=i, column=j, pady=3, padx=3)
        temp += 1
        btn.bind('<Button-1>', clickbtn)

#Creating buttons for the all the basic operations
zerobtn = Button(buttonFrame,
                 text='0',
                 font=font,
                 width=5,
                 relief="solid",
                 background='blue',
                 foreground='white',
                 activebackground='yellow',
                 activeforeground='black')
zerobtn.grid(row=3, column=1, pady=3, padx=3)

dotbtn = Button(buttonFrame,
                text='.',
                font=font,
                width=5,
                relief="solid",
                background='black',
                foreground='white',
                activebackground='yellow',
                activeforeground='black')
dotbtn.grid(row=3, column=0, pady=3, padx=3)

backbtn = Button(buttonFrame,
                 text='←',
                 font=font,
                 width=5,
                 relief="solid",
                 background='black',
                 foreground='white',
                 activebackground='yellow',
                 activeforeground='black',
                 command=clear)
backbtn.grid(row=3, column=2, pady=3, padx=3)

plusbtn = Button(buttonFrame,
                 text='+',
                 font=font,
                 width=5,
                 relief="solid",
                 background='black',
                 foreground='white',
                 activebackground='yellow',
                 activeforeground='black')
plusbtn.grid(row=0, column=4, pady=3, padx=3)

minusbtn = Button(buttonFrame,
                  text='-',
                  font=font,
                  width=5,
                  relief="solid",
                  background='black',
                  foreground='white',
                  activebackground='yellow',
                  activeforeground='black')
minusbtn.grid(row=1, column=4, pady=3, padx=3)

multiplybtn = Button(buttonFrame,
                     text='x',
                     font=font,
                     width=5,
                     relief="solid",
                     background='black',
                     foreground='white',
                     activebackground='yellow',
                     activeforeground='black')
multiplybtn.grid(row=2, column=4, pady=3, padx=3)

dividebtn = Button(buttonFrame,
                   text='/',
                   font=font,
                   width=5,
                   relief="solid",
                   background='black',
                   foreground='white',
                   activebackground='yellow',
                   activeforeground='black')
dividebtn.grid(row=3, column=4, pady=3, padx=3)

clearbtn = Button(buttonFrame,
                  text='AC',
                  font=font,
                  width=5,
                  relief="solid",
                  background='black',
                  foreground='white',
                  activebackground='yellow',
                  activeforeground='black',
                  command=all_clear)
clearbtn.grid(row=4, column=2, columnspan=2)

equalbtn = Button(buttonFrame,
                  text='=',
                  font=font,
                  width=5,
                  relief="solid",
                  background='black',
                  foreground='white',
                  activebackground='yellow',
                  activeforeground='black')
equalbtn.grid(row=4, column=3, columnspan=2)

#a button to hyperlink my linkedin page
linkedinbtn = Button(buttonFrame,
                  text=r'Reach Me!',
                  font=font,
                  width=12,
                  relief="solid",
                  background='orange',
                  foreground='black',
                  activebackground='yellow',
                  activeforeground='black')
linkedinbtn.grid(row=4, column=0, columnspan=2)

#binding the buttons to execute their respective functions
dividebtn.bind('<Button-1>', clickbtn)
multiplybtn.bind('<Button-1>', clickbtn)
minusbtn.bind('<Button-1>', clickbtn)
plusbtn.bind('<Button-1>', clickbtn)
equalbtn.bind('<Button-1>', clickbtn)
dotbtn.bind('<Button-1>', clickbtn)
zerobtn.bind('<Button-1>', clickbtn)
linkedinbtn.bind('<Button-1>', linkedin)
#running the application
window.mainloop()
