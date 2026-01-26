from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk
import random
import mysql.connector
import database
from tkinter import messagebox

class Customer_Window:
    def __init__ (self,root):
        self.root=root
        self.root.title("HOTEL MANAGEMENT SYSTEM")
        self.root.geometry("1140x520+210+165")
        
        ############ creating variables###########
        
        self.var_c_ref=StringVar()
        x=random.randint(1000,99999)
        self.var_c_ref.set(str(x))
        
        self.var_c_name=StringVar()
        self.var_m_name=StringVar()
        self.var_gender=StringVar() 
        self.var_zipcode=StringVar() 
        self.var_mobile=StringVar() 
        self.var_email=StringVar() 
        self.var_nationality=StringVar() 
        self.var_id_proof=StringVar() 
        self.var_id_number=StringVar() 
        self.var_address=StringVar() 
             
    
    # setting title
        lbl_title=Label(self.root,text="ADD CUSTOMER DETAILS",font=("times new roman",20,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1138,height=50)
    
    # logo for the page 
        
        img2=Image.open("C:\\Users\\sdher\\Desktop\\PyStay\\img\\logo.png")
        img2 = img2.resize((100,50),Image.Resampling.LANCZOS)
        self.photo_img2=ImageTk.PhotoImage(img2)
        
        lbl_img2=Label(self.root,image=self.photo_img2,bd=4,relief=RIDGE)
        lbl_img2.place(x=0,y=0,width=100,height=50)
        
    # Label frame
        
        label_frame_left=LabelFrame(self.root,bd=2,relief=SUNKEN,text="Customer Details",font=("arial",12,"bold"),bg="black",fg="pink")
        label_frame_left.place(x=5,y=50,width=425,height=455)
    
    ############### labels and entries ############################
        
        # customer reference
        lbl_customer=Label(label_frame_left,text="Customer Ref:",font=("arial",12,"bold"),padx=1,pady=5,bg="black",fg="pink")
        lbl_customer.grid(row=0,column=0,sticky=W)
    
        
        entry_ref=ttk.Entry(label_frame_left,textvariable=self.var_c_ref,width=29,font=("arial",12,"bold"),state="readonly")
        entry_ref.grid(row=0,column=1,sticky=W)
    
    
        # customer name
        cname=Label(label_frame_left,text="Customer's Name:",font=("arial",12,"bold"),padx=1,pady=5,bg="black",fg="pink")
        cname.grid(row=1,column=0,sticky=W)
    
        txt_cname=ttk.Entry(label_frame_left,textvariable=self.var_c_name,width=29,font=("arial",12,"bold"))
        txt_cname.grid(row=1,column=1,sticky=W)
        
        
        # mother name
        mname=Label(label_frame_left,text="Mother's Name:",font=("arial",12,"bold"),padx=1,pady=5,bg="black",fg="pink")
        mname.grid(row=2,column=0,sticky=W)
    
        txt_mname=ttk.Entry(label_frame_left,textvariable=self.var_m_name,width=29,font=("arial",12,"bold"))
        txt_mname.grid(row=2,column=1,sticky=W)
        
        # gender combo box
        lbl_gender=Label(label_frame_left,text="Gender:",font=("arial",12,"bold"),padx=1,pady=5,bg="black",fg="pink")
        lbl_gender.grid(row=3,column=0,sticky=W)
    
        combo_gender=ttk.Combobox(label_frame_left,textvariable=self.var_gender,font=("arial",12,"bold"),width=27,state="readonly")
        combo_gender["value"]=("Male","Female","Transgender","Other's")
        combo_gender.current(0)
        combo_gender.grid(row=3,column=1,sticky=W)
        
        
        # ZIP code
        lbl_zipcode=Label(label_frame_left,text="Zip-Code:",font=("arial",12,"bold"),padx=1,pady=5,bg="black",fg="pink")
        lbl_zipcode.grid(row=4,column=0,sticky=W)
    
        txt_zipcode=ttk.Entry(label_frame_left,width=29,textvariable=self.var_zipcode,font=("arial",12,"bold"))
        txt_zipcode.grid(row=4,column=1,sticky=W)
    
        
        # Mobile number
        lblMob=Label(label_frame_left,text="Mobile:",font=("arial",12,"bold"),padx=1,pady=5,bg="black",fg="pink")
        lblMob.grid(row=5,column=0,sticky=W)
        
        txt_mob=ttk.Entry(label_frame_left,textvariable=self.var_mobile,width=29,font=("arial",12,"bold"))
        txt_mob.grid(row=5,column=1,sticky=W)
        
        
        # Email
        lbl_email=Label(label_frame_left,text="Email:",font=("arial",12,"bold"),padx=1,pady=5,bg="black",fg="pink")
        lbl_email.grid(row=6,column=0,sticky=W)
    
        txt_email=ttk.Entry(label_frame_left,textvariable=self.var_email,width=29,font=("arial",12,"bold"))
        txt_email.grid(row=6,column=1,sticky=W)
    
        
        # Nationality combo box
        lbl_nationality=Label(label_frame_left,text="Nationality:",font=("arial",12,"bold"),padx=1,pady=5,bg="black",fg="pink")
        lbl_nationality.grid(row=7,column=0,sticky=W)
    
        combo_nationality=ttk.Combobox(label_frame_left,textvariable=self.var_nationality,font=("arial",12,"bold"),width=27,state="readonly")
        combo_nationality["value"]=("Indian","American","British","African","Other's")
        combo_nationality.current(0)
        combo_nationality.grid(row=7,column=1,sticky=W)
        
    
        # id Proof combo box
        lbl_id_proof=Label(label_frame_left,text="Id Proof Type:",font=("arial",12,"bold"),padx=1,pady=5,bg="black",fg="pink")
        lbl_id_proof.grid(row=8,column=0,sticky=W)
    
        combo_id_proof=ttk.Combobox(label_frame_left,textvariable=self.var_id_proof,font=("arial",12,"bold"),width=27,state="readonly")
        combo_id_proof["value"]=("Pan","Driving License","Passport","Other's")
        combo_id_proof.current(0)
        combo_id_proof.grid(row=8,column=1,sticky=W)
        
        
        # id number
        lbl_id_number=Label(label_frame_left,text="Id Number:",font=("arial",12,"bold"),padx=1,pady=5,bg="black",fg="pink")
        lbl_id_number.grid(row=9,column=0,sticky=W)
    
        txt_id_number=ttk.Entry(label_frame_left,textvariable=self.var_id_number,width=29,font=("arial",12,"bold"))
        txt_id_number.grid(row=9,column=1,sticky=W)
    
        # Address
        lbl_address=Label(label_frame_left,text="Address:",font=("arial",12,"bold"),padx=1,pady=5,bg="black",fg="pink")
        lbl_address.grid(row=10,column=0,sticky=W)
    
        txt_address=ttk.Entry(label_frame_left,textvariable=self.var_address,width=29,font=("arial",12,"bold"))
        txt_address.grid(row=10,column=1,sticky=W)
    
    
        ######################### creating frame for our buttons ##########################
        btn_frame=Frame(label_frame_left,bd=0,relief=SUNKEN,bg="black")
        btn_frame.place(x=0,y=365,width=412,height=80)
    
        # creating buttons
        # add button
        add_btn=Button(btn_frame,text="ADD",command=self.add_data,width=9,font=("arial",13,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
        add_btn.grid(row=0,column=0,padx=1,pady=18)
    
        # update button
        update_btn=Button(btn_frame,text="UPDATE",command=self.update,width=10,font=("arial",13,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
        update_btn.grid(row=0,column=1,padx=1,pady=18)
        
        # reset button
        reset_btn=Button(btn_frame,text="RESET",command=self.reset,width=9,font=("arial",13,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
        reset_btn.grid(row=0,column=2,padx=1,pady=18)
        
        # delete button
        del_btn=Button(btn_frame,text="DELETE",command=self.delete,width=11,font=("arial",13,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
        del_btn.grid(row=0,column=3,padx=1,pady=18)
    
        
        ###################  table frame of search system #############################
    
        table_frame=LabelFrame(self.root,bd=2,relief=SUNKEN,text="View Details & Search System",font=("arial",12,"bold"),bg="black",fg="pink")
        table_frame.place(x=435,y=50,width=700,height=455)
    
        ###################### creating label search by #################
        lbl_search=Label(table_frame,text="SearchBy:",font=("arial",12,"bold"),bg="blue",fg="black")
        lbl_search.grid(row=0,column=1,sticky=W,padx=2)
        self.search_var=StringVar()
        # creating combo box ############
        combo_search_by=ttk.Combobox(table_frame,textvariable=self.search_var,font=("arial",12,"bold"),width=20,state="readonly")
        combo_search_by["value"]=("Mobile","c_ref","id_number")
        combo_search_by.current(0)
        combo_search_by.grid(row=0,column=2,padx=2)
        
        # creating entry field for searching the customer#####
        self.txt_search=StringVar()
        txt_search=ttk.Entry(table_frame,textvariable=self.txt_search,width=21,font=("arial",12,"bold"))
        txt_search.grid(row=0,column=3,sticky=W,padx=2)
    
        # creating buttons####################
        # search button
        search_btn=Button(table_frame,text="SEARCH",command=self.search,width=9,font=("arial",12,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
        search_btn.grid(row=0,column=4,padx=1,pady=1)
        
        #show all button
        show_btn=Button(table_frame,text="SHOW ALL",command=self.fetch_data,width=9,font=("arial",12,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
        show_btn.grid(row=0,column=5,padx=1,pady=1)
    
    
        ###### SHOW DATA TABLE####################
        details_table=Frame(table_frame,bd=2,relief=SUNKEN,)
        details_table.place(x=0,y=50,width=690,height=380)
        
        # creating scroll bar
        scroll_x=ttk.Scrollbar(details_table,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(details_table,orient=VERTICAL)
        
        self.Customer_Details_Table=ttk.Treeview(details_table,column=("c_ref","c_name","m_name","gender","zipcode","mobile","email","nationality","id_proof","id_number","address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        
        scroll_x.config(command=self.Customer_Details_Table.xview)
        scroll_y.config(command=self.Customer_Details_Table.yview)
        
        ## displaying columns to the user #####################
        
        self.Customer_Details_Table.heading("c_ref",text="Reference No")
        self.Customer_Details_Table.heading("c_name",text="Name")
        self.Customer_Details_Table.heading("m_name",text="Mother's Name")
        self.Customer_Details_Table.heading("gender",text="Gender")
        self.Customer_Details_Table.heading("zipcode",text="ZipCode")
        self.Customer_Details_Table.heading("mobile",text="Mobile")
        self.Customer_Details_Table.heading("email",text="Email")
        self.Customer_Details_Table.heading("nationality",text="Nationality")
        self.Customer_Details_Table.heading("id_proof",text="Id Proof")
        self.Customer_Details_Table.heading("id_number",text="Id Number")
        self.Customer_Details_Table.heading("address",text="Address")
        
        # displaying columns with the help of show
        self.Customer_Details_Table["show"]="headings"
        
        # setting the width of columns
        self.Customer_Details_Table.column("c_ref",width=100)
        self.Customer_Details_Table.column("c_name",width=100)
        self.Customer_Details_Table.column("m_name",width=100)
        self.Customer_Details_Table.column("gender",width=100)
        self.Customer_Details_Table.column("zipcode",width=100)
        self.Customer_Details_Table.column("mobile",width=100)
        self.Customer_Details_Table.column("email",width=100)
        self.Customer_Details_Table.column("nationality",width=100)
        self.Customer_Details_Table.column("id_proof",width=100)
        self.Customer_Details_Table.column("id_number",width=100)
        self.Customer_Details_Table.column("address",width=100)
        
        ## packing our table
        self.Customer_Details_Table.pack(fill=BOTH,expand=1)    
        self.Customer_Details_Table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data() # calling the function after the customer is added to display his/her details
        
    # creating our functions for button functionality
    
    def add_data(self):
        if self.var_mobile.get()=="" or self.var_id_proof.get()=="":
            messagebox.showerror("ERROR","ALL FIELDS ARE REQUIRED",parent=self.root)
        elif self.var_email.get()=="" or self.var_id_number.get()=="":
            messagebox.showerror("MANDATORY SECTION","ALL FIELDS ARE REQUIRED",parent=self.root)
        elif self.var_gender.get()=="" or self.var_zipcode.get()=="":
            messagebox.showerror("ERROR","ALL FIELDS ARE REQUIRED",parent=self.root)
        else:
            try:
                conn=database.get_db_connection()
                my_cursor=conn.cursor()
                my_cursor.execute("INSERT INTO Customer VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                    self.var_c_ref.get(),
                                                                                                    self.var_c_name.get(),
                                                                                                    self.var_m_name.get(),
                                                                                                    self.var_gender.get(),
                                                                                                    self.var_zipcode.get(),
                                                                                                    self.var_mobile.get(),
                                                                                                    self.var_email.get(),
                                                                                                    self.var_nationality.get(),
                                                                                                    self.var_id_proof.get(),
                                                                                                    self.var_id_number.get(),
                                                                                                    self.var_address.get()
                                                                                                        ))
                conn.commit()
                self.fetch_data() # calling the function 
                conn.close()
                messagebox.showinfo("Success","Customer Has Been Added",parent=self.root)
            except:
                messagebox.showwarning("Warning","Something Went Wrong:",parent=self.root)   
                
    # creating a function named as fetch_data.    
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="root",database="hoteldb")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from Customer")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.Customer_Details_Table.delete(*self.Customer_Details_Table.get_children())
            for i in rows:
                self.Customer_Details_Table.insert("",END,values=i)
        conn.commit()
        conn.close()
            
        
    #creating a function so that if we click in our table columns the inserted data will automatically render in entry fields  
    # creating this because it will help us to update
    def get_cursor(self,event=""):
        cursor_row=self.Customer_Details_Table.focus()
        content=self.Customer_Details_Table.item(cursor_row)
        row=content["values"]
        
        self.var_c_ref.set(row[0]),
        self.var_c_name.set(row[1]),
        self.var_m_name.set(row[2]),
        self.var_gender.set(row[3]),
        self.var_zipcode.set(row[4]),
        self.var_mobile.set(row[5]),
        self.var_email.set(row[6]),
        self.var_nationality.set(row[7]),
        self.var_id_proof.set(row[8]),
        self.var_id_number.set(row[9]),
        self.var_address.set(row[10])
        
    # creating function for update
    def update(self):
        if self.var_mobile.get()=="":
            messagebox.showerror("ERROR","Please Enter Your Mobile Number",parent=self.root)
        else:    
            conn=database.get_db_connection()
            my_cursor=conn.cursor()
            my_cursor.execute("update Customer set c_name=%s,m_name=%s,gender=%s,zipcode=%s,mobile=%s,email=%s,nationality=%s,id_proof=%s,id_number=%s,address=%s where c_ref=%s",(
                                                                                                                                                                        
                                                                                                                                                                        self.var_c_name.get(),
                                                                                                                                                                        self.var_m_name.get(),
                                                                                                                                                                        self.var_gender.get(),
                                                                                                                                                                        self.var_zipcode.get(),
                                                                                                                                                                        self.var_mobile.get(),
                                                                                                                                                                        self.var_email.get(),
                                                                                                                                                                        self.var_nationality.get(),
                                                                                                                                                                        self.var_id_proof.get(),
                                                                                                                                                                        self.var_id_number.get(),
                                                                                                                                                                        self.var_address.get(),
                                                                                                                                                                        self.var_c_ref.get()    
                                                                                                                                                                            ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("UPDATE","Customer Details Has Been Updated")
       
    
    
    # CREATING function for delete
    def delete(self):
        delete=messagebox.askyesno("PyStay","Do You Want To Delete This Customer",parent=self.root)
        if delete>0:
            conn=database.get_db_connection()
            my_cursor=conn.cursor()
            query="delete from Customer where c_ref=%s"
            value=(self.var_c_ref.get(),)
            my_cursor.execute(query,value)
           
        else:
            if not delete:
                return
        conn.commit()
        self.fetch_data()
        conn.close()
    
    
    # creating function to reset
    def reset(self):
        #self.var_c_ref.set(""),
        self.var_c_name.set(""),
        self.var_m_name.set(""),
        #self.var_gender.set(""),
        self.var_zipcode.set(""),
        self.var_mobile.set(""),
        self.var_email.set(""),
        #self.var_nationality.set(""),
        #self.var_id_proof.set(""),
        self.var_id_number.set(""),
        self.var_address.set("")
        
        x=random.randint(1000,99999)
        self.var_c_ref.set(str(x))
    
    # creating a function for search 
    # it will help us to search for the customer
    
    def search(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="root",database="hoteldb")
        my_cursor=conn.cursor()
        my_cursor.execute(
        "select * from Customer where " +
        self.search_var.get() +
        " LIKE '%" + self.txt_search.get() + "%'"
        )
        row=my_cursor.fetchall()
        if len(row)!=0:
            self.Customer_Details_Table.delete(*self.Customer_Details_Table.get_children())
            for i in row:
                self.Customer_Details_Table.insert("",END,values=i)
        conn.commit()
        conn.close()        
    
    
    
    
    
    
    
    
    
    
if __name__ == "__main__":
    root=Tk()
    obj=Customer_Window(root)
    root.mainloop()