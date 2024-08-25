from tkinter import *
import tkinter.messagebox
from tkinter import ttk
from tkinter import font
import mysql.connector


conn = mysql.connector.connect(
                host='localhost',
                user='root',
                password='Rutu@007',
                database='police_dept'
            )
print("DATABASE CONNECTION SUCCESSFUL")

#Class for Officer registration 
class Officer:
    def __init__(self,master):
        self.master = master
        self.master.title("POLICE DEPARTMENT MANAGEMENT SYSTEM")
        self.master.geometry("1500x700+0+0")
        self.master.config(bg="#bcdbf7")
        self.frame = Frame(self.master,bg="#bcdbf7")
        self.frame.pack()

        #=============ATTRIBUTES===========
        
        self.Fname=StringVar()
        self.Lname=StringVar()
        self.age=IntVar()
        self.address=StringVar()
        self.id=IntVar()
        self.phone_no=StringVar()
        self.start_day=StringVar()
        self.Dept_id=IntVar()


        #===============TITLE==========
        self.lblTitle = Label(self.frame,text = "OFFICER REGISTRATION FORM", font="Helvetica 20 bold",bg="#bcdbf7")
        self.lblTitle.grid(row =0 ,column = 0,columnspan=2,pady=50)
        #==============FRAME==========
        self.LoginFrame = Frame(self.frame,width=400,height=80,relief="ridge",bg="#4682b4",bd=9)
        self.LoginFrame.grid(row=2,column=0,pady=(0,15))
        
        self.LoginFrame1 = Frame(self.frame,width=300,height=20,relief="ridge",bg="#bcdbf7",bd=0)
        self.LoginFrame1.grid(row=1,column=0)

        self.LoginFrame2 = Frame(self.frame,width=400,height=80,relief="ridge",bg="#4682b4",bd=5)
        self.LoginFrame2.grid(row=2,column=0,pady=(420,0))
        #===========LABELS=============   
        self.search_id=Entry(self.LoginFrame1,font="Helvetica 14 bold",textvariable=self.id)
        self.search_id.grid(row=0,column=1,pady=(10,0))   
        self.search_button = Button(self.LoginFrame1, text="Search", command=self.search_officer)
        self.search_button.grid(row=0, column=2, padx=10, pady=(10,0))   

        self.lblid = Label(self.LoginFrame,text="OFICER ID",font="Helvetica 14 bold",bg="#4682b4",bd=22)
        self.lblid.grid(row=1,column=0)
        self.lblid  = Entry(self.LoginFrame,font="Helvetica 14 bold",bd=2,textvariable= self.id)
        self.lblid.grid(row=1,column=1)
        
        self.lblfname = Label(self.LoginFrame,text="FIRST NAME",font="Helvetica 14 bold",bg="#4682b4",bd=22)
        self.lblfname.grid(row=2,column=0)
        self.lblfname  = Entry(self.LoginFrame,font="Helvetica 14 bold",bd=2,textvariable= self.Fname)
        self.lblfname.grid(row=2,column=1)

        self.lblLname = Label(self.LoginFrame,text="LAST NAME",font="Helvetica 14 bold",bg="#4682b4",bd=22)
        self.lblLname.grid(row=3,column=0)
        self.lblLname  = Entry(self.LoginFrame,font="Helvetica 14 bold",bd=2,textvariable= self.Lname)
        self.lblLname.grid(row=3,column=1)

        self.lblage = Label(self.LoginFrame,text="AGE",font="Helvetica 14 bold",bg="#4682b4",bd=22)
        self.lblage.grid(row=4,column=0)
        self.lblage  = Entry(self.LoginFrame,font="Helvetica 14 bold",bd=2,textvariable= self.age)
        self.lblage.grid(row=4,column=1)
        
        self.address=Label(self.LoginFrame,text="ADDRESS",font="Helvetica 14 bold",bg="#4682b4",bd=22)
        self.address.grid(row=5,column=0)
        self.address =Entry(self.LoginFrame,font="Helvetica 14 bold",bd=2,textvariable= self.address)
        self.address.grid(row=5,column=1)

        self.lblphone = Label(self.LoginFrame,text="PHONE NUMBER",font="Helvetica 14 bold",bg="#4682b4",bd=22)
        self.lblphone.grid(row=1,column=2)
        self.lblphone = Entry(self.LoginFrame,font="Helvetica 14 bold",bd=2,textvariable= self.phone_no)
        self.lblphone.grid(row=1,column=3)
        
        self.lbldate = Label(self.LoginFrame,text="START DATE",font="Helvetica 14 bold",bg="#4682b4",bd=22)
        self.lbldate.grid(row=2,column=2)
        self.lbldate  = Entry(self.LoginFrame,font="Helvetica 14 bold",bd=2,textvariable= self.start_day)
        self.lbldate.grid(row=2,column=3)
        
        self.lbldept_id = Label(self.LoginFrame,text="DEPARTMENT ID",font="Helvetica 14 bold",bg="#4682b4",bd=22)
        self.lbldept_id.grid(row=3,column=2)
        self.lbldept_id  = Entry(self.LoginFrame,font="Helvetica 14 bold",bd=2,textvariable= self.Dept_id)
        self.lbldept_id.grid(row=3,column=3)

        self.button1 = Button(self.LoginFrame2, text="SAVE",width =10,font="Helvetica 14 bold",bg="#4682b4",command = self.INSERT_OFF)
        self.button1.grid(row=4,column=1)
        
        self.button2 = Button(self.LoginFrame2, text="DELETE",width =10,font="Helvetica 14 bold",bg="#4682b4",command= self.DE_DISPLAY)
        self.button2.grid(row=4,column=2)

        self.button3 = Button(self.LoginFrame2, text="UPDATE",width =10,font="Helvetica 14 bold",bg="#4682b4",command = self.UPDATE_OFF)
        self.button3.grid(row=4,column=3)

        self.button4 = Button(self.LoginFrame2, text="EXIT",width =10,font="Helvetica 14 bold",bg="#4682b4",command = self.Exit)
        self.button4.grid(row=4,column=4)
        

   #FUNCTION TO EXIT PATIENT FORM
    def Exit(self):            
        self.master.destroy()
    
    def search_officer(self):
        # global e1,e2,e3,e4,e5,e6,e7,e8,var
        e5=(self.id.get())
        e1=(self.Fname.get())
        e2=(self.Lname.get())
        e3=(self.age.get())
        e4=(self.address.get())
        e6=(self.phone_no.get())
        e7=(self.start_day.get())
        e8=(self.Dept_id.get())
        print("Officer ID:",e5)  # Check if officer ID is retrieved correctly

        try:
            conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='Rutu@007',
            database='police_dept'
             )
            my_cursor = conn.cursor()
            my_cursor.execute("SELECT * FROM police_officer WHERE id = %s", (e5,))
            query = my_cursor.statement
            print("SQL Query:", query)  # Print SQL query for verification

            result = my_cursor.fetchone()
            print("Query Result:", result)  # Print query result

            if result:
                self.Fname.set(result[0])
                self.Lname.set(result[1])
                self.age.set(result[2])
                self.address.delete(0, END)  # Clear the current content
                self.address.insert(0, result[3])
                self.id.set(result[4])
                self.phone_no.set(result[5])
                self.start_day.set(result[6])
                self.Dept_id.set(result[7])
                tkinter.messagebox.showinfo("Police Department Management System", "Officer found.")
            else:
                tkinter.messagebox.showerror("Police Department Management System", "Officer not found.")

        except mysql.connector.Error as error:
            print("Error while fetching officer data:", error)

        finally:
            if my_cursor:
                my_cursor.close()
            if conn:
                conn.close()


    #FUNCTION TO INSERT DATA IN EMPLOYEE FORM
        
    def INSERT_OFF(self):
        # global e1,e2,e3,e4,e5,e6,e7,e8,var
        e5=(self.id.get())
        e1=(self.Fname.get())
        e2=(self.Lname.get())
        e3=(self.age.get())
        e4=(self.address.get())
        e6=(self.phone_no.get())
        e7=(self.start_day.get())
        e8=(self.Dept_id.get())

        conn = mysql.connector.connect(host='localhost',
                user='root',
                password='Rutu@007',
                database='police_dept')   
        my_cursor=conn.cursor()
        my_cursor.execute("SELECT * FROM police_officer WHERE id = %s", (e5,))
        result = my_cursor.fetchall()
        if result:
            tkinter.messagebox.showerror("POLICE DEPARTMENT DATABASE SYSTEM", "OFFICER ID ALREADY EXISTS")
        else:
        # Insert new officer data into the database
            my_cursor.execute("INSERT INTO police_officer VALUES (%s,%s , %s, %s, %s, %s, %s, %s)", (e1, e2, e3, e4, e5, e6, e7, e8,))
            tkinter.messagebox.showinfo("POLICE DEPARTMENT DATABASE SYSTEM", "OFFICER DATA ADDED")
        conn.commit()

    # Close database connection
        # conn.close()
    
    def UPDATE_OFF(self):
        global e1,e2,e3,e4,e5,e6,e7,e8,var
        e5=(self.id.get())
        e1=(self.Fname.get())
        e2=(self.Lname.get())
        e3=(self.age.get())
        e4=(self.address.get())
        e6=(self.phone_no.get())
        e7=(self.start_day.get())
        e8=(self.Dept_id.get())

    # Connect to the database
        conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='Rutu@007',
        database='police_dept')
        my_cursor = conn.cursor()

    # Execute SQL query to check if the officer with the given ID exists
        my_cursor.execute("SELECT * FROM police_officer WHERE id = %s", (e5,))
        result = my_cursor.fetchone()

        if result:
        # Update the officer's data
            my_cursor.execute("UPDATE police_officer SET fname = %s, lname = %s, age = %s, address = %s, phone_no = %s, start_day = %s, Dept_id = %s WHERE id = %s", (e1, e2, e3, e4, e6, e7, e8, e5,))
            tkinter.messagebox.showinfo("POLICE DEPARTMENT DATABASE SYSTEM", "OFFICER DATA UPDATED")
        else:
        # Show error message if the officer does not exist
            tkinter.messagebox.showerror("POLICE DEPARTMENT DATABASE SYSTEM", "OFFICER DATA INVALID")

        conn.commit()
    # Close database connection
        conn.close()


                
    #FUNCTION TO OPEN DELETE PATIENT DISPLAY WINDOW
    def DE_DISPLAY(self):
        self.newWindow = Toplevel(self.master)
        self.app = D_officer(self.newWindow)


