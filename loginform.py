from tkinter import *
from tkinter import messagebox
import ast

root=Tk()
root.title('login')
root.geometry('925x500+300+200')
root.configure(bg="#fff")
root.resizable(False,False)

def signin():
    username=user.get()
    password=code.get()

    if (username=='' or username=='Username') or (password=='' or password=='Password'):
        messagebox.showerror('ERROR','All fields are required')
    elif username=='admin' and password=='admin':
        screen=Toplevel(root)
        screen.title("App")
        screen.geometry('925x500+300+200')
        screen.config(bg="white")

        Label(screen,text='Hello',bg='#fff',font=('Calibri(Body)',50,'bold')).pack(expand=True)
        screen.mainloop()
    elif username!='admin' and password!='admin':
        messagebox.showerror("Invalid","Invalid username and password")
    elif password!='admin':
        messagebox.showerror("Invalid","Invalid password")
    elif username!='admin':
        messagebox.showerror("Invalid","Invalid username ")

def signup():
    root.destroy()


frame=Frame(root,width=350,height=350,bg="white")
frame.place(x=480,y=70)

heading=Label(frame,text='Sign in',fg='blue',bg='white',font=('Microsoft YaHei UI Light',23,'bold'))
heading.place(x=100,y=5)

def on_enter(e):
    if user.get()== 'Username':
        user.delete(0, 'end')
def on_leave(e):
    if user.get()=='':
        user.insert(0, 'Username')


user = Entry(frame,width=25,fg='black',border=0,bg="white",font=('Microsoft YaHei UI Light',11))
user.place(x=30,y=80)
user.insert(0,'Username')
user.bind('<FocusIn>', on_enter)
user.bind('<FocusOut>', on_leave)
Frame(frame,width=295,height=2,bg='black').place(x=25,y=107)



def on_enter(e):
    if code.get()=='Password':
        code.delete(0, 'end')
def on_leave(e):
    if code.get()=='':
        code.insert(0, 'Password')


code = Entry(frame,width=25,fg='black',border=0,bg="white",font=('Microsoft YaHei UI Light',11))
code.place(x=30,y=150)
code.insert(0,'Password')
code.bind('<FocusIn>', on_enter)
code.bind('<FocusOut>', on_leave)

Frame(frame,width=295,height=2,bg='black').place(x=25,y=177)


Button(frame,width=40,pady=7,text='Sign in',bg='blue',fg='white',border=0,command=signin).place(x=35,y=204)
label=Label(frame,text="Dont have an account?",fg='black',bg='white',font=('Microsoft YaHei UI Light',9))
label.place(x=75,y=270)

sign_up= Button(frame,width=6,text='Sign up',border=0,bg='white',cursor='hand2',fg='blue',command=signup)
sign_up.place(x=215,y=270)


root.mainloop()