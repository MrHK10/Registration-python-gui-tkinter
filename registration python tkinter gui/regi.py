from tkinter import*
from tkinter.messagebox import QUESTION
from turtle import bgcolor, title
from PIL import Image,ImageTk
# from pyparsing import White
from tkinter import ttk
class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Registration Form")
        self.root.geometry("1440x900+0+0")
        self.bg=ImageTk.PhotoImage(file="images/book.jpg")
        self.bg_image=Label(self.root,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)

        self.left=ImageTk.PhotoImage(file="regi/pn.png")
        left=Label(self.root,image=self.left).place(x=80,y=80,width=500,height=500)



        frame1=Frame(self.root,bg="white")
        frame1.place(x=580,y=80,width=630,height=500)
       

        title=Label(frame1,text="Register Here",bg="white",font=("times new roman",20,"bold")).place(x=50,y=30)
        f_name=Label(frame1,text="First Name",bg="white",fg="gray",font=("times new roman",18,"bold",)).place(x=50,y=90)
        txt_entry=Entry(frame1,bg="lightgray",font=("times new roman",15)).place(x=50,y=120,width=250)

        L_name=Label(frame1,text="Last Name",bg="white",fg="gray",font=("times new roman",18,"bold",)).place(x=340,y=90)
        txt_entry=Entry(frame1,bg="lightgray",font=("times new roman",15)).place(x=340,y=120,width=250)


        contact=Label(frame1,text="Contact No.",bg="white",fg="gray",font=("times new roman",18,"bold")).place(x=50,y=150)
        txt_entry=Entry(frame1,bg="lightgray",font=("times new roman",15)).place(x=50,y=180,width=250)

        email=Label(frame1,text="Email.",bg="white",fg="gray",font=("times new roman",18,"bold")).place(x=340,y=150)
        txt_entry=Entry(frame1,bg="lightgray",font=("times new roman",15)).place(x=340,y=180,width=250)


        
        # question=Label(frame1,text="security question",bg="white",fg="gray",font=("times new roman",18,"bold")).place(x=50,y=220)
        # cmb_quest=ttk.Combobox(frame1,font=("times new roman",13))
        # cmb_quest["values"]=('select','enter your nibbi name','enter your nibba name','enter your crush name')
        # cmb_quest.place(x=50,y=250,width=250)

        # answer=Label(frame1,text="Answer",bg="white",fg="gray",font=("times new roman",18,"bold")).place(x=340,y=220)
        # txt_entry=Entry(frame1,bg="lightgray",font=("times new roman",15)).place(x=340,y=250,width=250)

        password=Label(frame1,text="Password",bg="white",fg="gray",font=("times new roman",18,"bold")).place(x=50,y=220)
        txt_entry=Entry(frame1,bg="lightgray",font=("times new roman",15)).place(x=50,y=250,width=250)

        confirm_password=Label(frame1,text="Confirm your Password",bg="white",fg="gray",font=("times new roman",18,"bold")).place(x=340,y=220)
        txt_entry=Entry(frame1,bg="lightgray",font=("times new roman",15)).place(x=340,y=250,width=250)


        desc2=Label(frame1,text=" I Agree To The Terms & Conditions",bg="white",fg="black",font=("times new roman",10,"bold")).place(x=50,y=290)

        regi_btn=Button(frame1,text="Register Here -->",bd=0,bg="blue",fg="white",font=("times in roman",12)).place(x=57,y=340,width=200,height=30)

root=Tk()
obj=Register(root)
root.mainloop()
