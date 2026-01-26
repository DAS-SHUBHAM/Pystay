from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk
import random
import mysql.connector
import database
from tkinter import messagebox
from time import strftime
from datetime import datetime

class Room_Details:
    def __init__ (self,root):
        self.root=root
        self.root.title("ROOM DETAILS PAGE")
        self.root.geometry("950x325+210+165")
        
        # setting title
        lbl_title=Label(self.root,text="ROOM BOOKING INFORMATION",font=("times new roman",20,"bold"),bg="black",fg="pink",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=950,height=50)
    
        # logo for the page 
        
        img2=Image.open("C:\\Users\\sdher\\Desktop\\PyStay\\img\\logo.png")
        img2 = img2.resize((100,50),Image.Resampling.LANCZOS)
        self.photo_img2=ImageTk.PhotoImage(img2)
        
        lbl_img2=Label(self.root,image=self.photo_img2,bd=4,relief=RIDGE)
        lbl_img2.place(x=0,y=0,width=100,height=50)
        
        # Label frame
        label_frame_left=LabelFrame(self.root,bd=2,relief=SUNKEN,text="ADDING FLOORS & ROOMS",font=("arial",12,"bold"),bg="black",fg="pink")
        label_frame_left.place(x=5,y=50,width=500,height=270)
        
        # Floor Details
        lbl_FLOOR=Label(label_frame_left,text="FLOOR:",font=("arial",12,"bold"),padx=1,pady=5,bg="black",fg="pink")
        lbl_FLOOR.grid(row=0,column=0,sticky=W)
        
        self.var_floor=StringVar()
        entry_FLOOR=ttk.Entry(label_frame_left,textvariable=self.var_floor,width=20,font=("arial",12,"bold"),foreground="blue")
        entry_FLOOR.grid(row=0,column=1,sticky=W)
        
         #Room-Type
        lbl_room_type=Label(label_frame_left,text="RoomType:",font=("arial",12,"bold"),padx=1,pady=5,bg="black",fg="pink")
        lbl_room_type.grid(row=1,column=0,sticky=W)
        
        self.var_RoomType=StringVar()
        entry_room_type=ttk.Entry(label_frame_left,textvariable=self.var_RoomType,width=29,font=("arial",12,"bold"),foreground="blue")
        entry_room_type.grid(row=1,column=1,sticky=W)
        
        #RoomNumber
        lbl_RoomNumber=Label(label_frame_left,text="RoomNumber:",font=("arial",12,"bold"),padx=1,pady=2,bg="black",fg="pink")
        lbl_RoomNumber.grid(row=2,column=0,sticky=W)
        
        self.var_RoomNo=StringVar()
        entry_RoomNumber=ttk.Entry(label_frame_left,textvariable=self.var_RoomNo,width=29,font=("arial",12,"bold"),foreground="blue")
        entry_RoomNumber.grid(row=2,column=1,sticky=W)
        
        # creating buttons to perform some operations
        # add button
        add_btn=Button(label_frame_left,text="ADD",command=self.add_data,width=9,font=("arial",13,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
        add_btn.place(x=0,y=100)
    
        # update button
        update_btn=Button(label_frame_left,text="UPDATE",command=self.update,width=9,font=("arial",13,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
        update_btn.place(x=100,y=100)
        
        # reset button
        reset_btn=Button(label_frame_left,text="RESET",command=self.reset,width=9,font=("arial",13,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
        reset_btn.place(x=200,y=100)
        
        # delete button
        del_btn=Button(label_frame_left,text="DELETE",command=self.delete,width=11,font=("arial",13,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
        del_btn.place(x=300,y=100)
        
        ###################### creating table frame and label search by #################
        table_frame=LabelFrame(self.root,bd=2,relief=SUNKEN,text="SHOW ROOM DETAILS",font=("arial",12,"bold"),bg="black",fg="pink")
        table_frame.place(x=505,y=50,width=445,height=270)
        
        # creating scroll bar
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        
        self.Room_Table=ttk.Treeview(table_frame,column=("Floor","RoomType","RoomNumber"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        
        scroll_x.config(command=self.Room_Table.xview)
        scroll_y.config(command=self.Room_Table.yview)
        
         ## displaying columns to the user #####################
        
        self.Room_Table.heading("Floor",text="Floor")
        self.Room_Table.heading("RoomType",text="RoomType")
        self.Room_Table.heading("RoomNumber",text="RoomNumber")
        
        
        
        # displaying columns with the help of show
        self.Room_Table["show"]="headings"
        
        # setting the width of columns
        self.Room_Table.column("Floor",width=100)
        self.Room_Table.column("RoomType",width=100)
        self.Room_Table.column("RoomNumber",width=100)
        
        ## packing our table
        self.Room_Table.pack(fill=BOTH,expand=1) 
        self.Room_Table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()
        
    #creating function to add data
    def add_data(self):
            if self.var_floor.get()=="" or self.var_RoomType.get()=="":
                messagebox.showerror("ERROR","ALL FIELDS ARE REQUIRED",parent=self.root)
            else:
                try:
                    conn=database.get_db_connection()
                    my_cursor=conn.cursor()
                    my_cursor.execute("INSERT INTO details VALUES (%s,%s,%s)",(
                                                                                                            self.var_floor.get(),
                                                                                                            self.var_RoomType.get(),
                                                                                                            self.var_RoomNo.get(),
                                                                                                            
                                                                                                        ))
                    conn.commit()
                    self.fetch_data() # calling the function 
                    conn.close()
                    messagebox.showinfo("Success","New Room Added",parent=self.root)
                except:
                    messagebox.showwarning("Warning","Something Went Wrong:",parent=self.root)    
        
    # fetch data   
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="root",database="hoteldb")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from details")
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
        
        self.var_floor.set(row[0])
        self.var_RoomType.set(row[1])
        self.var_RoomNo.set(row[2])
        
    # creating update function
    def update(self):
        if self.var_floor.get()=="":
            messagebox.showerror("ERROR","Please Enter Your Floor Number",parent=self.root)
        else:    
            conn=mysql.connector.connect(host="localhost",username="root",password="root",database="hoteldb")
            my_cursor=conn.cursor()
            my_cursor.execute("update details set floor=%s,RoomType=%s where RoomNumber=%s",(
                                                                                                                                                                        
                                                                                                self.var_floor.get(),
                                                                                                self.var_RoomType.get(),
                                                                                                self.var_RoomNo.get()
                                                                                                                                                                       
                                                                                            ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("UPDATE","Room Details Has Been Updated",parent=self.root)   
        
        
    # creating function for delete
    def delete(self):
        delete=messagebox.askyesno("PyStay","Do You Want To Delete The Room Details",parent=self.root)
        if delete>0:
            conn=database.get_db_connection()
            my_cursor=conn.cursor()
            query="delete from details where RoomNumber=%s"
            value=(self.var_RoomNo.get(),)
            my_cursor.execute(query,value)
           
        else:
            if not delete:
                return
        conn.commit()
        self.fetch_data()
        conn.close()    
         
    # creating function for reset
    def reset(self):
        self.var_floor.set("")
        self.var_RoomNo.set("")
        self.var_RoomType.set("")

                
        
        
            
        
if __name__ == "__main__":
    root=Tk()
    obj=Room_Details(root)
    root.mainloop()