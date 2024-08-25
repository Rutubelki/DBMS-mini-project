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
class Cases_menu:
    def __init__(self,master):
        self.master = master
        self.master.title("Case management")
        self.master.geometry("1500x700+0+0")
        self.master.config(bg="#bcdbf7")
        self.frame = Frame(self.master,bg="#bcdbf7")
        self.frame.pack()

        #=============ATTRIBUTES===========
        # self.search_id_value = StringVar()  # StringVar for the search bar
        self.insert_status = StringVar()
        self.c_status=StringVar()
        self.c_no=StringVar()
        self.c_name=StringVar()
        self.ci_number=StringVar()
        self.plaintiff=StringVar()
        self.Defendant=StringVar()
        self.case_no=StringVar()
        self.ci_num=StringVar()
        self.c_status=StringVar()
        self.Department_id=StringVar()
        


        #===============TITLE==========
        self.lblTitle = Label(self.frame,text = "CASE RECORDS", font="Helvetica 20 bold",bg="#bcdbf7")
        self.lblTitle.grid(row =0 ,column = 0,columnspan=2,pady=50)
        #==============FRAME==========
        self.LoginFrame = Frame(self.frame,width=400,height=80,relief="ridge",bg="#4682b4",bd=9)
        self.LoginFrame.grid(row=2,column=0,pady=(0,15))
        
        self.LoginFrame1 = Frame(self.frame,width=300,height=20,relief="ridge",bg="#bcdbf7",bd=0)
        self.LoginFrame1.grid(row=1,column=0)

        self.LoginFrame2 = Frame(self.frame,width=400,height=80,relief="ridge",bg="#4682b4",bd=5)
        self.LoginFrame2.grid(row=2,column=0,pady=(420,0))
        #===========LABELS=============   
        self.search_id=Entry(self.LoginFrame1,font="Helvetica 14 bold",textvariable=self.c_no)
        self.search_id.grid(row=0,column=1,pady=(10,0))   
        self.search_button = Button(self.LoginFrame1, text="Search", command=self.search_case)
        self.search_button.grid(row=0, column=2, padx=10, pady=(10,0))   

        self.lblid = Label(self.LoginFrame,text="CASE NAME",font="Helvetica 14 bold",bg="#4682b4",bd=22)
        self.lblid.grid(row=1,column=0)
        self.lblid  = Entry(self.LoginFrame,font="Helvetica 14 bold",bd=2,textvariable= self.c_name)
        self.lblid.grid(row=1,column=1)
        
        self.lblfname = Label(self.LoginFrame,text="CASE NO",font="Helvetica 14 bold",bg="#4682b4",bd=22)
        self.lblfname.grid(row=2,column=0)
        self.lblfname  = Entry(self.LoginFrame,font="Helvetica 14 bold",bd=2,textvariable= self.c_no)
        self.lblfname.grid(row=2,column=1)

        self.lblLname = Label(self.LoginFrame,text="CASE STATUS",font="Helvetica 14 bold",bg="#4682b4",bd=22)
        self.lblLname.grid(row=3,column=0)
        self.lblLname  = Entry(self.LoginFrame,font="Helvetica 14 bold",bd=2,textvariable= self.c_status)
        self.lblLname.grid(row=3,column=1)

        self.lblage = Label(self.LoginFrame,text="DEPARTMENT ID",font="Helvetica 14 bold",bg="#4682b4",bd=22)
        self.lblage.grid(row=4,column=0)
        self.lblage  = Entry(self.LoginFrame,font="Helvetica 14 bold",bd=2,textvariable= self.Department_id)
        self.lblage.grid(row=4,column=1)
        
        self.address=Label(self.LoginFrame,text="PLAINTIFF NAME",font="Helvetica 14 bold",bg="#4682b4",bd=22)
        self.address.grid(row=5,column=0)
        self.address =Entry(self.LoginFrame,font="Helvetica 14 bold",bd=2,textvariable= self.plaintiff)
        self.address.grid(row=5,column=1)

        self.lblphone = Label(self.LoginFrame,text="CASE_INFO NUMBER",font="Helvetica 14 bold",bg="#4682b4",bd=22)
        self.lblphone.grid(row=1,column=2)
        self.lblphone = Entry(self.LoginFrame,font="Helvetica 14 bold",bd=2,textvariable= self.ci_number)
        self.lblphone.grid(row=1,column=3)
        
        self.lbldate = Label(self.LoginFrame,text="DEFENDANT NAME",font="Helvetica 14 bold",bg="#4682b4",bd=22)
        self.lbldate.grid(row=2,column=2)
        self.lbldate  = Entry(self.LoginFrame,font="Helvetica 14 bold",bd=2,textvariable= self.Defendant)
        self.lbldate.grid(row=2,column=3)
        
        # self.lbldept_id = Label(self.LoginFrame,text="DEPARTMENT ID",font="Helvetica 14 bold",bg="#4682b4",bd=22)
        # self.lbldept_id.grid(row=3,column=2)
        # self.lbldept_id  = Entry(self.LoginFrame,font="Helvetica 14 bold",bd=2,textvariable= self.Dept_id)
        # self.lbldept_id.grid(row=3,column=3)

        self.button1 = Button(self.LoginFrame2, text="SAVE",width =10,font="Helvetica 14 bold",bg="#4682b4",command = self.INSERT_CASE)
        self.button1.grid(row=4,column=1)
        
        self.button2 = Button(self.LoginFrame2, text="DELETE",width =10,font="Helvetica 14 bold",bg="#4682b4",command= self.DE_DISPLAY)
        self.button2.grid(row=4,column=2)

        self.button3 = Button(self.LoginFrame2, text="UPDATE",width =10,font="Helvetica 14 bold",bg="#4682b4",command = self.UPDATE_CASE)
        self.button3.grid(row=4,column=3)

        self.button4 = Button(self.LoginFrame2, text="EXIT",width =10,font="Helvetica 14 bold",bg="#4682b4",command = self.Exit)
        self.button4.grid(row=4,column=4)
        

   #FUNCTION TO EXIT PATIENT FORM
    def Exit(self):            
        self.master.destroy()
    
    def search_case(self):
        c2 = self.c_no.get()  # Get the case number from the GUI input
    
        try:
            conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='Rutu@007',
            database='police_dept'
        )
            my_cursor = conn.cursor()

            query = """
            SELECT 
            c.c_status, 
            c.c_no, 
            c.c_name, 
            c.Department_id, 
            ci.ci_number, 
            ci.plaintiff, 
            d.defendant
            FROM 
            cases c
            JOIN 
            case_information ci ON c.c_no = ci.case_no
            JOIN 
            c_defendant d ON ci.ci_number = d.ci_num
            WHERE 
            c.c_no = %s"""
        
            my_cursor.execute(query, (c2,))
            result = my_cursor.fetchone()

            if result:
            # If the case is found, populate the GUI fields with the retrieved data
                # self.search_id.set(result[1])
                self.c_status.set(result[0])
                self.case_no.set(result[1])
                self.c_name.set(result[2])
                self.Department_id.set(result[3])
                self.ci_number.set(result[4])
                self.plaintiff.set(result[5])
                self.Defendant.set(result[6])

                
                
                tkinter.messagebox.showinfo("Police Department Management System", "Case found.")
            else:
                tkinter.messagebox.showerror("Police Department Management System", "Case not found.")
            my_cursor.fetchall()

        except mysql.connector.Error as error:
            print("Error while fetching case data:", error)

        finally:
            if my_cursor:
                my_cursor.close()
            if conn:
                conn.close()
       


    #FUNCTION TO INSERT DATA IN EMPLOYEE FORM
        
    def INSERT_CASE(self):
        #global c1, c2, c3, c4, c5, c6, c7, c8, c9,c10,var
        c1 = self.c_status.get()
        c2 = self.c_no.get()
        c3 = self.c_name.get()
        c4 = self.ci_number.get()
        c5 = self.plaintiff.get()
        c6 = self.Defendant.get()
        c7 = self.c_status.get()
        c8 = self.Department_id.get()
        c9 = self.ci_num.get()
        c10=self.case_no.get()

        conn = mysql.connector.connect(host='localhost',
                user='root',
                password='Rutu@007',
                database='police_dept')   
        my_cursor=conn.cursor()
        my_cursor.execute("SELECT * FROM cases WHERE c_no= %s", (c2,))
        result = my_cursor.fetchall()
        if result:
            tkinter.messagebox.showerror("POLICE DEPARTMENT DATABASE SYSTEM", "CASE ALREADY EXISTS")
        else:
        # Insert new officer data into the database
            my_cursor.execute("INSERT INTO cases VALUES (%s,%s , %s, %s)", (c7, c2, c3, c8))
            my_cursor.execute("INSERT INTO case_information VALUES (%s,%s , %s)", (c4, c5, c2))
            my_cursor.execute("INSERT INTO c_defendant VALUES (%s,%s)", (c6, c4))
            tkinter.messagebox.showinfo("POLICE DEPARTMENT DATABASE SYSTEM", "CASE DATA ADDED")
        conn.commit()

    # Close database connection
        # conn.close()
    
    def UPDATE_CASE(self):
    # Retrieve data from entry fields
        c1 = self.c_status.get()
        c2 = self.c_no.get()
        c3 = self.c_name.get()
        c4 = self.ci_number.get()
        c5 = self.plaintiff.get()
        c6 = self.Defendant.get()
        c7 = self.c_status.get()
        c8 = self.Department_id.get()
        c9 = self.ci_num.get()
        c10 = self.case_no.get()
    
        try:
        # Connect to the database
            conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='Rutu@007',
            database='police_dept'
        )
            my_cursor = conn.cursor()

        # Execute SQL query to check if the case with the given case number exists
            my_cursor.execute("SELECT * FROM cases WHERE c_no= %s", (c2,))
            result = my_cursor.fetchone()

            if result:
            # Update the case's data in the cases table
                my_cursor.execute("UPDATE cases SET c_status=%s, c_name=%s, Department_id=%s WHERE c_no= %s", (c7, c3, c8, c2,))
            # Update the case's data in the case_information table
                my_cursor.execute("UPDATE case_information SET ci_number=%s, Plaintiff=%s WHERE ci_number= %s", (c4, c5, c4,))
            # Update the case's data in the c_defendant table
                my_cursor.execute("UPDATE c_defendant SET Defendant=%s WHERE ci_num= %s", (c6, c4,))
                tkinter.messagebox.showinfo("POLICE DEPARTMENT DATABASE SYSTEM", "CASE DATA UPDATED")
            else:
            # Show error message if the case does not exist
                tkinter.messagebox.showerror("POLICE DEPARTMENT DATABASE SYSTEM", "CASE NOT FOUND")

            conn.commit()

        except mysql.connector.Error as error:
            print("Error while updating case data:", error)
            tkinter.messagebox.showerror("POLICE DEPARTMENT DATABASE SYSTEM", "Error occurred while updating case data")

        finally:
            if my_cursor:
                my_cursor.close()
            if conn:
                conn.close()


                
    #FUNCTION TO OPEN DELETE PATIENT DISPLAY WINDOW
    def DE_DISPLAY(self):
        self.newWindow = Toplevel(self.master)
        self.app = D_officer(self.newWindow)


