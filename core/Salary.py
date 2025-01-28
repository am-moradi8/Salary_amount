from tkinter import *
from tkinter import messagebox

class Person():
    def __init__(self , firstname,lastname):
        self.firstname = firstname
        self.lastname = lastname
    
class Employee(Person):
    def __init__(self, firstname, lastname,hoursofwork,hourlywage):
        Person.__init__(self,firstname,lastname)

def salary_person ():
    salary = int(ent_salary.get())
    X= 0.15 * salary
    messagebox.showinfo('salary', X)
    return(X)

#form gui
win = Tk()
win.title("GUI")
win.geometry('500x250+500+200')
win.resizable(0,0)
win.config(bg='#E60004')
#label and entry
lbl_first_name = Label(win , text='first_name :',bg='#E60004',font='arial 12' )
lbl_first_name.place(x=5 , y=20)
ent_first_name = Entry(win) 
ent_first_name.place(x=100 , y=20)

lbl_last_name = Label(win , text='last_name :',bg='#E60004',font='arial 12' )
lbl_last_name.place(x=5 , y=100)
ent_last_name = Entry(win) 
ent_last_name.place(x=100 , y=100)

lbl_Percentage = Label(win , text='Percentage :',bg='#E60004',font='arial 12' )
lbl_Percentage.place(x=250 , y=20)
ent_Percentage = Entry(win) 
ent_Percentage.place(x=348 , y=20)

lbl_salary = Label(win , text='salary :',bg='#E60004',font='arial 12' )
lbl_salary.place(x=250 , y=100)
ent_salary = Entry(win) 
ent_salary.place(x=348, y=100)
#button
btn_showsalary = Button(win , text='show tax',command=salary_person)
btn_showsalary.place(x=220 , y=180)
win.mainloop()