from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import sqlite3
class supplierClass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1060x532+203+137")
        self.root.title(" SUPPLIER DETAILS | ")
        self.root.config(bg="lightgrey")
        self.root.focus_force()

        #==========================
        # All Variables==========
        self.var_searchby=StringVar()
        self.var_searchtxt=StringVar()
        
        self.var_sup_invoice=StringVar()
        self.var_name=StringVar()
        self.var_contact=StringVar()
        self.var_desc=StringVar()
    
        
        


        #==============search frame==============================

        #===========option=============

        lbl_search=Label(self.root,text="Search By Invoice No.",bg="lightgrey",font=("goudy old style",15))
        lbl_search.place(x=700,y=80)
      

        txt_search=Entry(self.root,textvariable=self.var_searchtxt,font=("goudy old style",15),bg="lightyellow").place(x=890,y=80,width=180)
        btn_search=Button(self.root,text="Search",command=self.search,font=("goudy old style",15),bg="orange",fg="white").place(x=1090,y=80,width=90,height=30)
        
        #========title==================
        title=Label(self.root,text=" Manage Supplier Details",font=("goudy old style",20,"bold"),bg="#0f4d7d",fg="white").place(x=50,y=10,width=1100,height=40)

        #========content==================
        
        #====== Row_1 ================

        lbl_supplier_invoice=Label(self.root,text="Invoice.No. ",font=("goudy old style",14),bg="lightgrey").place(x=50,y=100)
        txt_supplier_invoice=Entry(self.root,textvariable=self.var_sup_invoice,font=("goudy old style",15),bg="lightyellow").place(x=180,y=100,width=180)
        

        #====== Row_2 ================
        lbl_name=Label(self.root,text="Name",font=("goudy old style",14),bg="lightgrey").place(x=50,y=180)
        txt_name=Entry(self.root,textvariable=self.var_name,font=("goudy old style",15),bg="lightyellow").place(x=180,y=190,width=220)
       
        #=========Row_3 ===========

        lbl_contact=Label(self.root,text="Contact",font=("goudy old style",14),bg="lightgrey").place(x=50,y=230)
        txt_contact=Entry(self.root,textvariable=self.var_contact,font=("goudy old style",15),bg="lightyellow").place(x=180,y=230,width=220)
        

        #=========Row_4 ===========

        lbl_desc=Label(self.root,text="Description",font=("goudy old style",14),bg="lightgrey").place(x=50,y=280)
        self.txt_desc=Text(self.root,font=("goudy old style",14),bg="lightyellow")
        self.txt_desc.place(x=180,y=280,width=480,height=165)
        


        #============button============
        btn_add=Button(self.root,text="Save",command=self.add,font=("goudy old style",15),bg="#2196f3",fg="white",cursor="hand2").place(x=180,y=480,width=100,height=28)
        btn_update=Button(self.root,text="Update",command=self.update,font=("goudy old style",15),bg="#4caf50",fg="white",cursor="hand2").place(x=305,y=480,width=100,height=28)
        btn_delete=Button(self.root,text="Delete",command=self.delete,font=("goudy old style",15),bg="#f44336",fg="white",cursor="hand2").place(x=435,y=480,width=100,height=28)
        btn_clear=Button(self.root,text="Clear",command=self.clear,font=("goudy old style",15),bg="#607b8b",fg="white",cursor="hand2").place(x=563,y=480,width=100,height=28)

         #============Employee Details ============

        sup_frame=Frame(self.root,bd=3,relief=RIDGE)
        sup_frame.place(x=700,y=130,width=480,height=380)
        scrolly=Scrollbar(sup_frame,orient=VERTICAL)
        scrollx=Scrollbar(sup_frame,orient=HORIZONTAL)
        

        self.SupplierTable=ttk.Treeview(sup_frame,columns=("invoice","name","contact","desc"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.SupplierTable.xview)
        scrolly.config(command=self.SupplierTable.yview)
        self.SupplierTable.heading("invoice",text="Invoice No")
        self.SupplierTable.heading("name",text="Supplier Name")
        self.SupplierTable.heading("contact",text="Contact No")
        self.SupplierTable.heading("desc",text="Description")
        
        self.SupplierTable["show"]="headings"

        self.SupplierTable.column("invoice",width=90)
        self.SupplierTable.column("name",width=100)
        self.SupplierTable.column("contact",width=100)
        self.SupplierTable.column("desc",width=100)
        
        self.SupplierTable.pack(fill=BOTH,expand=1)
        self.SupplierTable.bind("<ButtonRelease-1>",self.get_data)

        self.show()

        #==========================================================

    def add(self):
        con=sqlite3.connect(database=r"C:\Users\ram\Desktop\Inventory\vinod.db")
        cur=con.cursor()
        try:
            if self.var_sup_invoice.get()=="":
                messagebox.showerror("Error","Invoice No. required",parent=self.root)
            else:
                cur.execute("Select * from supplier where invoice=?",(self.var_sup_invoice.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","Invoice already assigned, try diffrent",parent=self.root)
                else:
                    cur.execute("insert into supplier (invoice,name,contact,desc) values(?,?,?,?)",(
                                        self.var_sup_invoice.get(),
                                        self.var_name.get(),
                                        self.var_contact.get(),
                                        self.txt_desc.get('1.0',END),
                                        
                                        
                     ))
                    con.commit()
                    messagebox.showinfo("Success","Supplier Addeed Successfully",parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)
            
    def show(self):
        con=sqlite3.connect(database=r"C:\Users\ram\Desktop\Inventory\vinod.db")
        cur=con.cursor()
        try:
            cur.execute("select * from supplier ")
            rows=cur.fetchall()
            self.search.delete(*self.SupplierTable.get_children())
            for row in rows:
                self.SupplierTable.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)

    def get_data(self,ev):
        f=self.SupplierTable.focus()
        content=(self.SupplierTable.item(f))
        row=content["values"]
        #print(row)
        self.var_sup_invoice.set(row[0]),
        self.var_name.set(row[1]),
        self.var_contact.set(row[2]),
      
        self.txt_desc.delete('1.0',END),
        self.txt_desc.insert(END,row[3]),
       

    def update(self):
        con=sqlite3.connect(database=r"C:\Users\ram\Desktop\Inventory\vinod.db")
        cur=con.cursor()
        try:
            if self.var_sup_invoice.get()=="":
                messagebox.showerror("Error","Invoice No. Must be required",parent=self.root)
            else:
                cur.execute("Select * from supplier where invoice=?",(self.var_sup_invoice.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid Invoice No. ",parent=self.root)
                else:
                    cur.execute("Update supplier set name=?,contact=?,desc=? where invoice=?",(
                                        
                                                self.var_name.get(),
                                                self.var_contact.get(),
                                                self.txt_desc.get('1.0',END),
                                                self.var_sup_invoice.get(),
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Supplier Udated Successfully",parent=self.root)
                    self.show()
                   
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)
   
    def show(self):
        con=sqlite3.connect(database=r"C:\Users\ram\Desktop\Inventory\vinod.db")
        cur=con.cursor()
        try:
            cur.execute("select * from supplier ")
            rows=cur.fetchall()
            self.SupplierTable.delete(*self.SupplierTable.get_children())
            for row in rows:
                self.SupplierTable.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)
    
    
    def delete (self):
        con=sqlite3.connect(database=r"C:\Users\ram\Desktop\Inventory\vinod.db")
        cur=con.cursor()
        try:
            if self.var_sup_invoice.get()=="":
                messagebox.showerror("Error","Invoice No. be required",parent=self.root)
            else:
                cur.execute("Select * from supplier where invoice=?",(self.var_sup_invoice.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid Invoice No. ",parent=self.root)
                else:
                    op=messagebox.askyesno("Confirm"," Do You really want to Delete ? ",parent=self.root)
                    if op==True:
                        cur.execute("Delete from supplier where invoice=?",(self.var_sup_invoice.get(),))
                        con.commit()
                        messagebox.showinfo("Delete"," Supplier Deleted Successfully",parent=self.root)
                        self.show()

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)

    def clear(self):
        self.var_sup_invoice.set(""),
        self.var_name.set(""),
        self.var_contact.set(""),
        self.txt_desc.delete('1.0',END),
        self.var_searchtxt.set("")
        
        self.show()



    def search (self):
        con=sqlite3.connect(database=r"C:\Users\ram\Desktop\Inventory\vinod.db")
        cur=con.cursor()
        try:
            if self.var_searchtxt.get()=="":
               messagebox.showerror("Error","invoice No. should be required",parent=self.root)

            else:
              cur.execute("select * from supplier where invoice=?",(self.var_searchtxt.get(),))
              row=cur.fetchone()
              if row!=None:
                    self.SupplierTable.delete(*self.SupplierTable.get_children())
                    self.SupplierTable.insert('',END,values=row)
              else:
                  messagebox.showerror("Error", " No Record Found !!!",parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)



if __name__=="__main__": 
    root=Tk()
    obj=supplierClass(root)
    root.mainloop()    