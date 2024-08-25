import tkinter as tk
from tkinter import Toplevel, messagebox
import mysql.connector
from police_form import Officer
from Departments import Department_menu
from cases  import Cases_menu
class Menu:
    def __init__(self, master):
        self.master = master
        self.master.title("POLICE DEPARTMENT MANAGEMENT SYSTEM")
        self.master.geometry("800x600+0+0")
        self.master.config(bg="#bcdbf7")
        self.frame = tk.Frame(self.master, bg="#bcdbf7")
        self.frame.pack()
        
        self.lblTitle1 = tk.Label(self.frame, text="🚓 ""POLICE DEPARTMENT MANAGEMENT SYSTEM"" 🚓", font="Helvetica 22 bold", bg="#bcdbf7",fg="#0a1c2d")
        self.lblTitle1.grid(row=0, column=0, columnspan=4, pady=10)

        self.lblTitle = tk.Label(self.frame, text="MAIN MENU", font="Helvetica 20 bold", bg="#bcdbf7",fg="#0a1c2d")
        self.lblTitle.grid(row=3, column=1, columnspan=2, pady=(50,10),padx=(10,0))
        
        self.LoginFrame = tk.Frame(self.frame, width=400, height=80, relief="ridge", bg="#bcdbf7", bd=10)
        self.LoginFrame.grid(row=4, column=1,padx=(70,0),pady=(30,0))
        
        self.button1 = tk.Button(self.LoginFrame, text="1.POLICE OFFICER", width=30, font="Helvetica 14 bold", bg="#4682b4", command=self.police_form)       
        self.button1.grid(row=4, column=1, pady=10)
        
        self.button2 = tk.Button(self.LoginFrame, text="2.DEPARTMENT", width=30, font="Helvetica 14 bold", bg="#4682b4", command=self.Departments)
        self.button2.grid(row=7, column=1, pady=10)
        
        self.button3 = tk.Button(self.LoginFrame, text="3.CASES", width=30, font="Helvetica 14 bold", bg="#4682b4", command=self.cases)
        self.button3.grid(row=9, column=1, pady=10)
      
        self.button6 = tk.Button(self.LoginFrame, text="6.EXIT", width=30, font="Helvetica 14 bold", bg="#4682b4", command=self.Exit)
        self.button6.grid(row=12, column=1, pady=10)
        print("connecting to database")
        try:
            # Connect to the database
            self.connection = mysql.connector.connect(
                host='localhost',
                user='root',
                password='Rutu@007',
                database='police_dept'
            )
            print("DATABASE CONNECTION SUCCESSFUL")
        except mysql.connector.Error as err:
            print("ERROR: ", err)
            messagebox.showerror("Error", "Failed to connect to the database. Please check your credentials.")


    def Exit(self):
        self.connection.close()
        self.master.destroy()

    def police_form(self):
        self.newWindow=Toplevel(self.master)
        self.app=Officer(self.newWindow)
       

    def Departments(self):
        self.newWindow=Toplevel(self.master)
        self.app=Department_menu(self.newWindow)

    def cases(self):
        self.newWindow=Toplevel(self.master)
        self.app=Cases_menu(self.newWindow)

def main():
    root = tk.Tk()
    app = Menu(root)
    root.mainloop()

if __name__ == "__main__":
    main()


