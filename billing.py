from tkinter import*
from PIL import Image,ImageTk
import os
from tkinter import ttk,messagebox

class BillClass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.title("Rc Infra Digital Solution | Developed by Abhinav")
        self.root.config(bg="white")
        #===title===
        self.icon_title=PhotoImage(file="images/logo1.png")
        tiitle=Label(self.root,text="Rc infra Product Billing",image=self.icon_title,compound=LEFT,font=("times new roman",40,"bold"),bg="#010c48",fg="white",anchor="w",padx=20).place(x=0,y=0,relwidth=1,height=70)
        #===btn_loout===
        btn_logout=Button(self.root,text="Logout",font=("times new roman",15,"bold"),bg="yellow",cursor="hand2").place(x=1150,y=10,height=50,width=150)
        #===clock====
        self.lbl_clock=Label(self.root,text="Welcome to Store managemnt\t\t Date=:DD-MM-YYYY\t\t Time:HH:MM:SS",font=("times new roman",15),bg="#4d636d",fg="white")
        self.lbl_clock.place(x=0,y=70,relwidth=1,height=30)


        #======Product Frame===============
        self.var_search=StringVar()

        ProductFrame1= Frame(self.root,bd=4,relief=RIDGE,bg="white")
        ProductFrame1.place(x=6,y=110,width=410,height=550)


        pTitle=Label(ProductFrame1,text="All Products",font=("goudy old style",20,"bold"),bg="#262626",fg="white").pack(side=TOP,fill=X)

