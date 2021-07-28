from tkinter import*
import math,random,os
from tkinter import messagebox

class Bill_App:
    def __init__(self, root):
        self.root=root
       #self.root.geometry("1350x7000+0+0")
        self.root.title("Billing Software")
        bg_color="#074463"
        title=Label(self.root,text="Billing Software",bd=12,relief=GROOVE,font=("times new roman",30,"bold"),bg=bg_color,fg="white",pady=2).pack(fill=X)

        #=============================  Variable  ===================
        #============================= Cosmetics  ====================

        self.soap=IntVar()
        self.fae_cream=IntVar()
        self.face_wash=IntVar()
        self.spray=IntVar()
        self.gell=IntVar()
        self.loshn=IntVar()

        #======================= Grocery ============================
        self.rice=IntVar()
        self.food_oil=IntVar()
        self.dall=IntVar()
        self.wheat=IntVar()
        self.sugar=IntVar()
        self.tea=IntVar()
                 
        #======================= Cold Drinks ============================
        self.maza=IntVar()
        self.cock=IntVar()
        self.frooti=IntVar()
        self.thombsup=IntVar()
        self.limca=IntVar()
        self.sprite=IntVar()
        
        #======================= Total Prodact Price &  Tax Variables ======
        self.cosmetic_price=StringVar()
        self.grocery_price=StringVar()
        self.cold_drink_price=StringVar()

        self.cosmetic_tax=StringVar()
        self.grocery_tax=StringVar()
        self.cold_drink_tax=StringVar()

        # ==================== Customer Vaeiables ===============
        self.c_name=StringVar()
        self.c_phone=StringVar()
        
        self.bill_no=StringVar()
        x=random.randint(1000,9999)
        self.bill_no.set(str(x))
        self.search_bill=StringVar()

       
        


        #=============================Customer Details================
        F1=LabelFrame(self.root,bd=10,relief=GROOVE,text="Customer Detaisl",font=("times new roman",15,"bold"),bg=bg_color,fg="gold")
        F1.place(x=0,y=80,relwidth=1)

        cname_lbl=Label(F1,text="Name",bg=bg_color,fg="white",font=("times new roman",18,"bold")).grid(row=0,column=0,pady=5,padx=20)
        cname_txt=Entry(F1,width=20,textvariable=self.c_name,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=1,pady=5,padx=10)

        cphone_lbl=Label(F1,text="Phone NO.",bg=bg_color,fg="white",font=("times new roman",18,"bold")).grid(row=0,column=2,pady=5,padx=20)
        cphone_txt=Entry(F1,width=20,textvariable=self.c_phone,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=3,pady=5,padx=10)
        
        c_bill_lbl=Label(F1,text="Bill NO.",bg=bg_color,fg="white",font=("times new roman",18,"bold")).grid(row=0,column=4,pady=5,padx=20)
        c_bill_txt=Entry(F1,width=20,textvariable=self.search_bill,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=5,pady=5,padx=10)
        
        bill_btn=Button(F1,text="search",width=10,command=self.find_bill,bd=7,font="arial 12 bold").grid(row=0,column=6,pady=10,padx=10)
         #==================== C0smetic Detail ==========

        F2=LabelFrame(self.root,bd=10,relief=GROOVE,text="Cosmetic",font=("times new roman",15,"bold"),bg=bg_color,fg="gold")
        F2.place(x=0,y="170",width="335",height="390")

        bath_lbl=Label(F2,text="Bath Shop",bg=bg_color,fg="lightgreen",font=("times new roman",18,"bold")).grid(row=0,column=0,pady=10,padx=0)
        bath_txt=Entry(F2,width=10,textvariable=self.soap,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=1,pady=10,padx=5)

        Face_cream_lbl=Label(F2,text="Face Cream",bg=bg_color,fg="lightgreen",font=("times new roman",18,"bold")).grid(row=1,column=0,pady=10,padx=5)
        Face_cream_txt=Entry(F2,width=10,textvariable=self.fae_cream,font="arial 15 ",bd=7,relief=SUNKEN).grid(row=1,column=1,pady=10,padx=5)

        Face_w_lbl=Label(F2,text="Face Wash",bg=bg_color,fg="lightgreen",font=("times new roman",18,"bold")).grid(row=2,column=0,pady=10,padx=5)
        Face_w_txt=Entry(F2,width=10,textvariable=self.face_wash,font="arial 15",bd=7,relief=SUNKEN).grid(row=2,column=1,pady=10,padx=5)


        Hair_s_lbl=Label(F2,text="Hair Spray",bg=bg_color,fg="lightgreen",font=("times new roman",18,"bold")).grid(row=3,column=0,pady=10,padx=5)
        Hair_s_txt=Entry(F2,width=10,textvariable=self.spray,font="arial 15",bd=7,relief=SUNKEN).grid(row=3,column=1,pady=10,padx=5)

        hair_g_lbl=Label(F2,text="Hair Gel",bg=bg_color,fg="lightgreen",font=("times new roman",18,"bold")).grid(row=4,column=0,pady=10,padx=5)
        Hair_g_txt=Entry(F2,width=10,textvariable=self.gell,font="arial 15",bd=7,relief=SUNKEN).grid(row=4,column=1,pady=10,padx=5)
        
        Body_lbl=Label(F2,text="Body Loshan",bg=bg_color,fg="lightgreen",font=("times new roman",18,"bold")).grid(row=5,column=0,pady=10,padx=5)
        Body_txt=Entry(F2,width=10,textvariable=self.loshn,font="arial 15",bd=7,relief=SUNKEN).grid(row=5,column=1,pady=10,padx=5)

        #==============Grocery Details================================

        F3=LabelFrame(self.root,bd=10,relief=GROOVE,text="Grocery",font=("times new roman",15,"bold"),bg=bg_color,fg="gold")
        F3.place(x="340",y="170",width="335",height="390")

        g1_lbl=Label(F3,text="Rice",bg=bg_color,fg="lightgreen",font=("times new roman",18,"bold")).grid(row=0,column=0,pady=10,padx=10)
        g1_txt=Entry(F3,width=13,textvariable=self.rice,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=1,pady=10,padx=10)

        g2_lbl=Label(F3,text="Food Oil",bg=bg_color,fg="lightgreen",font=("times new roman",18,"bold")).grid(row=1,column=0,pady=10,padx=10)
        g2_txt=Entry(F3,width=13,textvariable=self.food_oil,font="arial 15",bd=7,relief=SUNKEN).grid(row=1,column=1,pady=10,padx=10)

        g3_lbl=Label(F3,text="Daal",bg=bg_color,fg="lightgreen",font=("times new roman",18,"bold")).grid(row=2,column=0,pady=10,padx=10)
        g3_txt=Entry(F3,width=13,textvariable=self.dall,font="arial 15",bd=7,relief=SUNKEN).grid(row=2,column=1,pady=10,padx=10)

        g4_lbl=Label(F3,text="Wheat",bg=bg_color,fg="lightgreen",font=("times new roman",18,"bold")).grid(row=3,column=0,pady=10,padx=10)
        g4_txt=Entry(F3,width=13,textvariable=self.wheat,font="arial 15",bd=7,relief=SUNKEN).grid(row=3,column=1,pady=10,padx=10)

        g5_lbl=Label(F3,text="Sugar",bg=bg_color,fg="lightgreen",font=("times new roman",18,"bold")).grid(row=4,column=0,pady=10,padx=10)
        g5_txt=Entry(F3,width=13,textvariable=self.sugar,font="arial 15",bd=7,relief=SUNKEN).grid(row=4,column=1,pady=10,padx=10)

        g6_lbl=Label(F3,text="Tea",bg=bg_color,fg="lightgreen",font=("times new roman",18,"bold")).grid(row=5,column=0,pady=10,padx=10)
        g6_txt=Entry(F3,width=13,textvariable=self.tea,font="arial 15",bd=7,relief=SUNKEN).grid(row=5,column=1,pady=10,padx=10)

        #================ Cold Drinks ==============

        F4=LabelFrame(self.root,bd=10,relief=GROOVE,text="Cold Drinks",bg=bg_color,fg="gold",font=("times new roman",15,"bold"))
        F4.place(x="680",y="170",width="335",height="390")

        c1_lbl=Label(F4,text="Maza",bg=bg_color,fg="lightgreen",font=("times new roman",18,"bold")).grid(row=0,column=0,pady=1,padx=10)
        c1_txt=Entry(F4,width=13,textvariable=self.maza,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=1,pady=10,padx=10)

        c2_lbl=Label(F4,text="Cock",bg=bg_color,fg="lightgreen",font=("times new roman",18,"bold")).grid(row=1,column=0,pady=1,padx=10)
        c2_txt=Entry(F4,width=13,textvariable=self.cock,font="arial 15",bd=7,relief=SUNKEN).grid(row=1,column=1,pady=10,padx=10)

        c3_lbl=Label(F4,text="Frooti",bg=bg_color,fg="lightgreen",font=("times new roman",18,"bold")).grid(row=2,column=0,pady=1,padx=10)
        c3_txt=Entry(F4,width=13,textvariable=self.frooti,font="arial 15",bd=7,relief=SUNKEN).grid(row=2,column=1,pady=10,padx=10)

        c4_lbl=Label(F4,text="Thumbs Up",bg=bg_color,fg="lightgreen",font=("times new roman",18,"bold")).grid(row=3,column=0,pady=1,padx=10)
        c4_txt=Entry(F4,width=13,textvariable=self.thombsup,font="arial 15",bd=7,relief=SUNKEN).grid(row=3,column=1,pady=10,padx=10)

        c5_lbl=Label(F4,text="Limca",bg=bg_color,fg="lightgreen",font=("times new roman",18,"bold")).grid(row=4,column=0,pady=1,padx=10)
        c5_txt=Entry(F4,width=13,textvariable=self.limca,font="arial 15",bd=7,relief=SUNKEN).grid(row=4,column=1,pady=10,padx=10)

        c6_lbl=Label(F4,text="Sprite",bg=bg_color,fg="lightgreen",font=("times new roman",15,"bold")).grid(row=5,column=0,pady=1,padx=10)
        c6_txt=Entry(F4,width=13,textvariable=self.sprite,font="arial 15",bd=7,relief=SUNKEN).grid(row=5,column=1,pady=10,padx=10)



        #========================= Bill Area =============

        F5=Label(self.root,bd=10,relief=GROOVE)
        F5.place(x="1030",y="170",width="510",height="380")
        bill_title=Label(F5,text="Bill Area",bd=7,relief=GROOVE,font="arial 15 bold").pack(fill=X)
        scrol_y=Scrollbar(F5,orient=VERTICAL)
        self.txtarea=Text(F5,yscrollcommand=scrol_y.set)
        scrol_y.pack(side=RIGHT,fill=Y)
        scrol_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH,expand=1)


        #======================= Button Frame ==================

        F6=LabelFrame(self.root,bd=10,relief=GROOVE,text="Bill Manu",bg=bg_color,fg="gold",font=("times new roman",15,"bold"))
        F6.place(x=0,y=540,relwidth=1,height=240)

        m1=Label(F6,text="Total Cosmetic Price",bg=bg_color,fg="white",font=("times new roman",15,"bold")).grid(row=0,column=0,pady=5,padx=20,sticky="w")
        m1=Entry(F6,width=18,textvariable=self.cosmetic_price,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=0,column=1,pady=15,padx=1)

        m2=Label(F6,text="Total Grocery Price",bg=bg_color,fg="white",font=("times new roman",15,"bold")).grid(row=1,column=0,pady=5,padx=20,sticky="w")
        m2=Entry(F6,width=18,textvariable=self.grocery_price,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=1,column=1,pady=15,padx=1)

        m3=Label(F6,text="Total Cold Drinks Price",bg=bg_color,fg="white",font=("times new roman",15,"bold")).grid(row=2,column=0,pady=5,padx=20,sticky="w")
        m3=Entry(F6,width=18,textvariable=self.cold_drink_price,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=2,column=1,pady=15,padx=1)



        c1=Label(F6,text="Cosmetic Tax",bg=bg_color,fg="white",font=("times new roman",15,"bold")).grid(row=0,column=2,pady=5,padx=20,sticky="w")
        c1=Entry(F6,width=18,textvariable=self.cosmetic_tax,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=0,column=3,pady=15,padx=1)

        c2=Label(F6,text="Total Grocery Price",bg=bg_color,fg="white",font=("times new roman",15,"bold")).grid(row=1,column=2,pady=5,padx=20,sticky="w")
        c2=Entry(F6,width=18,textvariable=self.grocery_tax,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=1,column=3,pady=15,padx=1)

        c3=Label(F6,text="Total Cold Drinks Price",bg=bg_color,fg="white",font=("times new roman",15,"bold")).grid(row=2,column=2,pady=5,padx=20,sticky="w")
        c3=Entry(F6,width=18,textvariable=self.cold_drink_tax,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=2,column=3,pady=15,padx=1)
        
        btn_F=Frame(F6,bd=7,relief=GROOVE)
        btn_F.place(x=780,width=730,height=200)

        total_btn=Button(btn_F,command=self.total,text="Total",bg="cadetblue",fg="white",pady=15,width=13,height=2,font="arial 14 bold").grid(row=0,column=0,padx=5,pady=5)
        GBill_btn=Button(btn_F,command=self.bill_area,text="Genrate Bill",bg="cadetblue",fg="white",pady=13,height=2,width=15,font="arial 14 bold").grid(row=0,column=1,padx=5,pady=5)
        Clear_btn=Button(btn_F,command=self.clear_data,text="Clear",bg="cadetblue",fg="white",pady=15,width=13,height=2,font="arial 14 bold").grid(row=0,column=2,padx=5,pady=5)
        Exit_btn=Button(btn_F,command=self.Exit_app,text="Exit",bg="cadetblue",fg="white",pady=15,width=12,height=2,font="arial 14 bold").grid(row=0,column=3,padx=5,pady=5)


        F7=LabelFrame(self.root,bd=7,relief=GROOVE,bg="cadetblue",font=("times new roman",15,"bold"))
        F7.place(x=0,y=760,relwidth=1,relheight=1)
        c6_lbl=Label(F7,text="This Billing Software Created by N.M.R",bg="cadetblue",fg="gold",font=("times new roman",16,"bold")).grid(row=0,column=0,pady=0,padx=540)
        self.welcomw_bill()

    def total(self):

        self.c_s_p=self.soap.get()*40
        self.c_fc_p=self.fae_cream.get()*120
        self.c_fw_p=self.face_wash.get()*60
        self.c_hs_p=self.spray.get()*180
        self.c_hg_p=self.gell.get()*140
        self.c_bl_p=self.loshn.get()*180
                
        self.total_cosmetic_price=float(
                                    self.c_s_p+
                                    self.c_fc_p+
                                    self.c_fw_p+
                                    self.c_hs_p+
                                    self.c_hg_p+
                                    self.c_bl_p

                                      )
        self.cosmetic_price.set("Rs. "+str(self.total_cosmetic_price))
        self.c_tax=round((self.total_cosmetic_price*0.05),2)
        self.cosmetic_tax.set("RS. "+str(self.c_tax))

        self.g_r_p=self.rice.get()*40
        self.g_f_p=self.food_oil.get()*120
        self.g_d_p=self.dall.get()*60
        self.g_w_p=self.wheat.get()*180
        self.g_s_p=self.sugar.get()*140
        self.g_t_p=self.tea.get()*180
                
        self.total_grocery_price=float(
                                    self.g_r_p+
                                    self.g_f_p+
                                    self.g_d_p+
                                    self.g_w_p+
                                    self.g_s_p+
                                    self.g_t_p

                                      )
        self.grocery_price.set("Rs. "+str(self.total_grocery_price))
        self.g_tax=round((self.total_grocery_price*0.1),2)
        self.grocery_tax.set("RS. "+str(self.g_tax))

        self.d_m_p=self.maza.get()*60
        self.d_c_p=self.cock.get()*60
        self.d_f_p=self.frooti.get()*50
        self.d_t_p=self.thombsup.get()*45
        self.d_l_p=self.limca.get()*40
        self.d_s_p=self.sprite.get()*60
                
        self.total_cold_drink_price=float(
                                    self.d_m_p+
                                    self.d_c_p+
                                    self.d_f_p+
                                    self.d_t_p+
                                    self.d_l_p+
                                    self.d_s_p

                                      )
        self.cold_drink_price.set("Rs. "+str(self.total_cold_drink_price))
        self.d_tax=round((self.total_cold_drink_price*0.05),2)
        self.cold_drink_tax.set("RS. "+str(self.d_tax))
        

        self.Total_bill=float( self.total_cosmetic_price+
                               self.total_grocery_price+
                               self.total_cold_drink_price+
                               self.c_tax+
                               self.g_tax+
                               self.d_tax 
                             )

    def welcomw_bill(self):
      self.txtarea.delete('1.0',END)
      self.txtarea.insert(END,"\t\t Welcome to NMR Retail\n")
      self.txtarea.insert(END,f"\n Bill Number :- {self.bill_no.get()}")
      self.txtarea.insert(END,f"\n Name :- {self.c_name.get()}")
      self.txtarea.insert(END,f"\n Phone Number :- {self.c_phone.get()}")
      self.txtarea.insert(END,f"\n =========================================================")
      self.txtarea.insert(END,f"\t\tProduct \t\tQty\t\tPrice")
      self.txtarea.insert(END,f"\n =========================================================")

    def bill_area(self):
      if self.c_name.get()=="" or self.c_phone.get()=="":
        messagebox.showerror("Error","Customer Detail are must Entered")
      elif self.cosmetic_price.get()=="Rs. 0.0" and self.grocery_price.get()=="Rs. 0.0" and self.cold_drink_price.get()=="Rs. 0.0":
        messagebox.showerror("Error","No Product Selected")

      else:
        self.welcomw_bill()
        #============= cosmetic =============
        if self.soap.get()!=0:
          self.txtarea.insert(END,f"\n\tBath Shop\t\t{self.soap.get()}\t\tRs. {self.c_s_p}")
        if self.fae_cream.get()!=0:
          self.txtarea.insert(END,f"\n\tFace cream\t\t{self.fae_cream.get()}\t\tRs. {self.c_fc_p}")
        if self.face_wash.get()!=0:
          self.txtarea.insert(END,f"\n\tFace Wash\t\t{self.face_wash.get()}\t\tRs. {self.c_fw_p}")
        if self.spray.get()!=0:
          self.txtarea.insert(END,f"\n\tHair Spray\t\t{self.spray.get()}\t\tRs. {self.c_s_p}")
        if self.gell.get()!=0:
          self.txtarea.insert(END,f"\n\tHair Gell\t\t{self.gell.get()}\t\tRs. {self.c_hg_p}")
        if self.loshn.get()!=0:
          self.txtarea.insert(END,f"\n\tBody Loshan\t\t{self.loshn.get()}\t\tRs. {self.c_bl_p}")

        #============= Grocery =============
        if self.rice.get()!=0:
          self.txtarea.insert(END,f"\n\tRice\t\t{self.rice.get()}\t\tRs. {self.g_r_p}")
        if self.food_oil.get()!=0:
          self.txtarea.insert(END,f"\n\tFood Oil\t\t{self.food_oil.get()}\t\tRs. {self.g_f_p}")
        if self.dall.get()!=0:
          self.txtarea.insert(END,f"\n\tDall\t\t{self.dall.get()}\t\tRs. {self.g_d_p}")
        if self.wheat.get()!=0:
          self.txtarea.insert(END,f"\n\tWheat\t\t{self.wheat.get()}\t\tRs. {self.g_w_p}")
        if self.sugar.get()!=0:
          self.txtarea.insert(END,f"\n\tSugar\t\t{self.sugar.get()}\t\tRs. {self.g_s_p}")
        if self.tea.get()!=0:
          self.txtarea.insert(END,f"\n\tTea\t\t{self.tea.get()}\t\tRs. {self.g_t_p}")  

        #============= Cold Drinks =============
        if self.maza.get()!=0:
          self.txtarea.insert(END,f"\n\tMaza\t\t{self.maza.get()}\t\tRs. {self.d_m_p}")
        if self.cock.get()!=0:
          self.txtarea.insert(END,f"\n\tCock\t\t{self.cock.get()}\t\tRs. {self.d_c_p}")
        if self.frooti.get()!=0:
          self.txtarea.insert(END,f"\n\tFrooti\t\t{self.frooti.get()}\t\tRs. {self.d_f_p}")
        if self.thombsup.get()!=0:
          self.txtarea.insert(END,f"\n\tThumbs Up\t\t{self.thombsup.get()}\t\tRs. {self.d_t_p}")
        if self.limca.get()!=0:
          self.txtarea.insert(END,f"\n\tLimca\t\t{self.limca.get()}\t\tRs. {self.d_l_p}")
        if self.sprite.get()!=0:
          self.txtarea.insert(END,f"\n\tSprite\t\t{self.sprite.get()}\t\tRs. {self.d_s_p}")



        self.txtarea.insert(END,f"\n\n ---------------------------------------------------------")
        if self.cosmetic_tax.get()!="RS. 0.0":
          self.txtarea.insert(END,f"\n\tCosmetic Tax\t\t\t\t{self.cosmetic_tax.get()}")

        if self.grocery_tax.get()!="RS. 0.0":
          self.txtarea.insert(END,f"\n\tGrocery tax\t\t\t\t{self.grocery_tax.get()}")

        if self.cold_drink_tax.get()!="RS. 0.0":
          self.txtarea.insert(END,f"\n\tCosmetic Tax\t\t\t\t{self.cold_drink_tax.get()}")
          
        self.txtarea.insert(END,f"\n ---------------------------------------------------------")
        self.txtarea.insert(END,f"\n\t Total Bill\t\t\t\tRs. {self.Total_bill}")
        self.save_bill()
    def save_bill(self):
      op=messagebox.askyesno("Saveve Bill","Do you want save the Bill?")
      if op>0:
        self.bill_data=self.txtarea.get("1.0",END)
        f1=open("bills/"+str(self.bill_no.get())+".txt","w")
        f1.write(self.bill_data)
        f1.close()
        messagebox.showinfo("Save",f"Bill no. : {self.bill_no.get()} saved  Succesfuly")
      else:
        return
    def find_bill(self):
      present="no"
      for i in os.listdir("bills/"):
        if i.split('.')[0]==self.search_bill.get():
          f1=open(f"bills/{i}","r")
          self.txtarea.delete("1.0",END)
          for d in f1:
            self.txtarea.insert(END,d)
          f1.close()
          present="yes"
      if present=="no":
        messagebox.showerror("Error","Invalid Bill No.")
        

    def clear_data(self):
      op=messagebox.askyesno("Clear","Do you Want to Clear?")
      if op>0:

        self.soap.set(0)
        self.fae_cream.set(0)
        self.face_wash.set(0)
        self.spray.set(0)
        self.gell.set(0)
        self.loshn.set(0)

        #======================= Grocery ============================
        self.rice.set(0)
        self.food_oil.set(0)
        self.dall.set(0)
        self.wheat.set(0)
        self.sugar.set(0)
        self.tea.set(0)
                 
        #======================= Cold Drinks ============================
        self.maza.set(0)
        self.cock.set(0)
        self.frooti.set(0)
        self.thombsup.set(0)
        self.limca.set(0)
        self.sprite.set(0)
        
        #======================= Total Prodact Price &  Tax Variables ======
        self.cosmetic_price.set("")
        self.grocery_price.set("")
        self.cold_drink_price.set(0)
        self.cosmetic_tax.set("")
        self.grocery_tax.set("")
        self.cold_drink_tax.set("")
        # ==================== Customer Vaeiables ===============
        self.c_name.set("")
        self.c_phone.set("")
        
        self.bill_no.set("")
        x=random.randint(1000,9999)
        self.bill_no.set(str(x))
        self.search_bill.set("")
        self.welcomw_bill()

    def Exit_app(self):
      op=messagebox.askyesno("Exit","Do you Want to Exit?")
      if op>0:
        self.root.destroy()




    
                
root=Tk()
obj=Bill_App(root)
root.mainloop()
