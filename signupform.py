from tkinter import*
from tkinter import messagebox
import ast

window= Tk()
window.title("SignUp")
window.geometry('925x500+300+200')
window.configure(bg='#fff')
window.resizable(False,False)

def signup():
    email=mail.get()
    username=user.get()
    password=code.get()
    confirm_password=con_code.get()

    if (email=='E-mail' or email=='') or (username=='Username' or username=='')or (password=='Password' or password=='')or (confirm_password=='Confirm Password'or confirm_password==''):
        messagebox.showerror('ERROR','All fields are required' )
    elif password!=confirm_password:
        messagebox.showerror('Invalid','Both Password should match')
    else:
        messagebox.showinfo('Success','SignUp is successful')
    

def sign():
    window.destroy()




frame=Frame(window,width=350,height=400,bg='#fff')
frame.place(x=480,y=50)

heading=Label(frame,text='Sign up',fg='blue',bg='white',font=('Microsoft Yahei UI Light',23,'bold'))
heading.place(x=100,y=5)

def on_enter(e):
    if mail.get()=='E-mail':
        mail.delete(0,'end')
def on_leave(e):
    if mail.get()=='':
        mail.insert(0, 'E-mail')

mail = Entry(frame,width=25,fg='black',border=0,bg='white',font=('Microsoft Yahei UI Light',11))
mail.place(x=30,y=80)
mail.insert(0, 'E-mail')
mail.bind("<FocusIn>", on_enter)
mail.bind("<FocusOut>", on_leave)

Frame(frame,width=295,height=2,bg='black').place(x=25,y=100)



def on_enter(e):
    if user.get()=='Username':
        user.delete(0,'end')
def on_leave(e):
    if user.get()=='':
        user.insert(0, 'Username')

user = Entry(frame,width=25,fg='black',border=0,bg='white',font=('Microsoft Yahei UI Light',11))
user.place(x=30,y=130)
user.insert(0, 'Username')
user.bind("<FocusIn>", on_enter)
user.bind("<FocusOut>", on_leave)

Frame(frame,width=295,height=2,bg='black').place(x=25,y=150)



def on_enter(e):
    if code.get()=='Password':
        code.delete(0,'end')
def on_leave(e):
    if code.get()=='':
        code.insert(0, 'Password')

code = Entry(frame,width=25,fg='black',border=0,bg='white',font=('Microsoft Yahei UI Light',11))
code.place(x=30,y=180)
code.insert(0, 'Password')
code.bind("<FocusIn>", on_enter)
code.bind("<FocusOut>", on_leave)

Frame(frame,width=295,height=2,bg='black').place(x=25,y=200)


def on_enter(e):
    if con_code.get()=='Confirm Password':
        con_code.delete(0,'end')
def on_leave(e):
    if con_code.get()=='':
        con_code.insert(0, 'Confirm Password')

con_code = Entry(frame,width=25,fg='black',border=0,bg='white',font=('Microsoft Yahei UI Light',11))
con_code.place(x=30,y=230)
con_code.insert(0, 'Confirm Password')
con_code.bind("<FocusIn>", on_enter)
con_code.bind("<FocusOut>", on_leave)

Frame(frame,width=295,height=2,bg='black').place(x=25,y=250)

Button(frame,width=40,pady=7,text='Sign up',bg='blue',fg='white',border=0,command=signup).place(x=35,y=280)
label=Label(frame,text='Already have an account?',fg='black',bg='white',font=('Microsoft Yahei UI Light',9))
label.place(x=70,y=340)

signin=Button(frame,width=6,text='Sign in',border=0,bg='white',cursor='hand2',fg='blue',command=sign)
signin.place(x=220,y=340)

window.mainloop()