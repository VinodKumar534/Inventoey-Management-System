from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import sqlite3
class categoryClass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1060x532+203+137")
        self.root.title(" CATEGORY ")
        self.root.config(bg="lightgrey")
        self.root.focus_force()
#=============variabe=================
        
        self.var_cat_id=StringVar()
        self.var_name=StringVar()
        



        #===========title=========================
        lbl_title=Label(self.root,text="Manage Product Category ",font=("times new roman",25,"bold"),bg="#010c48",fg="white").pack(side=TOP,fill=X,padx=10,pady=2)
        lbl_name=Label(self.root,text="Enter Category Name",font=("goudy old style",20),bg="lightgrey").place(x=50,y=100)
        txt_name=Entry(self.root,textvariable=self.var_name,font=("times new roman",18),bg="lightyellow").place(x=50,y=170,width=300)
        btn_name=Button(self.root,text="Add",command=self.add,font=("times new roman",18),bg="#4caf50",fg="white",cursor="hand2").place(x=360,y=170,width=100,height=30)
        btn_name=Button(self.root,text="Delete",command=self.delete,font=("times new roman",18),bg="RED",fg="white",cursor="hand2").place(x=490,y=170,width=100,height=30)
        
        #===========Category Details=========================        
        
        cat_frame=Frame(self.root,bd=3,relief=RIDGE)
        cat_frame.place(x=630,y=100,width=452,height=100)
        scrolly=Scrollbar(cat_frame,orient=VERTICAL)
        scrollx=Scrollbar(cat_frame,orient=HORIZONTAL)
        
        self.categoryTable=ttk.Treeview(cat_frame,columns=("cid","name"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.categoryTable.xview)
        scrolly.config(command=self.categoryTable.yview)
        self.categoryTable.heading("cid",text="C ID")
        self.categoryTable.heading("name",text="Name")
        
        self.categoryTable["show"]="headings"

        self.categoryTable.column("cid",width=90)
        self.categoryTable.column("name",width=100)
        
        
        self.categoryTable.pack(fill=BOTH,expand=1)
        self.categoryTable.bind("<ButtonRelease-1>",self.get_data)





        self.im1=Image.open(r"C:\Users\ram\Desktop\Inventory\res\bg.ico")
        self.im1=self.im1.resize((500,250))
        self.im1=ImageTk.PhotoImage(self.im1)

        self.lbl_im1=Label(self.root,image=self.im1,bd=2,relief=RAISED)
        self.lbl_im1.place(x=50,y=220)

        self.im2=Image.open(r"C:\Users\ram\Desktop\Inventory\res\category.jpg")
        self.im2=self.im2.resize((500,250))
        self.im2=ImageTk.PhotoImage(self.im2)

        self.lbl_im2=Label(self.root,image=self.im2,bd=2,relief=RAISED)
        self.lbl_im2.place(x=580,y=220)
        self.show()
#=====================function========================================
    def add(self):
        con=sqlite3.connect(database=r"C:\Users\ram\Desktop\Inventory\vinod.db")
        cur=con.cursor()
        try:
            if self.var_name.get()=="":
                messagebox.showerror("Error","Category Name should be required",parent=self.root)
            else:
                cur.execute("Select * from category where name=?",(self.var_name.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","Category already assigned, try diffrent",parent=self.root)
                else:
                    cur.execute("Insert into category (name) values(?)",(self.var_name.get(),))
                    con.commit()
                    messagebox.showinfo("Success","Category Addeed Successfully",parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)

    def show(self):
        con=sqlite3.connect(database=r"C:\Users\ram\Desktop\Inventory\vinod.db")
        cur=con.cursor()
        try:
            cur.execute("select * from category ")
            rows=cur.fetchall()
            self.categoryTable.delete(*self.categoryTable.get_children())
            for row in rows:
                self.categoryTable.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)
            self.show()

    def get_data(self,ev):
        f=self.categoryTable.focus()
        content=(self.categoryTable.item(f))
        row=content["values"]
        #print(row)
        self.var_cat_id.set(row[0]),
        self.var_name.set(row[1]),
        self.show()
    
    def delete (self):
        con=sqlite3.connect(database=r"C:\Users\ram\Desktop\Inventory\vinod.db")
        cur=con.cursor()
        try:
            if self.var_cat_id.get()=="":
                messagebox.showerror("Error","Category Name Should be required",parent=self.root)
            else:
                cur.execute("Select * from category where cid=?",(self.var_cat_id.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Please Try Again. ",parent=self.root)
                else:
                    op=messagebox.askyesno("Confirm"," Do You really want to Delete ? ",parent=self.root)
                    if op==True:
                        cur.execute("Delete from category where cid=?",(self.var_cat_id.get(),))
                        con.commit()
                        messagebox.showinfo("Delete"," Category Deleted Successfully",parent=self.root)
                        self.show()

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)




if __name__=="__main__":     
    root=Tk()
    obj=categoryClass(root)
    root.mainloop()       