from tkinter import*
from PIL import Image,ImageTk
from tkinter import messagebox
import sqlite3
import os
import email_pass
import smtplib


import time





class Login_System:
    def __init__(self,root):
        self.root=root
        self.root.title("Login System | Developed By Vinod ")
        self.root.geometry("850x600+0+0")
        self.root.maxsize(850,550)
        
    
        self.otp=""
    
    
    #=======================Image ======================================
        #self.photo_image=ImageTk.PhotoImage(file=r"C:\Users\ram\Downloads\login-icon-3060.png")
        #self.lbl_photo_image=Label(self.root,image=self.photo_image).place(x=100,y=130)

        
        st_frame=Frame(self.root,bd=5,relief=GROOVE)
        st_frame.place(x=10,width=830,height=540)
    
    
    
    
    #============== Login Frame ======================================
        
        self.employee_id=StringVar()
        self.password=StringVar()
        
        login_frame=Frame(self.root,bd=5,relief=GROOVE,bg="#EAEAEA")
        login_frame.place(x=390,y=40,width=400,height=460)

        
        
        
        
        title=Label(login_frame,text="Login Sytem",bg="#EAEAEA",font=("Elephant",34,"bold"),fg="darkblue").place(x=50,y=30)

        
        lbl_user=Label(login_frame,text="Employee Id ",font=("goudy old style",20),bg="#EAEAEA").place(x=50,y=110)
        user_entry=Entry(login_frame,textvariable=self.employee_id,font=("Elephant",14),bg="lightyellow").place(x=50,y=150)
        lbl_pass=Label(login_frame,bg="#EAEAEA",text="Password ",font=("goudy old style",20)).place(x=50,y=190)
        password_entry=Entry(login_frame,textvariable=self.password,show="*",font=("Elephant",14),bg="lightyellow").place(x=50,y=230)

        login_btn=Button(login_frame,text="Login",command=self.login,font=("goudy old style",18),width=21,bg="#1E90FF",fg="white",cursor="hand2").place(x=50,y=280)

        lbl_user=Label(login_frame,bg="white").place(x=50,y=370,width=280,height=2)
        lbl_user=Label(login_frame,bg="#EAEAEA",text="OR",fg="grey",font=("times new roman",14)).place(x=170,y=360)
        forget_btn=Button(login_frame,bg="#EAEAEA",command=self.forget_window,text="Forget Password ?",fg="#00688B",cursor="hand2",font=("times new roman",16),bd=0).place(x=120,y=390)

        lbl_user=Label(text="Don't have an account ? ",font=("goudy old style",20),fg="black").place(x=15,y=350)
        sign_up_btn=Button(text="Sign Up ",fg="#00688B",cursor="hand2",font=("times new roman",18),bd=0).place(x=280,y=350)
         
         #============== Animation image ======================================
        self.im1=ImageTk.PhotoImage(file=r"C:\Users\ram\Desktop\Inventory\res\Crystal_Project_Personal.png")
        self.im2=ImageTk.PhotoImage(file=r"C:\Users\ram\Desktop\Inventory\res\dd.png")
        self.im3=ImageTk.PhotoImage(file=r"C:\Users\ram\Desktop\Inventory\res\forgot-password-icon-18358.png")
        self.im4=ImageTk.PhotoImage(file=r"C:\Users\ram\Desktop\Inventory\res\login .png")
        self.im5=ImageTk.PhotoImage(file=r"C:\Users\ram\Desktop\Inventory\res\login-icon-3058.png")
        self.im6=ImageTk.PhotoImage(file=r"C:\Users\ram\Desktop\Inventory\res\login-icon-3060.png")
        self.im7=ImageTk.PhotoImage(file=r"C:\Users\ram\Desktop\Inventory\res\password.png")
        self.im8=ImageTk.PhotoImage(file=r"C:\Users\ram\Desktop\Inventory\res\user-login.242x256.png")
        
        
        
        self.lbl_change_image=Label(self.root)
        self.lbl_change_image.place(x=100,y=100,width=200,height=250)

     
        self.animate()
    #=========================== All Function =================================
    def animate(self):
        self.im=self.im1
        self.im1=self.im2
        self.im2=self.im3
        self.im3=self.im4
        self.im4=self.im5
        self.im5=self.im6
        self.im6=self.im7
        self.im7=self.im8
        self.im8=self.im


        self.lbl_change_image.config(image=self.im)
        self.lbl_change_image.after(2000,self.animate)


    
    def login(self):
        con=sqlite3.connect(database=r"C:\Users\ram\Desktop\Inventory\vinod.db")
        cur=con.cursor()
        try:
            if self.employee_id.get()=="" or self.password.get()=="":
                messagebox.showerror("Error"," All Field are Rquired ",parent=self.root)

            else:
                cur.execute("select utype from employee where eid=? AND pass=?",(self.employee_id.get(),self.password.get()))
                user=cur.fetchone()
                if user==None:
                    messagebox.showerror("Error"," Invalid USERNAME / PASSWORD ",parent=self.root)
                    
                else:
                    if user[0]=="Admin":
                        self.root.destroy()
                        os.system("python IMS.py")
                    else:  
                        self.root.destroy()
                        os.system("python billing.py")

        
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)


            

    def forget_window(self):
        con=sqlite3.connect(database=r"C:\Users\ram\Desktop\Inventory\vinod.db")
        cur=con.cursor()
        try:
            if self.employee_id.get()=="":
                messagebox.showerror("Error"," Employee ID Must Be Fill ",parent=self.root)
            else:
                cur.execute("select email from employee where eid=?",(self.employee_id.get(),))
                email=cur.fetchone()
                if email==None:
                    messagebox.showerror("Error"," Invalid Employee ID, Try Again",parent=self.root)
                    
                else:
                    
                #===================Forget Window ===================================    
                    self.var_otp=StringVar()
                    self.var_new_pass=StringVar()
                    self.var_confirm_pass=StringVar()
                 


                    #call.send_email_funcation()
                    chk=self.send_email(email[0])
                    if chk!="s":
                        messagebox.showerror("Error",'Connction Error ,Try again',parent=self.root)
                    else:
                        self.forget_win=Toplevel(self.root)
                        self.forget_win.title("RESET PASSWORD")
                        self.forget_win.geometry("400x350+500+100")
                        self.forget_win.focus_force()

                        title=Label(self.forget_win,text="RESET PASSWORD",font=("goudy old style",15,"bold"),bg="#3f51b5",fg="white").pack(side=TOP,fil=X)
                        
                        lbl_reset=Label(self.forget_win,text="Enter OTP Sent on Registered Email ID ",font=("times new roman",15)).place(x=20,y=60)
                        tet_reset=Entry(self.forget_win,textvariable=self.var_otp,font=("times new roman",15),bg="lightyellow").place(x=20,y=100)
                        
                        lbl_new_pass=Label(self.forget_win,text="Enter New Password",font=("times new roman",15)).place(x=20,y=140)
                        lbl_new_pass=Entry(self.forget_win,textvariable=self.var_new_pass,font=("times new roman",15),bg="lightyellow").place(x=20,y=180)

                        lbl_confirm_pass=Label(self.forget_win,text="Enter Confirm Password",font=("times new roman",15)).place(x=20,y=220)
                        lbl_confirm_pass=Entry(self.forget_win,textvariable=self.var_confirm_pass,font=("times new roman",15),bg="lightyellow").place(x=20,y=260)

                        self.btn_update=Button(self.forget_win,text=" Update Password",command=self.update_password,state=DISABLED,font=("times new roman",11),bg="skyblue",fg="black")
                        self.btn_update.place(x=120,y=300)

                        self.btn_submit=Button(self.forget_win,text=" SUBMIT",command=self.validate_otp,font=("times new roman",11),bg="skyblue",fg="black")
                        self.btn_submit.place(x=270,y=100)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)

    
    def update_password(self):
        if self.var_new_pass.get()=="" or self.var_confirm_pass.get()=="":
             messagebox.showerror("Error","Password is reqired",parent=self.forget_win)
        elif self.var_new_pass.get()!= self.var_confirm_pass.get():
            messagebox.showerror("Error","New Password & Confirm Must be Same",parent=self.forget_win)
        else:
            con=sqlite3.connect(database=r"C:\Users\ram\Desktop\Inventory\vinod.db")
            cur=con.cursor()
            try:
                cur.execute("Update employee SET pass=? where eid=?",(self.var_new_pass.get(),self.employee_id.get()))
                con.commit()
                messagebox.showinfo("Success","Password Updated Successfully",parent=self.forget_win)
                self.forget_win.destroy() 

            
            except Exception as ex:
                messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)


    def validate_otp(self):
        
        if int(self.otp)==int(self.var_otp.get()):
            self.btn_update.config(state=NORMAL)
            self.btn_submit.config(state=DISABLED)
        else:
            messagebox.showerror("Error","Invalid OTP,Try Again",parent=self.forget_win)
        
  
       
    
    def send_email(self,to_):
        s=smtplib.SMTP('smtp.gmail.com',587)
        s.starttls()
        email_=email_pass.email_
        pass_=email_pass.pass_
        s.login(email_,pass_)
        self.otp=int(time.strftime("%H%S%M"))+int(time.strftime("%S"))
        subj="IMS Reset Password OTP"
        msg=f"Dear Sir / Madam,\n\nYour Reset OTP is {str(self.otp)}.\n\nWith Reqards,\nIMS Team"
        msg="Subject : {}\n\n{}".format(subj,msg)
        s.sendmail(email_,to_,msg)

        chk=s.ehlo()
        if chk[0]==250:
                return "s"
        else:
                return "f"

        




root=Tk()
obj=Login_System(root)
root.mainloop()