#CLASS FOR DISPLAY MENU FOR DELETE EMPLOYEE
class D_officer:
    def __init__(self,master):    
        global de1_case,de
        self.master = master
        self.master.title("POLICE DEPARTMENT MANAGEMENT SYSTEM")
        self.master.geometry("1500x700+0+0")
        self.master.config(bg="#bcdbf7")
        self.frame = Frame(self.master,bg="#bcdbf7")
        self.frame.pack()
        self.de1_case=StringVar()
        self.lblTitle = Label(self.frame,text = "DELETE CASE WINDOW", font="Helvetica 20 bold",bg="#bcdbf7")
        self.lblTitle.grid(row =0 ,column = 0,columnspan=2,pady=50)
        #==============FRAME==========
        self.LoginFrame = Frame(self.frame,width=400,height=80,relief="ridge",bg="#4682b4",bd=20)
        self.LoginFrame.grid(row=1,column=0)
        self.LoginFrame2 = Frame(self.frame,width=400,height=80,relief="ridge",bg="#4682b4",bd=20)
        self.LoginFrame2.grid(row=2,column=0)
        #===========LABELS=============          
        self.lbloffid = Label(self.LoginFrame,text="ENTER CASE NUMBER TO DELETE",font="Helvetica 14 bold",bg="#4682b4",bd=22)
        self.lbloffid.grid(row=0,column=0)
        self.lbloffid= Entry(self.LoginFrame,font="Helvetica 14 bold",bd=2,textvariable= self.de1_case)
        self.lbloffid.grid(row=0,column=1)

        self.DeleteB = Button(self.LoginFrame2, text="DELETE",width =10,font="Helvetica 14 bold",bg="#4682b4",command = self.DELETE_OFF)
        self.DeleteB.grid(row=3,column=1)
        
    #FUNCTION TO DELETE DATA IN EMPLOYEE FORM 
    def DELETE_OFF(self):        
        de = str(self.de1_case.get())
        conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='Rutu@007',
        database='police_dept'
        ) 
        my_cursor = conn.cursor()

        try:
        # Check if the case exists in the cases table
            my_cursor.execute("SELECT * FROM cases WHERE c_no = %s", (de,))
            result = my_cursor.fetchall()

            if result:
            # Delete the case from the cases table
                my_cursor.execute("DELETE FROM cases WHERE c_no = %s", (de,))
                print("Deleted case from cases table")

                tkinter.messagebox.showinfo("POLICE DEPARTMENT DATABASE SYSTEM", "CASE DATA DELETED")
            else:
                tkinter.messagebox.showerror("POLICE DEPARTMENT DATABASE SYSTEM", "CASE NOT FOUND")
        
        # Commit the transaction
            conn.commit()
        except mysql.connector.Error as error:
            print("Error:", error)
            tkinter.messagebox.showerror("POLICE DEPARTMENT DATABASE SYSTEM", "An error occurred while deleting the case.")
        finally:
        # Close database connection
            if my_cursor:
                my_cursor.close()
            if conn:
                conn.close()



    #update the officer details
    
def main():
    root = Tk()
    app = Cases_menu(root)
    root.mainloop()

if __name__ == "__main__":
    main()

