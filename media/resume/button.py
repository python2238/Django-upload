from tkinter import *
from tkinter import messagebox

class mybutton:
    def __init__(self, masterWindow):
        frame = Frame(masterWindow)
        frame.pack()
        self.button = Button(frame, text = "Exit" , bg= 'red',fg = 'white',command= quit,pady=5, padx=20, highlightcolor='gray')
        self.button.pack(side=LEFT)

        self.Click = Button(frame ,  bg = 'green', command=self.btn_action,  text="Click me",font='arial')
        self.Click.pack(side=RIGHT)

    def btn_action(self):
        print("Button Clicked!!!")
        messagebox.showinfo("Greetings","Thanks for click on the button")
root = Tk()
obj = mybutton(root)
root.mainloop()




# from tkinter import *
# win = Tk()
# btn = Button(win , text = "Button" , command = quit)
# btn.pack()
# win.mainloop()
