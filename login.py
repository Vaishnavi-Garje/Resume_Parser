from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import os
class Login:
    def __init__(self,root):
        self.root=root
        self.root.title("Login system")
        self.root.geometry("1199x600+100+50")
        self.root.resizable(False,False)
        self.bg=ImageTk.PhotoImage(file='images/e1.jpg')
        self.bg_image=Label(self.root,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)

        Frame_login=Frame(self.root,bg="white")
        Frame_login.place(x=330,y=100,width=550,height=480)
        title=Label(Frame_login,text="Login here", font=("impact",35,"bold"),fg="#6162FF",bg="white").place(x=170,y=30)
        subtitle=Label(Frame_login,text="Admin Login ", font=("Goudy old style",15,"bold"),fg="#1d1d1d",bg="white").place(x=220,y=100)
        #username
        lbl_user=Label(Frame_login,text="Username", font=("Goudy old style",15,"bold"),fg="grey",bg="white").place(x=98,y=140)
        self.username=Entry(Frame_login, font=("Goudy old style",15,"bold"),bg="#E7E6E6")
        self.username.place(x=98,y=170,width=320,height=35)

        #password
        lbl_password=Label(Frame_login,text="Password", font=("Goudy old style",15,"bold"),fg="grey",bg="white").place(x=98,y=210)
        self.password=Entry(Frame_login, font=("Goudy old style",15,"bold"),bg="#E7E6E6",show="*")
        self.password.place(x=98,y=240,width=320,height=35)

        #button
        submit=Button(Frame_login,command=self.check_function,text="login",bd=8,font=("Goudy old style",15,),bg="#6162FF",fg="white").place(x=190,y=320,width=180,height=40)

    def check_function(self):
        if self.username.get()=="" or self.password.get()=="":
            messagebox.showerror("Error","All the fields are required",parent=self.root)
        elif self.username.get()!="admin" or self.password.get()!="admin123":
            messagebox.showerror("Error","Invalid username or password",parent=self.root)
        else:
            
            messagebox.showinfo("Welcome",f"Welcome {self.username.get()}")
            os.system('project.py')
                
root=Tk()
obj=Login(root)
root.mainloop()
