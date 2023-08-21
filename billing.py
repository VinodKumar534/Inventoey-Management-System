from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import sqlite3
import time
import os
import tempfile
class BillClass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.title(" INVENTORY MANAGEMENT SYSTEM  | Developed BY Vinod Kumar")
        self.root.config(bg="lightgrey")
        self.cart_list=[]
        self.chk_print=0
        # ***********************************Title***********************************
        self.icon_title=PhotoImage(file=r"C:\Users\ram\Desktop\Inventory\res\akshay-infrasya-logo.png")
        title=Label(self.root,text="      Inventory Management System ",image=self.icon_title,compound=LEFT,font=("times new roman",30,"bold"),bg="#010c48",fg="white",anchor="w",padx=20).place(x=0,y=0,relwidth=1,height=70)

        # *********************************BUTTON LOGOUT***********************************
        
        btn_logout=Button(self.root,text=" Logout",command=self.logout,font=("times new roman",17,"bold"),bd=5,bg="yellow",cursor="hand2",relief=GROOVE).place(x=1100,y=10,height=50,width=150)

        #***************************clock*************************************************
        self.lbl_clock=Label(self.root,text="Welcome To Inventory Management System\t\t Date :DD-MM-YYYY\t\t Time: HH:MM:SS",font=("times new roman",15,"bold"),bg="lightgrey",fg="black")
        self.lbl_clock.place(x=0,y=80,relwidth=1,height=15)

        #========================Product Frame===========================================
        
        
        
        
        ProductFrame1=Frame(self.root,bd=4,relief=RIDGE)
        ProductFrame1.place(x=6,y=110,width=410,height=550)


        pTitle=Label(ProductFrame1,text="All Products",font=("times new roman",15,"bold"),bg="#262626",fg="white").pack(side=TOP,fill=X)

        #============ Product Search Frame ===================
        
        self.var_search=StringVar()
        
        ProductFrame2=Frame(ProductFrame1,bd=4,bg="white",relief=RIDGE)
        ProductFrame2.place(x=2,y=42,width=398,height=90)

        lbl_search=Label(ProductFrame2,text="Search Product | By Name",font=("times new roman",15),bg="white",fg="green").place(x=2,y=5)
        lbl_search=Label(ProductFrame2,text="Product Name",font=("times new roman",15,),bg="white").place(x=2,y=40)
        lbl_text=Entry(ProductFrame2,textvariable=self.var_search,font=("times new roman",15,),bg="lightyellow").place(x=128,y=47,width=150,height=22)
        btn_search=Button(ProductFrame2,text="Search",command=self.search,font=("goudy old style",15),bg="#00688B",fg="white",cursor="hand2").place(x=290,y=47,width=90,height=22)
        btn_show_all=Button(ProductFrame2,text="Show All",command=self.show,font=("goudy old style",15),bg="#FF7D40",fg="white",cursor="hand2").place(x=290,y=10,width=90,height=22)

        #============Product Details Frame ============

        ProductFrame3=Frame(ProductFrame1,bd=3,relief=RIDGE)
        ProductFrame3.place(x=2,y=140,width=398,height=375)
        scrolly=Scrollbar(ProductFrame3,orient=VERTICAL)
        scrollx=Scrollbar(ProductFrame3,orient=HORIZONTAL)
        

        self.product_Table=ttk.Treeview(ProductFrame3,columns=("pid","name","price","qty","status"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.product_Table.xview)
        scrolly.config(command=self.product_Table.yview)
        self.product_Table.heading("pid",text="P ID ")
        self.product_Table.heading("name",text="Product Name")
        self.product_Table.heading("price",text="Price")
        self.product_Table.heading("qty",text="QTY")
        self.product_Table.heading("status",text="Status")
        
        self.product_Table["show"]="headings"

        self.product_Table.column("pid",width=30)
        self.product_Table.column("name",width=140)
        self.product_Table.column("price",width=60)
        self.product_Table.column("qty",width=30)
        self.product_Table.column("status",width=60)
        self.product_Table.pack(fill=BOTH,expand=1)
        self.product_Table.bind("<ButtonRelease-1>",self.get_data)
        lbl_note=Label(ProductFrame1,text="Note : Enter 0 Qunantity to remove product from the Cart",font=("goudy old style",11,"bold"),bg="white",fg="red").pack(side=BOTTOM,fill=X)


        #===================Customer Frame============================================
        self.var_cname=StringVar()
        self.var_contact=StringVar()


        CustomerFrame=Frame(self.root,bd=4,relief=RIDGE,bg="white")
        CustomerFrame.place(x=420,y=110,width=530,height=70)
        cTitle=Label(CustomerFrame,text="Customer Details",font=("times new roman",15,"bold"),bg="lightgrey").pack(side=TOP,fill=X)
        lbl_name=Label(CustomerFrame,text="Name ",font=("times new roman",15,),bg="white").place(x=2,y=30)
        lbl_name=Entry(CustomerFrame,textvariable=self.var_cname,font=("times new roman",13,"bold"),bg="lightyellow").place(x=80,y=35,width=150)

        lbl_contact=Label(CustomerFrame,text="Contact No",font=("times new roman",15),bg="white").place(x=250,y=30)
        lbl_contact=Entry(CustomerFrame,textvariable=self.var_contact,font=("times new roman",13,"bold"),bg="lightyellow").place(x=360,y=35,width=150)

        #============ cal card Frame ===================

        Cal_cartFrame=Frame(self.root,bd=4,relief=RIDGE,bg="white")
        Cal_cartFrame.place(x=420,y=190,width=530,height=360)

         #============ calclulator Frame ===================
        self.var_cal_input=StringVar()
        
        Cal_Frame=Frame(Cal_cartFrame,bd=9,relief=RIDGE,bg="white")
        Cal_Frame.place(x=5,y=10,width=270,height=340)
        txt_cal_input=Entry(Cal_Frame,textvariable=self.var_cal_input,font=("arial",15,"bold"),width=21,bd=10,relief=GROOVE,state="readonly",justify=RIGHT)
        txt_cal_input.grid(row=0,columnspan=4)
        btn_7=Button(Cal_Frame,text="7",font=("arial",15,"bold"),command=lambda:self.get_input(7),bd=5,width=4,pady=10,cursor="hand2").grid(row=1,column=0)
        btn_8=Button(Cal_Frame,text="8",font=("arial",15,"bold"),command=lambda:self.get_input(8),bd=5,width=4,pady=10,cursor="hand2").grid(row=1,column=1)
        btn_9=Button(Cal_Frame,text="9",font=("arial",15,"bold"),command=lambda:self.get_input(9),bd=5,width=4,pady=10,cursor="hand2").grid(row=1,column=2)
        btn_sum=Button(Cal_Frame,text="+" ,font=("arial",15,"bold"),command=lambda:self.get_input("+"),bd=5,width=4,pady=10,cursor="hand2").grid(row=1,column=3)

        btn_4=Button(Cal_Frame,text="4",font=("arial",15,"bold"),command=lambda:self.get_input(4),bd=5,width=4,pady=10,cursor="hand2").grid(row=2,column=0)
        btn_5=Button(Cal_Frame,text="5",font=("arial",15,"bold"),command=lambda:self.get_input(5),bd=5,width=4,pady=10,cursor="hand2").grid(row=2,column=1)
        btn_6=Button(Cal_Frame,text="6",font=("arial",15,"bold"),command=lambda:self.get_input(6),bd=5,width=4,pady=10,cursor="hand2").grid(row=2,column=2)
        btn_sub=Button(Cal_Frame,text="-" ,font=("arial",15,"bold"),command=lambda:self.get_input("-"),bd=5,width=4,pady=10,cursor="hand2").grid(row=2,column=3)

        btn_3=Button(Cal_Frame,text="1",font=("arial",15,"bold"),command=lambda:self.get_input(1),bd=5,width=4,pady=10,cursor="hand2").grid(row=3,column=0)
        btn_2=Button(Cal_Frame,text="2",font=("arial",15,"bold"),command=lambda:self.get_input(2),bd=5,width=4,pady=10,cursor="hand2").grid(row=3,column=1)
        btn_1=Button(Cal_Frame,text="3",font=("arial",15,"bold"),command=lambda:self.get_input(3),bd=5,width=4,pady=10,cursor="hand2").grid(row=3,column=2)
        btn_mul=Button(Cal_Frame,text="*" ,font=("arial",15,"bold"),command=lambda:self.get_input("*"),bd=5,width=4,pady=10,cursor="hand2").grid(row=3,column=3)
        
        btn_0=Button(Cal_Frame,text="0",font=("arial",15,"bold"),command=lambda:self.get_input(0),bd=5,width=4,pady=13,cursor="hand2").grid(row=4,column=0)
        btn_c=Button(Cal_Frame,text="C",font=("arial",15,"bold"),command=self.Clear,bd=5,width=4,pady=13,cursor="hand2").grid(row=4,column=1)
        btn_eq=Button(Cal_Frame,text="=",font=("arial",15,"bold"),command=self.perform_cal,bd=5,width=4,pady=13,cursor="hand2").grid(row=4,column=2)
        btn_div=Button(Cal_Frame,text="/",font=("arial",15,"bold"),command=lambda:self.get_input("/"),bd=5,width=4,pady=13,cursor="hand2").grid(row=4,column=3)
        
        
        
        
        
        
        
        
        
        
        #============ Card Frame ===================
       
        
        CartFrame=Frame(Cal_cartFrame,bd=3,relief=RIDGE)
        CartFrame.place(x=270,y=8,width=250,height=342)
        self.cartTitle=Label(CartFrame,text="Cart\t  Total Product: [0]",font=("times new roman",15),bg="lightgrey")
        self.cartTitle.pack(side=TOP,fill=X)
        scrolly=Scrollbar(CartFrame,orient=VERTICAL)
        scrollx=Scrollbar(CartFrame,orient=HORIZONTAL)
        

        self.CartTable=ttk.Treeview(CartFrame,columns=("pid","name","price","qty"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.CartTable.xview)
        scrolly.config(command=self.CartTable.yview)
        self.CartTable.heading("pid",text="P ID ")
        self.CartTable.heading("name",text="Product Name")
        self.CartTable.heading("price",text="Price")
        self.CartTable.heading("qty",text="QTY")
        
        
        self.CartTable["show"]="headings"

        self.CartTable.column("pid",width=40)
        self.CartTable.column("name",width=120)
        self.CartTable.column("price",width=90)
        self.CartTable.column("qty",width=40)
        
        self.CartTable.pack(fill=BOTH,expand=1)
        self.CartTable.bind("<ButtonRelease-1>",self.get_data_cart)

       
       #============Add Card  widgets Frame===================
        self.var_pid=StringVar()
        self.var_pname=StringVar()
        self.var_price=StringVar()
        self.var_qty=StringVar()
        self.var_stock=StringVar()


       
        Add_CartWidgetsFrame=Frame(self.root,bd=4,relief=RIDGE,bg="white")
        Add_CartWidgetsFrame.place(x=420,y=550,width=530,height=110)

        lbl_P_name=Label(Add_CartWidgetsFrame,text="Product Name",font=("times new roman",15),bg="white").place(x=5,y=5)
        txt_P_name=Entry(Add_CartWidgetsFrame,textvariable=self.var_pname,font=("times new roman",15),bg="lightyellow",state="readonly").place(x=5,y=35,width=190,height=22)

        lbl_P_price=Label(Add_CartWidgetsFrame,text="Price Per Qty",font=("times new roman",15),bg="white").place(x=220,y=5)
        txt_P_price=Entry(Add_CartWidgetsFrame,textvariable=self.var_price,font=("times new roman",15),bg="lightyellow",state="readonly").place(x=220,y=35,width=150,height=22)

        lbl_P_qty=Label(Add_CartWidgetsFrame,text="Quantity",font=("times new roman",15),bg="white").place(x=390,y=5)
        txt_P_qty=Entry(Add_CartWidgetsFrame,textvariable=self.var_qty,font=("times new roman",15),bg="lightyellow").place(x=390,y=35,width=100,height=22)

        self.lbl_inStock=Label(Add_CartWidgetsFrame,text="In Stock",font=("times new roman",15),bg="white")
        self.lbl_inStock.place(x=5,y=70)
        
        txt_P_name=Entry(Add_CartWidgetsFrame,textvariable=self.var_pname,font=("times new roman",15),bg="lightyellow",state="readonly").place(x=5,y=35,width=190,height=22)
        
        btn_clear=Button(Add_CartWidgetsFrame,text="Clear",command=self.clear_cart,font=("times new roman",15),bg="lightgrey",cursor="hand2").place(x=220,y=72,width=100,height=22)
        btn_add_card=Button(Add_CartWidgetsFrame,text="Add Update | Card",command=self.add_update_card,font=("times new roman",15),bg="green",fg="white",cursor="hand2").place(x=350,y=72,width=160,height=22)


        #============================Customer Bill Area ============================================
        
        billFrame=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        billFrame.place(x=953,y=110,width=315,height=435)
        
        custTitle=Label(billFrame,text="Customer Bill Area",font=("times new roman",15,"bold"),bg="#8B475D",fg="white").pack(side=TOP,fill=X)
        scrolly=Scrollbar(billFrame,orient=VERTICAL)
        scrolly.pack(side=RIGHT,fill=Y)
        
        self.txt_bill_area=Text(billFrame,yscrollcommand=scrolly.set)
        self.txt_bill_area.pack(fill=BOTH,expand=1)
        scrolly.config(command=self.txt_bill_area.yview)

        #============================Customer Bill Area ============================================

        billMenuFrame=Frame(self.root,bd=4,relief=RIDGE,bg="white")
        billMenuFrame.place(x=953,y=520,width=315,height=140)

        self.lbl_amnt=Label(billMenuFrame,text="Bill Amt\n[0]",font=("goudy old style",15,"bold"),bd=2,bg="#00688B",fg="white")
        self.lbl_amnt.place(x=2,y=5,width=100,height=70)
       
        self.lbl_discount=Label(billMenuFrame,text="Discount\n[5%]",font=("goudy old style",15,"bold"),bd=2,bg="#228B22",fg="white")
        self.lbl_discount.place(x=104,y=5,width=100,height=70)
       
        self.lbl_net_pay=Label(billMenuFrame,text="Net Pay\n[0]",font=("goudy old style",15,"bold"),bd=2,bg="#8B4513",fg="white")
        self.lbl_net_pay.place(x=206,y=5,width=100,height=70)


        btn_print=Button(billMenuFrame,text="Print",font=("goudy old style",15,"bold"),bd=5,command=self.print_bill,bg="#FFE4C4",fg="black",cursor="hand2")
        btn_print.place(x=2,y=77,width=100,height=53)
       
        btn_clear=Button(billMenuFrame,text="Clear all",command=self.clear_all,font=("goudy old style",15,"bold"),bd=5,bg="#FFF8DC",fg="black",cursor="hand2")
        btn_clear.place(x=104,y=78,width=100,height=53)
       
        btn_genrate=Button(billMenuFrame,text="Gen Bill",command=self.generate_bill,font=("goudy old style",15,"bold"),bd=5,bg="#8FBC8F",fg="black",cursor="hand2")
        btn_genrate.place(x=206,y=79,width=100,height=53)


        self.show()
        #self.bill_top()
        self.update_date_time()
        #============================ All Fubctions ============================================

    def get_input(self,num):
            xnum=self.var_cal_input.get()+str(num)
            self.var_cal_input.set(xnum)
    def Clear(self):
            self.var_cal_input.set("")
    
    def perform_cal(self):
       result=self.var_cal_input.get()
       self.var_cal_input.set(eval(result))

    def show(self):
        con=sqlite3.connect(database=r"C:\Users\ram\Desktop\Inventory\vinod.db")
        cur=con.cursor()
        try:
            cur.execute("select pid,name,price,qty,status from product where status= 'Active' ")
            rows=cur.fetchall()
            self.product_Table.delete(*self.product_Table.get_children())
            for row in rows:
                self.product_Table.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)

    def search (self):
        con=sqlite3.connect(database=r"C:\Users\ram\Desktop\Inventory\vinod.db")
        cur=con.cursor()
        try:
            
            if self.var_search.get()=="":
                messagebox.showerror("Error","Search input should be required",parent=self.root)

            else:
              cur.execute("select pid,name,price,qty,status from product where name LIKE  '%" +self.var_search.get()+"%' and status='Active'")
              rows=cur.fetchall()
              if len(rows)!=0:
                    self.product_Table.delete(*self.product_Table.get_children())
                    for row in rows:
                        self.product_Table.insert('',END,values=row)
              else:
                  messagebox.showerror("Error", " No Record Found !!!",parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)

    def get_data(self,ev):
        f=self.product_Table.focus()
        content=(self.product_Table.item(f))
        row=content["values"]
        self.var_pid.set(row[0])
        self.var_pname.set(row[1])
        self.var_price.set(row[2])
        self.lbl_inStock.config(text=f"In Stock[{str(row[3])}]")
        self.var_stock.set(row[3])
        self.var_qty.set("1")


    def get_data_cart(self,ev):
        f=self.CartTable.focus()
        content=(self.CartTable.item(f))
        row=content["values"]
        self.var_pid.set(row[0])
        self.var_pname.set(row[1])
        self.var_price.set(row[2])
        self.var_qty.set(row[3])
        self.lbl_inStock.config(text=f"In Stock[{str(row[4])}]")
        self.var_stock.set(row[4])
        



    def add_update_card(self):
        
        if self.var_pid.get()=="":
            messagebox.showerror("Error","Please Select Product from the List",parent=self.root)
        
        elif self.var_qty.get()=="":
            messagebox.showerror("Error","Quantity is Required",parent=self.root)
        elif int(self.var_qty.get()) > int(self.var_stock.get()):
            messagebox.showerror("Error","Quantity More than Stock",parent=self.root)
        else:
            #price_cal=int(self.var_qty.get())*float(self.var_price.get())
            #price_cal=float(price_cal)
            price_cal=self.var_price.get()
            cart_data=[self.var_pid.get(),self.var_pname.get(),price_cal,self.var_qty.get(),self.var_stock.get()]
            
            self.show_cart()
    
    #=============================== Update card ============================================
            present="no"
            index_=0
            for row in self.cart_list:
                if self.var_pid.get()==row[0]:
                    present="yes"
                    break
                index_+=1
            if present=="yes":
                op=messagebox.askyesno("Confirm","The Product already present \n Do you want to Update | or Remove from the Cart list",parent=self.root)
                if op==True:
                    if self.var_qty.get()=="0":
                        self.cart_list.pop(index_)
                    else:
                        #self.cart_list[index_][2]=price_cal
                        self.cart_list[index_][3]=self.var_qty.get()
            else:
                    self.cart_list.append(cart_data)
            self.show_cart()
            self.bill_updates()
    
    def bill_updates(self):
        self.bill_amnt=0
        self.net_pay=0
        self.discount=0
        for row in self.cart_list:
            self.bill_amnt=self.bill_amnt+(float(row[2])*int(row[3]))
            self.discount=(self.bill_amnt*5)/100                           
            self.net_pay=self.bill_amnt-self.discount
            self.lbl_amnt.config(text=f"Bill Amt\n{str(self.bill_amnt)}")
            self.lbl_net_pay.config(text=f"Net Pay\n{str(self.net_pay)}")
            self.cartTitle.config(text=f"Cart\t  Total Product: [{str(len(self.cart_list))}]")
    
    
    
    
    def show_cart(self):
        
        try:
            self.CartTable.delete(*self.CartTable.get_children())
            for row in self.cart_list:
                self.CartTable.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)
        
    def generate_bill(self):
        if self.var_cname.get()=="" or self.var_contact.get()=="":
            messagebox.showerror("Error",f"Customer Details Are Required ",parent=self.root)
        elif len(self.cart_list)==0:
            messagebox.showerror("Error",f"Please Add Product to the Card ",parent=self.root)
        else:
            #============== Bill Top =============
           self.bill_top()
            #============== Bill Mid =============
           self.bill_middle()
            #============== Bill Bottom =============
           self.bill_bottom()

           fp=open(f"bill/{str(self.invoice)}.txt","w")
           fp.write(self.txt_bill_area.get("1.0",END))
           fp.close()
           messagebox.showinfo("Saved","Bill Has Been Generated/Save in Backend",parent=self.root)
           self.chk_print=1

        
         
         
         #============== End Gretings =============
          
        pass
    
    def bill_top(self):
        self.invoice=int(time.strftime("%H%M%S"))+int(time.strftime("%d%M%Y"))
        bill_top_temp=f'''
\t    AKSHAY INFRASYS\n\t     CUSTOMER BILL\n
Phone No.8851920472  \tJaipur-125001\n
{str("="*36)}\n
Customer Name    :     {self.var_cname.get()}\n
Mobile No        :     {self.var_contact.get()}\n
Bill No : {str(self.invoice)}  Date: {str(time.strftime('%d/%m/%Y'))}\n
{str("="*36)}
Product Name\t          QTY     price
{str("="*36)}'''
        self.txt_bill_area.delete("1.0",END)
        self.txt_bill_area.insert("1.0",bill_top_temp)
        


    def bill_bottom(self):
        bill_bottom_temp=f"""
{str("="*36)}       
Bill Amount\t\t\tRs.{self.bill_amnt}
Bill Discount\t\t\tRs.{self.discount}
Net Pay\t\t\tRs.{self.net_pay}
{str("="*36)}
    Thanks For Visiting Here !!!

    """
        self.txt_bill_area.insert(END,bill_bottom_temp)

    
     
    
    
    
    def bill_middle(self):
        con=sqlite3.connect(database=r"C:\Users\ram\Desktop\Inventory\vinod.db")
        cur=con.cursor()
        try:
            for row in self.cart_list:
                
                pid=row[0]
                name=row[1]
                qty=int(row[4])-int(row[3])
                if int(row[3])==int(row[4]):
                    status="Inactive"
                if int(row[3])!=int(row[4]):
                    status="Active"
                
                price=float(row[2])*int(row[3])
                price=str(price)
                self.txt_bill_area.insert(END,"\n"+name+"\t\t\t"+row[3]+"   "+price)
    #======================== Update qty in product =====================================
                cur.execute("Update Product set qty=?,status=? where pid=?",(
                    qty,
                    status,
                    pid
                ))  
                con.commit()
            con.close()
            self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)


    def clear_cart(self):
        self.var_pid.set("")
        self.var_pname.set("")
        self.var_price.set("")
        self.var_qty.set("")
        self.lbl_inStock.config(text=f"In Stock")
        self.var_stock.set("")


    def clear_all(self):
        del self.cart_list[:]
        self.var_cname.set("")
        self.var_contact.set("")
        self.txt_bill_area.delete("1.0",END)
        self.cartTitle.config(text=f"Cart\t  Total Product: [0]")
        self.var_search.set("")
        self.clear_cart()
        self.show()
        self.show_cart()

    def update_date_time(self):
        time_=time.strftime("%I:%M:%S")
        date_=time.strftime("%d-%m-%Y")

        self.lbl_clock.config(text=f"Welcome To Inventory Management System\t\t Date :  {str(date_)}\t\t Time :  {str(time_)}")
        self.lbl_clock.after(200,self.update_date_time)

    def print_bill(self):
        if self.chk_print==1:
            messagebox.showinfo("Print","Please Wait While Printing",parent=self.root)
            new_file=tempfile.mktemp(".txt")
            open(new_file,"w").write(self.txt_bill_area.get("1.0",END))
            os.startfile(new_file,"Print")
        else:
             messagebox.showerror("Error ","Please Generate Bill ",parent=self.root)
    
    
    def logout(self):
        self.root.destroy()
        os.system("python login.py")





if __name__=="__main__": 
    root=Tk()
    obj=BillClass(root)
    root.mainloop()