#=================================Product Search Frame========================
        ProductFrame2= Frame(ProductFrame1,bd=2,relief=RIDGE,bg="white")
        ProductFrame2.place(x=2,y=42,width=398,height=90)
        lbl_search=Label(ProductFrame2,text="Search Product | By Name", font=("times new roman",15,"bold"),bg="white",fg="green").place(x=2,y=5)

        lbl_search=Label(ProductFrame2,text="Product Name", font=("times new roman",15,"bold"),bg="white",).place(x=2,y=45)
        txt_search=Entry(ProductFrame2,textvariable=self.var_search, font=("times new roman",15),bg="lightyellow",).place(x=130,y=47,width=150,height=22)
        btn_search =Button(ProductFrame2,text="Search",font=("goudy old style",15),bg="#2196f3",fg="white",cursor="hand2").place(x=285,y=45,width=100,height=25)
        btn_show_all =Button(ProductFrame2,text="Show All",font=("goudy old style",15),bg="#083531",fg="white",cursor="hand2").place(x=285,y=10,width=100,height=25)



         #=======Product Detailed Frame================================

        ProductFrame3=Frame(ProductFrame1,bd=3,relief=RIDGE)
        ProductFrame3.place(x=2,y=140,width=398,height=375)

        scrolly=Scrollbar(ProductFrame3,orient=VERTICAL)
        scrollx=Scrollbar(ProductFrame3,orient=HORIZONTAL)

        self.product_Table=ttk.Treeview(ProductFrame3,columns=("pid","name","price","qty","status"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM ,fill=X)
        scrolly.pack(side=RIGHT ,fill=Y)
        scrollx.config(command=self.product_Table.xview)
        scrolly.config(command=self.product_Table.yview)
        self.product_Table.heading("pid",text="P-ID")
        self.product_Table.heading("name",text="Name")
        self.product_Table.heading("price",text="Price")
        self.product_Table.heading("qty",text="QTY")
        self.product_Table.heading("status",text="Status")
       

        self.product_Table["show"]="headings"

        self.product_Table.column("pid",width=90)
        self.product_Table.column("name",width=100)
        self.product_Table.column("price",width=100)
        self.product_Table.column("qty",width=100)
        self.product_Table.column("status",width=100)
        self.product_Table.pack(fill=BOTH,expand=1)
        lbl_note=Label(ProductFrame1,text="Note:'Enter 0 Qty to Remove the Product from the Cart'", font=("goudy old style",12),anchor='w',bg="white",fg="red").pack(side=BOTTOM,fill=X)
       
       
        

        #===========================================CustomerFrame==================================================================================================================================================
        
        self.var_cname=StringVar()
        self.var_contact = StringVar()
        CustomerFrame= Frame(self.root,bd=4,relief=RIDGE,bg="white")
        CustomerFrame.place(x=420,y=110,width=530,height=70)

        cTitle=Label(CustomerFrame,text="Customer Details",font=("goudy old style",15),bg="lightgray").pack(side=TOP,fill=X)
        lbl_name=Label(CustomerFrame,text="Name",font =("times new roman",15), bg ="white").place(x=5,y=35)
        txt_name=Entry(CustomerFrame,textvariable=self.var_cname, font=("times new roman ",13),bg = "lightyellow").place(x=80,y=35,width=180)

        lbl_contact=Label(CustomerFrame,text="Contact No.",font =("times new roman",15), bg ="white").place(x=270,y=35)
        txt_contact=Entry(CustomerFrame,textvariable=self.var_contact, font=("times new roman ",13),bg = "lightyellow").place(x=380,y=35,width=140)

#=====================Cal Cart Frame======================================

        Cal_Cart_Frame= Frame(self.root,bd=2,relief=RIDGE,bg="white")
        Cal_Cart_Frame.place(x=420,y=190,width=530,height=360)

#========================Calculator Frame==============
        Cal_Frame= Frame(Cal_Cart_Frame,bd=4,relief=RIDGE,bg="white")
        Cal_Frame.place(x=5,y=10,width=268,height=340)




        #======= cart Frsame3================================

        cart_Frame=Frame(Cal_Cart_Frame,bd=3,relief=RIDGE)
        cart_Frame.place(x=280,y=8,width=245,height=342)
        cartTitle=Label(cart_Frame,text="Cart \t Total Product: [0] ",font=("goudy old style",15),bg="lightgray").pack(side=TOP,fill=X)

        scrolly=Scrollbar(cart_Frame,orient=VERTICAL)
        scrollx=Scrollbar(cart_Frame,orient=HORIZONTAL)

        self.CartTable=ttk.Treeview(cart_Frame,columns=("pid","name","price","qty","status"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM ,fill=X)
        scrolly.pack(side=RIGHT ,fill=Y)
        scrollx.config(command=self.CartTable.xview)
        scrolly.config(command=self.CartTable.yview)

        self.CartTable.heading("pid",text="P-ID")
        self.CartTable.heading("name",text="Name")
        self.CartTable.heading("price",text="Price")
        self.CartTable.heading("qty",text="QTY")
        self.CartTable.heading("status",text="Status")
        self.CartTable["show"]="headings"

        self.CartTable.column("pid",width=40)
        self.CartTable.column("name",width=100)
        self.CartTable.column("price",width=90)
        self.CartTable.column("qty",width=40)
        self.CartTable.column("status",width=90)
        self.CartTable.pack(fill=BOTH,expand=1)
        #self.CartTable.bind("<ButtonRelease-1>",self.get_data)

        #======Add CartWidgets Frame===============================================================
        self.var_pid=StringVar()
        self.var_pname=StringVar()
        self.var_price=StringVar()
        self.var_qty=StringVar()
        self.var_stock=StringVar()
        Add_CartWidgetsFrame= Frame(self.root,bd=2,relief=RIDGE,bg="white")
        Add_CartWidgetsFrame.place(x=420,y=550,width=530,height=110)


        lbl_p_name=Label(Add_CartWidgetsFrame,text="Product Name" , font=("times new roman",15),bg="white").place(x=5,y=5)
        txt_p_name=Entry(Add_CartWidgetsFrame,textvariable=self.var_pname , font=("times new roman",15),bg="lightyellow",state='readonly').place(x=5,y=35,width=190,height=22)

        lbl_p_price=Label(Add_CartWidgetsFrame,text="Price Per Qty" , font=("times new roman",15),bg="white").place(x=230,y=5)
        txt_p_price=Entry(Add_CartWidgetsFrame,textvariable=self.var_price, font=("times new roman",15),bg="lightyellow",state='readonly').place(x=230,y=35,width=150,height=22)

        lbl_p_qty=Label(Add_CartWidgetsFrame,text="Quantity", font=("times new roman",15),bg="white").place(x=390,y=5)
        txt_p_qty=Entry(Add_CartWidgetsFrame,textvariable=self.var_qty, font=("times new roman",15),bg="lightyellow").place(x=390,y=35,width=125,height=22)

        self.lbl_inStock=Label(Add_CartWidgetsFrame,text="In Stock [9999]" , font=("times new roman",15),bg="white")
        self.lbl_inStock.place(x=5,y=70)
        btn_clear_cart=Button(Add_CartWidgetsFrame,text ="clear",font =("times new roman", 15,"bold"),bg="red",cursor="hand2").place(x=180,y=70,width=150,height=30)
        btn_add_cart=Button(Add_CartWidgetsFrame,text ="Add | Update Cart",font =("times new roman", 15,"bold"),bg="green",cursor="hand2").place(x=340,y=70,width=180,height=30)






               













if __name__ == "__main__":
    root =Tk()
    obj =BillClass(root)
    root.mainloop()