#CLASS FOR DISPLAY MENU FOR DELETE EMPLOYEE
class D_officer:
    def __init__(self,master):    
        global de1_emp,de
        self.master = master
        self.master.title("POLICE DEPARTMENT MANAGEMENT SYSTEM")
        self.master.geometry("1500x700+0+0")
        self.master.config(bg="#bcdbf7")
        self.frame = Frame(self.master,bg="#bcdbf7")
        self.frame.pack()
        self.de1_emp=StringVar()
        self.lblTitle = Label(self.frame,text = "DELETE OFFICER WINDOW", font="Helvetica 20 bold",bg="#bcdbf7")
        self.lblTitle.grid(row =0 ,column = 0,columnspan=2,pady=50)
        #==============FRAME==========
        self.LoginFrame = Frame(self.frame,width=400,height=80,relief="ridge",bg="#4682b4",bd=20)
        self.LoginFrame.grid(row=1,column=0)
        self.LoginFrame2 = Frame(self.frame,width=400,height=80,relief="ridge",bg="#4682b4",bd=20)
        self.LoginFrame2.grid(row=2,column=0)
        #===========LABELS=============          
        self.lbloffid = Label(self.LoginFrame,text="ENTER OFFICER ID TO DELETE",font="Helvetica 14 bold",bg="#4682b4",bd=22)
        self.lbloffid.grid(row=0,column=0)
        self.lbloffid= Entry(self.LoginFrame,font="Helvetica 14 bold",bd=2,textvariable= self.de1_emp)
        self.lbloffid.grid(row=0,column=1)

        self.DeleteB = Button(self.LoginFrame2, text="DELETE",width =10,font="Helvetica 14 bold",bg="#4682b4",command = self.DELETE_OFF)
        self.DeleteB.grid(row=3,column=1)
        
    #FUNCTION TO DELETE DATA IN EMPLOYEE FORM 
    def DELETE_OFF(self):        
        global inp_d
        de = str(self.de1_emp.get())
        conn = mysql.connector.connect(host='localhost',
                user='root',
                password='Rutu@007',
                database='police_dept') 
        my_cursor=conn.cursor()
        my_cursor.execute("SELECT * FROM police_officer WHERE id = %s", (de,))
        result = my_cursor.fetchall()
        if result:
            my_cursor.execute("DELETE from police_officer where id=%s", (de,))
            tkinter.messagebox.showinfo("POLICE DEPARTMENT DATABASE SYSTEM", "OFFICER DATA DELETED")
            
        else:
        #Delete officer data from the database
            tkinter.messagebox.showerror("POLICE DEPARTMENT DATABASE SYSTEM", "OFFICER NOT FOUND")
        conn.commit()

    # Close database connection
        conn.close() 

    #update the officer details
    
def main():
    root = Tk()
    app = Officer(root)
    root.mainloop()

if __name__ == "__main__":
    main()

    
