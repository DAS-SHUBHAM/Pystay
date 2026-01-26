from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk
import random
import mysql.connector
import database
from tkinter import messagebox
from time import strftime
from datetime import datetime

class Room_Booking:
    def __init__ (self,root):
        self.root=root
        self.root.title("ROOM BOOKING PAGE")
        self.root.geometry("1140x520+210+165")
        
        # declaring variables
        self.var_contact=StringVar()
        self.var_checkIn=StringVar()
        self.var_checkOut=StringVar()
        self.var_roomType=StringVar()
        self.var_roomNo=StringVar()
        self.var_stayingDays=StringVar()
        self.var_mealType=StringVar()
        self.var_paidTax=StringVar()
        self.var_subTotal=StringVar()
        self.var_totalPrice=StringVar()
        
        # setting title
        lbl_title=Label(self.root,text="ROOM BOOKING INFORMATION",font=("times new roman",20,"bold"),bg="black",fg="pink",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1138,height=50)
    
        # logo for the page 
        
        img2=Image.open("C:\\Users\\sdher\\Desktop\\PyStay\\img\\logo.png")
        img2 = img2.resize((100,50),Image.Resampling.LANCZOS)
        self.photo_img2=ImageTk.PhotoImage(img2)
        
        lbl_img2=Label(self.root,image=self.photo_img2,bd=4,relief=RIDGE)
        lbl_img2.place(x=0,y=0,width=100,height=50)
        
        # Label frame
        
        label_frame_left=LabelFrame(self.root,bd=2,relief=SUNKEN,text="ROOM BOOKING DETAILS",font=("arial",12,"bold"),bg="black",fg="pink")
        label_frame_left.place(x=5,y=50,width=425,height=465)
    
        # customer contact
        lbl_contact=Label(label_frame_left,text="Customer Contact:",font=("arial",12,"bold"),padx=1,pady=5,bg="black",fg="pink")
        lbl_contact.grid(row=0,column=0,sticky=W)
    
        entry_contact=ttk.Entry(label_frame_left,textvariable=self.var_contact,width=20,font=("arial",12,"bold"),foreground="blue")
        entry_contact.grid(row=0,column=1,sticky=W)
        
        # creating button after contact label to fetch data
        fetch_btn=Button(label_frame_left,text="FETCH",command=self.Fetch_Contact,width=8,font=("arial",10,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
        fetch_btn.place(x=345,y=4)
    
        
        # customer check-in date
        lbl_check_in_date=Label(label_frame_left,text="Check-In-Date:",font=("arial",12,"bold"),padx=1,pady=5,bg="black",fg="pink")
        lbl_check_in_date.grid(row=1,column=0,sticky=W)
    
        entry_check_in_date=ttk.Entry(label_frame_left,textvariable=self.var_checkIn,width=29,font=("arial",12,"bold"),foreground="blue")
        entry_check_in_date.grid(row=1,column=1,sticky=W)
        
        # customer check_out_date
        lbl_check_out=Label(label_frame_left,text="Check-Out-Date:",font=("arial",12,"bold"),padx=1,pady=2,bg="black",fg="pink")
        lbl_check_out.grid(row=2,column=0,sticky=W)
    
        entry_check_out=ttk.Entry(label_frame_left,width=29,textvariable=self.var_checkOut,font=("arial",12,"bold"),foreground="blue")
        entry_check_out.grid(row=2,column=1,sticky=W)
    
        # customer room type combo box
        lbl_room_type=Label(label_frame_left,text="Room-Type:",font=("arial",12,"bold"),padx=1,pady=5,bg="black",fg="pink")
        lbl_room_type.grid(row=3,column=0,sticky=W)
        
        combo_room_type=ttk.Combobox(label_frame_left,textvariable=self.var_roomType,font=("arial",12,"bold"),width=27,state="readonly")
        combo_room_type["value"]=("Single","Double","Luxury")
        combo_room_type.current(0)
        combo_room_type.grid(row=3,column=1)
    
        #Room Number
        lbl_room_number=Label(label_frame_left,text="Room-Number:",font=("arial",12,"bold"),padx=1,pady=5,bg="black",fg="pink")
        lbl_room_number.grid(row=4,column=0,sticky=W)
    
        entry_room_number=ttk.Entry(label_frame_left,textvariable=self.var_roomNo,width=29,font=("arial",12,"bold"),foreground="blue")
        entry_room_number.grid(row=4,column=1,sticky=W)
    
        #Number Of Days
        lbl_no_of_days=Label(label_frame_left,text="Staying-Days:",font=("arial",12,"bold"),padx=1,pady=5,bg="black",fg="pink")
        lbl_no_of_days.grid(row=5,column=0,sticky=W)
    
        combo_no_of_days=ttk.Combobox(label_frame_left,textvariable=self.var_stayingDays,font=("arial",12,"bold"),width=27,state="readonly")
        combo_no_of_days["value"]=("1","2","3","4","5","6","7","8","9","10","11","12","13","14","15",
                                   "16","17","18","19","20","21","22","23","24","25","26","27","28","29","30")
        combo_no_of_days.current(0)
        combo_no_of_days.grid(row=5,column=1)
    
        # customer meal type combo box
        lbl_meal_type=Label(label_frame_left,text="Meal-Type:",font=("arial",12,"bold"),padx=1,pady=5,bg="black",fg="pink")
        lbl_meal_type.grid(row=6,column=0,sticky=W)
        
        combo_meal_type=ttk.Combobox(label_frame_left,font=("arial",12,"bold"),textvariable=self.var_mealType,width=27,state="readonly")
        combo_meal_type["value"]=("Veg","Non-Veg")
        combo_meal_type.current(0)
        combo_meal_type.grid(row=6,column=1)
    
        # Paid Tax
        lbl_tax=Label(label_frame_left,text="Paid-Tax:",font=("arial",12,"bold"),padx=1,pady=5,bg="black",fg="pink")
        lbl_tax.grid(row=7,column=0,sticky=W)
    
        entry_tax=ttk.Entry(label_frame_left,textvariable=self.var_paidTax,width=29,font=("arial",12,"bold"),foreground="blue",state="readonly")
        entry_tax.grid(row=7,column=1,sticky=W)
        
        # sub total
        lbl_sub_total=Label(label_frame_left,text="Sub-Total:",font=("arial",12,"bold"),padx=1,pady=5,bg="black",fg="pink")
        lbl_sub_total.grid(row=8,column=0,sticky=W)
    
        entry_sub_total=ttk.Entry(label_frame_left,textvariable=self.var_subTotal,width=29,font=("arial",12,"bold"),foreground="blue",state="readonly")
        entry_sub_total.grid(row=8,column=1,sticky=W)
        
        # total cost
        lbl_total_Cost=Label(label_frame_left,text="Total-Price:",font=("arial",12,"bold"),padx=1,pady=5,bg="black",fg="pink")
        lbl_total_Cost.grid(row=9,column=0,sticky=W)
    
        entry_total_Cost=ttk.Entry(label_frame_left,textvariable=self.var_totalPrice,width=29,font=("arial",12,"bold"),foreground="blue",state="readonly")
        entry_total_Cost.grid(row=9,column=1,sticky=W)
        
        # creating buttons to perform some operations
        # add button
        add_btn=Button(label_frame_left,text="ADD",command=self.add_data,width=9,font=("arial",13,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
        add_btn.place(x=0,y=350)
    
        # update button
        update_btn=Button(label_frame_left,text="UPDATE",command=self.update,width=9,font=("arial",13,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
        update_btn.place(x=100,y=350)
        
        # reset button
        reset_btn=Button(label_frame_left,text="RESET",command=self.reset,width=9,font=("arial",13,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
        reset_btn.place(x=200,y=350)
        
        # delete button
        del_btn=Button(label_frame_left,text="DELETE",command=self.delete,width=11,font=("arial",13,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
        del_btn.place(x=300,y=350)
        
        #BILLING details button
        bill_btn=Button(label_frame_left,text="BILLING-DETAILS",command=self.total,width=33,font=("arial",15,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
        bill_btn.place(x=7,y=390)
        
        # right side image
        img3=Image.open("C:\\Users\\sdher\\Desktop\\PyStay\\img\\bedroom.jpg")
        img3 = img3.resize((318,190),Image.Resampling.LANCZOS)
        self.photo_img3=ImageTk.PhotoImage(img3)
        
        lbl_img3=Label(self.root,image=self.photo_img3,bd=4,relief=RIDGE)
        lbl_img3.place(x=820,y=50,width=318,height=190)
        
        
        ###################### creating table frame and label search by #################
        table_frame=LabelFrame(self.root,bd=2,relief=SUNKEN,text="View Details & Search System",font=("arial",12,"bold"),bg="black",fg="pink")
        table_frame.place(x=432,y=240,width=705,height=275)
        
        # creating label search by
        lbl_search=Label(table_frame,text="SearchBy:",font=("arial",12,"bold"),bg="Blue",fg="black")
        lbl_search.grid(row=0,column=1,sticky=W,padx=2)
        self.search_var=StringVar()
        # creating combo box ############
        combo_search_by=ttk.Combobox(table_frame,textvariable=self.search_var,font=("arial",12,"bold"),width=20,state="readonly")
        combo_search_by["value"]=("Contact","RoomNumber")
        combo_search_by.current(0)
        combo_search_by.grid(row=0,column=2,padx=2)
        
        # creating entry field for searching the customer#####
        self.txt_search=StringVar()
        txt_search=ttk.Entry(table_frame,textvariable=self.txt_search,width=21,font=("arial",12,"bold"))
        txt_search.grid(row=0,column=3,sticky=W,padx=2)
    
        # creating buttons####################
        # search button
        search_btn=Button(table_frame,text="SEARCH",command=self.search,width=9,font=("arial",12,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
        search_btn.grid(row=0,column=4)
        
        #show all button
        show_btn=Button(table_frame,text="SHOW ALL",command=self.fetch_data,width=9,font=("arial",12,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
        show_btn.grid(row=0,column=5)
    
        # creating show data table ##################
        ###### SHOW DATA TABLE####################
        details_table=Frame(table_frame,bd=2,relief=SUNKEN,)
        details_table.place(x=0,y=50,width=690,height=190)
        
        # creating scroll bar
        scroll_x=ttk.Scrollbar(details_table,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(details_table,orient=VERTICAL)
        
        self.Room_Table=ttk.Treeview(details_table,column=("Contact","CheckIn","CheckOut","RoomType","RoomNumber","StayingDays","MealType","PaidTax","SubTotal","TotalPrice"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        
        scroll_x.config(command=self.Room_Table.xview)
        scroll_y.config(command=self.Room_Table.yview)
        
        ## displaying columns to the user #####################
        
        self.Room_Table.heading("Contact",text="Contact")
        self.Room_Table.heading("CheckIn",text="CheckIn")
        self.Room_Table.heading("CheckOut",text="CheckOut")
        self.Room_Table.heading("RoomType",text="RoomType")
        self.Room_Table.heading("RoomNumber",text="RoomNumber")
        self.Room_Table.heading("StayingDays",text="StayingDays")
        self.Room_Table.heading("MealType",text="MealType")
        self.Room_Table.heading("PaidTax",text="PaidTax")
        self.Room_Table.heading("SubTotal",text="SubTotal")
        self.Room_Table.heading("TotalPrice",text="TotalPrice")
        
        
        # displaying columns with the help of show
        self.Room_Table["show"]="headings"
        
        # setting the width of columns
        self.Room_Table.column("Contact",width=100)
        self.Room_Table.column("CheckIn",width=100)
        self.Room_Table.column("CheckOut",width=100)
        self.Room_Table.column("RoomType",width=100)
        self.Room_Table.column("RoomNumber",width=100)
        self.Room_Table.column("StayingDays",width=100)
        self.Room_Table.column("MealType",width=100)
        self.Room_Table.column("PaidTax",width=100)
        self.Room_Table.column("SubTotal",width=100)
        self.Room_Table.column("TotalPrice",width=100)
        
        ## packing our table
        self.Room_Table.pack(fill=BOTH,expand=1) 
        self.Room_Table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()# fetching our data
        
     
     
    ####################### fetching data ##############################    
    def Fetch_Contact(self):
        if self.var_contact.get=="":
            messagebox.showerror("ERROR","Please Enter The Contact Number.",parent=self.root)
        else:
            conn=database.get_db_connection()
            my_cursor=conn.cursor()   
            query=("select c_name from Customer where mobile=%s")
            value=(self.var_contact.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            
            if row==None:
                messagebox.showerror("ERROR","ENTERED NUMBER DIDN'T MATCHED WITH RECORDS",parent=self.root)
            else:
                conn.commit()
                conn.close()
                
                show_data_frame=Frame(self.root,bd=4,relief=RIDGE,padx=2)
                show_data_frame.place(x=430,y=52,width=380,height=187)
                
                lbl_name=Label(show_data_frame,text="Customer's Name:",font=("arial",12,"bold"))
                lbl_name.place(x=0,y=0)
                
                lbl=Label(show_data_frame,text=row,font=("arial",12,"bold"))
                lbl.place(x=150,y=0)
            
                # FETCHING GENDER
                conn=database.get_db_connection()
                my_cursor=conn.cursor()   
                query=("select gender from Customer where mobile=%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()
                
                lbl_GENDER=Label(show_data_frame,text="Customer's Gender:",font=("arial",12,"bold"))
                lbl_GENDER.place(x=0,y=30)
                
                lbl=Label(show_data_frame,text=row,font=("arial",12,"bold"))
                lbl.place(x=160,y=30)
        
                # FETCHING EMAIL
                conn=database.get_db_connection()
                my_cursor=conn.cursor()   
                query=("select email from Customer where mobile=%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()
                
                lbl_EMAIL=Label(show_data_frame,text="Customer's Email:",font=("arial",12,"bold"))
                lbl_EMAIL.place(x=0,y=60)
                
                lbl=Label(show_data_frame,text=row,font=("arial",12,"bold"))
                lbl.place(x=150,y=60)
        
                
                # fetching nationality
                conn=database.get_db_connection()
                my_cursor=conn.cursor()   
                query=("select nationality from Customer where mobile=%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()
                
                lbl_NATIONALITY=Label(show_data_frame,text="Customer's Nationality:",font=("arial",12,"bold"))
                lbl_NATIONALITY.place(x=0,y=90)
                
                lbl=Label(show_data_frame,text=row,font=("arial",12,"bold"))
                lbl.place(x=185,y=90)
        
        
                # id proof number
                conn=database.get_db_connection()
                my_cursor=conn.cursor()   
                query=("select id_number from Customer where mobile=%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()
                
                lbl_id_proof_no=Label(show_data_frame,text="Customer's ID-Prof-No:",font=("arial",12,"bold"))
                lbl_id_proof_no.place(x=0,y=120)
                
                lbl=Label(show_data_frame,text=row,font=("arial",12,"bold"))
                lbl.place(x=185,y=120)
        
                # address 
                conn=database.get_db_connection()
                my_cursor=conn.cursor()   
                query=("select address from Customer where mobile=%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()
                
                lbl_address=Label(show_data_frame,text="Customer's Address:",font=("arial",12,"bold"))
                lbl_address.place(x=0,y=150)
                
                lbl=Label(show_data_frame,text=row,font=("arial",12,"bold"))
                lbl.place(x=170,y=150)
                conn.commit()
                conn.close()
        
        # creating function to work with buttons
    def add_data(self):
            if self.var_contact.get()=="" or self.var_checkIn.get()=="":
                messagebox.showerror("ERROR","ALL FIELDS ARE REQUIRED",parent=self.root)
            elif self.var_roomNo.get()=="" or self.var_roomType.get()=="":
                messagebox.showerror("MANDATORY SECTION","ALL FIELDS ARE REQUIRED",parent=self.root)
            elif self.var_paidTax.get()=="" or self.var_subTotal.get()=="":
                messagebox.showerror("ERROR","ALL FIELDS ARE REQUIRED",parent=self.root)
            else:
                try:
                    conn=database.get_db_connection()
                    my_cursor=conn.cursor()
                    my_cursor.execute("INSERT INTO rooms VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                            self.var_contact.get(),
                                                                                                            self.var_checkIn.get(),
                                                                                                            self.var_checkOut.get(),
                                                                                                            self.var_roomType.get(),
                                                                                                            self.var_roomNo.get(),
                                                                                                            self.var_stayingDays.get(),
                                                                                                            self.var_mealType.get(),
                                                                                                            self.var_paidTax.get(),
                                                                                                            self.var_subTotal.get(),
                                                                                                            self.var_totalPrice.get()
                                                                                                        ))
                    conn.commit()
                    self.fetch_data() # calling the function 
                    conn.close()
                    messagebox.showinfo("Success","Room Booked",parent=self.root)
                except:
                    messagebox.showwarning("Warning","Something Went Wrong:",parent=self.root)  
        
    # fetch data   
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="root",database="hoteldb")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from rooms")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.Room_Table.delete(*self.Room_Table.get_children())
            for i in rows:
                self.Room_Table.insert("",END,values=i)
        conn.commit()
        conn.close()
              
    # creating function for get cursor     
    def get_cursor(self,event=""):
        cursor_row=self.Room_Table.focus()
        content=self.Room_Table.item(cursor_row)
        row=content["values"]
        
        self.var_contact.set(row[0])
        self.var_checkIn.set(row[1])
        self.var_checkOut.set(row[2])
        self.var_roomType.set(row[3])
        self.var_roomNo.set(row[4])
        self.var_stayingDays.set(row[5])
        self.var_mealType.set(row[6])
        self.var_paidTax.set(row[7])
        self.var_subTotal.set(row[8])
        self.var_totalPrice.set(row[9])
        
    # creating function to update
    def update(self):
        if self.var_contact.get()=="":
            messagebox.showerror("ERROR","Please Enter Your Mobile Number",parent=self.root)
        else:    
            conn=database.get_db_connection()
            my_cursor=conn.cursor()
            my_cursor.execute("update rooms set CheckIn=%s,CheckOut=%s,RoomType=%s,RoomNumber=%s,StayingDays=%s,MealType=%s,PaidTax=%s,SubTotal=%s,TotalPrice=%s where Contact=%s",(
                                                                                                                                                                        
                                                                                                                                                                        self.var_checkIn.get(),
                                                                                                                                                                        self.var_checkOut.get(),
                                                                                                                                                                        self.var_roomType.get(),
                                                                                                                                                                        self.var_roomNo.get(),
                                                                                                                                                                        self.var_stayingDays.get(),
                                                                                                                                                                        self.var_mealType.get(),
                                                                                                                                                                        self.var_paidTax.get(),
                                                                                                                                                                        self.var_subTotal.get(),
                                                                                                                                                                        self.var_totalPrice.get(),
                                                                                                                                                                        self.var_contact.get()    
                                                                                                                                                                            ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("UPDATE","Room Details Has Been Updated",parent=self.root)
    
    
    #creating function to delete
    def delete(self):
        delete=messagebox.askyesno("PyStay","Do You Want To Delete The Details",parent=self.root)
        if delete>0:
            conn=database.get_db_connection()
            my_cursor=conn.cursor()
            query="delete from rooms where contact=%s"
            value=(self.var_contact.get(),)
            my_cursor.execute(query,value)
           
        else:
            if not delete:
                return
        conn.commit()
        self.fetch_data()
        conn.close()    
         
    # creating function for reset
    def reset(self):
        self.var_contact.set("")
        self.var_checkIn.set("")
        self.var_checkOut.set("")
        self.var_roomType.set("")
        self.var_roomNo.set("")
        self.var_stayingDays.set("")
        self.var_paidTax.set("")
        self.var_subTotal.set("")
        self.var_totalPrice.set("")
        
             
    ##########creating function for calculations ############
    def total(self):
        try:
            in_date = datetime.strptime(self.var_checkIn.get(), "%d/%m/%Y")
            out_date = datetime.strptime(self.var_checkOut.get(), "%d/%m/%Y")
        except ValueError:
            messagebox.showerror(
                "Invalid Date",
                "Please enter dates in DD/MM/YYYY format"
            )
            return

        if out_date < in_date:
            messagebox.showerror(
                "Date Error",
                "Check-out date cannot be before check-in date"
            )
            return

        staying_days = (out_date - in_date).days
        if staying_days == 0:
            staying_days = 1

        self.var_stayingDays.set(staying_days)
  
         
        # condition for single room and non-veg to calculate bill
        if (self.var_mealType.get()=="Non-Veg" and self.var_roomType.get()=="Single"):
            q1=float(800)
            q2=float(1500)
            q3=float(self.var_stayingDays.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs."+str("%.2f"%((q5)*0.9))
            ST="Rs."+str("%.2f"%((q5)))
            TP="Rs."+str("%.2f"%(q5+((q5)*0.9)))
            self.var_paidTax.set(Tax)
            self.var_subTotal.set(ST)
            self.var_totalPrice.set(TP)
        
        # condition for single room and veg to calculate bill    
        elif(self.var_mealType.get()=="Veg" and self.var_roomType.get()=="Single"):
            q1=float(500)
            q2=float(1000)
            q3=float(self.var_stayingDays.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax=str("%.2f"%((q5)*0.9))
            ST=str("%.2f"%((q5)))
            TP=str("%.2f"%(q5+((q5)*0.9)))
            self.var_paidTax.set(Tax)
            self.var_subTotal.set(ST)
            self.var_totalPrice.set(TP)
        #else:
        #   messagebox.showerror("Error","Please select meal type.")
        # condition for double room and non-veg to calculate bill
        if (self.var_mealType.get()=="Non-Veg" and self.var_roomType.get()=="Double"):
            q1=float(1600)
            q2=float(3000)
            q3=float(self.var_stayingDays.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs."+str("%.2f"%((q5)*0.9))
            ST="Rs."+str("%.2f"%((q5)))
            TP="Rs."+str("%.2f"%(q5+((q5)*0.9)))
            self.var_paidTax.set(Tax)
            self.var_subTotal.set(ST)
            self.var_totalPrice.set(TP)
        
        # condition for double room and veg to calculate bill    
        elif(self.var_mealType.get()=="Veg" and self.var_roomType.get()=="Double"):
            q1=float(1000)
            q2=float(2000)
            q3=float(self.var_stayingDays.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax=str("%.2f"%((q5)*0.9))
            ST=str("%.2f"%((q5)))
            TP=str("%.2f"%(q5+((q5)*0.9)))
            self.var_paidTax.set(Tax)
            self.var_subTotal.set(ST)
            self.var_totalPrice.set(TP)
        #else:
        #    messagebox.showerror("Error","Please select meal type.")
        #condition for luxury room and non-veg to calculate bill
        if (self.var_mealType.get()=="Non-Veg" and self.var_roomType.get()=="Double"):
            q1=float(3200)
            q2=float(6000)
            q3=float(self.var_stayingDays.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs."+str("%.2f"%((q5)*0.9))
            ST="Rs."+str("%.2f"%((q5)))
            TP="Rs."+str("%.2f"%(q5+((q5)*0.9)))
            self.var_paidTax.set(Tax)
            self.var_subTotal.set(ST)
            self.var_totalPrice.set(TP)
        
        # condition for luxury room and veg to calculate bill    
        elif(self.var_mealType.get()=="Veg" and self.var_roomType.get()=="Luxury"):
            q1=float(2500)
            q2=float(4000)
            q3=float(self.var_stayingDays.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax=str("%.2f"%((q5)*0.9))
            ST=str("%.2f"%((q5)))
            TP=str("%.2f"%(q5+((q5)*0.9)))
            self.var_paidTax.set(Tax)
            self.var_subTotal.set(ST)
            self.var_totalPrice.set(TP)
        #else:
        #    messagebox.showerror("Error","Please select meal type.")
         
         
    ###### search system functionalities
    def search(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="root",database="hoteldb")
        my_cursor=conn.cursor()
        my_cursor.execute(
        "select * from rooms where " +
        self.search_var.get() +
        " LIKE '%" + self.txt_search.get() + "%'"
        )
        row=my_cursor.fetchall()
        if len(row)!=0:
            self.Room_Table.delete(*self.Room_Table.get_children())
            for i in row:
                self.Room_Table.insert("",END,values=i)
        conn.commit()
        conn.close()        
      
            
        
        
if __name__ == "__main__":
    root=Tk()
    obj=Room_Booking(root)
    root.mainloop()