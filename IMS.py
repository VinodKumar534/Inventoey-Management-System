from tkinter import*
from PIL import Image,ImageTk
from employee import employeeClass
from supplier import supplierClass
from category import categoryClass
from product import productClass
from sales import salesClass
import sqlite3
from tkinter import messagebox
import os
import time

class IMS:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.title(" INVENTORY MANAGEMENT SYSTEM  | Developed BY Vinod Kumar")
        self.root.config(bg="lightgrey")
        
        frame=Frame(width=1070,height=570,bg="lightgrey",bd=5,relief=GROOVE).place(x=200,y=102)
     
        # ***********************************Title***********************************
        self.icon_title=PhotoImage(file=r"C:\Users\ram\Desktop\Inventory\res\akshay-infrasya-logo.png")
        title=Label(self.root,text="         Inventory Management System ",image=self.icon_title,compound=LEFT,font=("times new roman",30,"bold"),bg="#010c48",fg="white",anchor="w",padx=20).place(x=0,y=0,relwidth=1,height=70)

        # *********************************BUTTON LOGOUT***********************************
        
        btn_logout=Button(self.root,command=self.logout,text=" Logout",font=("times new roman",15,"bold"),bg="yellow",cursor="hand2").place(x=1100,y=10,height=50,width=150)

        #***************************clock*************************************************
        self.lbl_clock=Label(self.root,text="Welcome To Inventory Management System\t\t Date :DD-MM-YYYY\t\t Time: HH:MM:SS",font=("times new roman",15,"bold"),bg="lightgrey",fg="black")
        self.lbl_clock.place(x=0,y=80,relwidth=1,height=15)

        #***************************Left Menu*************************************************
        self.MenuLogo=Image.open(r"C:\Users\ram\Downloads\pngwing.com (6).png")
        self.MenuLogo=self.MenuLogo.resize((200,200)    )
        self.MenuLogo=ImageTk.PhotoImage(self.MenuLogo)
        LeftMenu=Frame(self.root,bd=5,relief=RIDGE,bg="lightgrey")
        LeftMenu.place(x=0,y=102,width=200,height=575)
        lbl_menuLogo=Label(LeftMenu,image=self.MenuLogo)
        lbl_menuLogo.pack(side=TOP,fill=X)
        
        self.product_icon=PhotoImage(file=r"C:\Users\ram\Desktop\product.png")
        self.category_icon=PhotoImage(file=r"C:\Users\ram\Desktop\category.png")
        self.supplier_icon=PhotoImage(file=r"C:\Users\ram\Desktop\supplier.png")
        self.employe_icon=PhotoImage(file=r"C:\Users\ram\Desktop\employee.png")
        self.sales_icon=PhotoImage(file=r"C:\Users\ram\Desktop\sales.png")
        lbl_Menu=Label(LeftMenu,text=" Menu",font=("times new roman",20,"bold"),bg="#009688",bd=3).pack(side=TOP,fill=X)
        btn_employee=Button(LeftMenu,text="Employee",command=self.employee,image=self.employe_icon,compound=LEFT,padx=5,anchor="w",font=("times new roman",20),bg="lightgrey",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_supplier=Button(LeftMenu,text=" Supplier",command=self.supplier,image=self.supplier_icon,compound=LEFT,padx=5,anchor="w",font=("times new roman",20),bg="lightgrey",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_category=Button(LeftMenu,text=" Category",command=self.category,image=self.category_icon,compound=LEFT,padx=5,anchor="w",font=("times new roman",20),bg="lightgrey",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_product=Button(LeftMenu,text=" Product",command=self.product,image=self.product_icon,compound=LEFT,padx=5,anchor="w",font=("times new roman",20),bg="lightgrey",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_sales=Button(LeftMenu,text=" Sales",command=self.sales,image=self.sales_icon,compound=LEFT,padx=5,anchor="w",font=("times new roman",20),bg="lightgrey",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        self.int_side=PhotoImage(file=r"C:\Users\ram\Desktop\favpng_logo-inventory-stock-management.png")
        btn_exit=Button(LeftMenu,image=self.int_side,font=("times new roman",20,"bold"),bg="lightgrey",bd=3).pack(side=TOP,fill=X)

        #*************************content***************************
        self.lbl_employee=Label(self.root,text="TOTAL EMPLOYEE\n[ 0 ]",bd=2,relief=GROOVE,bg="#9B30FF",fg="white",font=("Calibri",20,"bold"))
        self.lbl_employee.place(x=250,y=120,width=300,height=150)
        self.lbl_supplier=Label(self.root,text="TOTAL SUPPLIER\n[ 0 ]",bd=2,relief=RIDGE,bg="#008B8B",fg="white",font=("Calibri",20,"bold"))
        self.lbl_supplier.place(x=600,y=120,width=300,height=150)
        self.lbl_category=Label(self.root,text="TOTAL CATEGORY\n[ 0 ]",bd=2,relief=RIDGE,bg="#FF8C00",fg="white",font=("Calibri",20,"bold"))
        self.lbl_category.place(x=950,y=120,width=300,height=150)
        self.lbl_product=Label(self.root,text="TOTAL PRODUCT\n[ 0 ]",bd=2,relief=RIDGE,bg="#FF69B4",fg="white",font=("Calibri",20,"bold"))
        self.lbl_product.place(x=250,y=300,width=300,height=150)
        self.lbl_sales=Label(self.root,text="TOTAL SALES\n[ 0 ]",bd=2,relief=RIDGE,bg="#00CD00",fg="white",font=("Calibri",20,"bold"))
        self.lbl_sales.place(x=600,y=300,width=300,height=150)

        
        self.update_content()
        #************footer*******************
        
        lbl_footer=Label(self.root,text="IMS- Inventory Management System | For Technical Issue-8851920472",font=("times new roman",15,"bold"),bg="lightgrey",bd=0,fg="black").pack(side=BOTTOM,fill=X)

        #****************************************************

    def employee(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=employeeClass(self.new_win)

    def supplier(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=supplierClass(self.new_win)
    
    def category(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=categoryClass(self.new_win)
        
    def product(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=productClass(self.new_win)

    def sales(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=salesClass(self.new_win)

    def update_content(self):
        con=sqlite3.connect(database=r"C:\Users\ram\Desktop\Inventory\vinod.db")
        cur=con.cursor()
        try:
            cur.execute("select * from product")
            product=cur.fetchall()
            self.lbl_product.config(text=f"TOTAL PRODUCT\n[ {str(len(product))} ]")

            cur.execute("select * from supplier")
            supplier=cur.fetchall()
            self.lbl_supplier.config(text=f"TOTAL SUPPLIER\n[ {str(len(supplier))} ]")

            cur.execute("select * from category")
            category=cur.fetchall()
            self.lbl_category.config(text=f"TOTAL CATEGORY\n[ {str(len(category))} ]")

            cur.execute("select * from employee")
            employee=cur.fetchall()
            self.lbl_employee.config(text=f"TOTAL EMPLOYEE\n[ {str(len(employee))} ]")

            bill=len(os.listdir("bill"))
            self.lbl_sales.config(text=f"TOTAL SALES\n [{str(bill)}]")

            time_=time.strftime("%I:%M:%S")
            date_=time.strftime("%d-%m-%Y")

            self.lbl_clock.config(text=f"Welcome To Inventory Management System\t\t Date :  {str(date_)}\t\t Time :  {str(time_)}")
            self.lbl_clock.after(200,self.update_content)

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)

    def logout(self):
        self.root.destroy()
        os.system("python login.py")






if __name__=="__main__": 
    root=Tk()
    obj=IMS(root)
    root.mainloop()