from tkinter import *
import tkinter.messagebox
from tkinter import ttk
from tkinter import font

from police_dept import Menu


def main():
    root = Tk()
    app= MainWindow(root)
    root.mainloop()
#MAIN WINDOW FOR LOG IN
class MainWindow:
    # constructor
    def __init__(self,master):
        # public data mambers
        self.master = master
        self.master.title("POLICE DEPARTMENT MANAGEMENT SYSTEM")
        self.master.geometry("800x500+0+0")
        self.master.config(bg="#bcdbf7")
        self.frame = Frame(self.master,bg="#bcdbf7")
        self.frame.pack()

        
        self.Username = StringVar()
        self.Password = StringVar()

        self.lblTitle = Label(self.frame,text = "POLICE DEPARTMENT MANAGEMENT SYSTEM", font="Helvetica 20 bold",bg="#bcdbf7",fg="black")
        self.lblTitle.grid(row =0 ,column = 0,columnspan=2,pady=40)
        #======================
        self.LoginFrame1 = Frame(self.frame,width=400,height=80,relief="ridge",bg="#4682b4",bd=9)
        self.LoginFrame1.grid(row=1,column=0,padx=(70,0),pady=30)
        self.LoginFrame2 = Frame(self.frame,width=400,height=80,relief="ridge",bg="#4682b4",bd=5)
        self.LoginFrame2.grid(row=2,column=0,padx=(70,0))
        #======LABEL AND ENTRY=========
        self.lblUsername = Label(self.LoginFrame1,text="Username",font="Helvetica 14 bold",bg="#4682b4",bd=12)
        self.lblUsername.grid(row=0,column=0)
        self.lblUsername = Entry(self.LoginFrame1,font="Helvetica 14 bold",textvariable= self.Username,bd=2)
        self.lblUsername.grid(row=0,column=1)
        self.lblPassword = Label(self.LoginFrame1,text="Password ",font="Helvetica 14 bold",bg="#4682b4",bd=12)
        self.lblPassword .grid(row=1,column=0)
        self.lblPassword  = Entry(self.LoginFrame1,font="Helvetica 14 bold",show="*",textvariable= self.Password,bd=2)
        self.lblPassword .grid(row=1,column=1)
        #===========BUTTONS====
        self.btnLogin = Button(self.LoginFrame2,text = "Login" ,font="Helvetica 10 bold", width =10 ,bg="#bcdbf7",command = self.Login_system)
        self.btnLogin.grid(row=3,column=0)
        self.btnExit = Button(self.LoginFrame2,text = "Exit" ,font="Helvetica 10 bold", width =10 ,bg="#bcdbf7",command = self.Exit)
        self.btnExit.grid(row=3,column=1)
    # public member function  
    #Function for LOGIN
    def Login_system(self):

        S1=(self.Username.get())
        S2=(self.Password.get())
        if(S1=='admin' and S2=='1234'):
            self.newWindow = Toplevel(self.master)
            self.app = Menu(self.newWindow)
        elif(S1=='root' and S2=='4321'):
            self.newWindow = Toplevel(self.master)
            self.app = Menu(self.newWindow)
        else:
            tkinter.messagebox.askretrycancel("POLICE DEPARTMENT MANAGEMENT SYSTEM" , "PLEASE ENTER VALID USERNAME AND PASSWORD")
    #Function for Exit
    def Exit(self):
        self.master.destroy()




if __name__ == "__main__":
    main()
