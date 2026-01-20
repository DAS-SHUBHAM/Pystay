from tkinter import*
from PIL import Image,ImageTk
from customer import Customer_Window
from room import Room_Booking


class HotelManagementSystem:
    def __init__(self,root):
        self.root=root
        self.root.title("PyStay")
        self.root.geometry("1550x100+0+0")
        
        # declaring a variable for our image named as img1
        # setting it's path from where the img will come
        # First image
        img1=Image.open("C:\\Users\\sdher\\Desktop\\PyStay\\img\\hotels.jpg")
        img1 = img1.resize((1550,140), Image.Resampling.LANCZOS)
        self.photo_img1=ImageTk.PhotoImage(img1)
        
        lbl_img1=Label(self.root,image=self.photo_img1,bd=4,relief=RIDGE)
        lbl_img1.place(x=0,y=0,width=1550,height=140)
        
        # logo for the page 
        # setting the logo
        # second image
        
        img2=Image.open("C:\\Users\\sdher\\Desktop\\PyStay\\img\\logo.png")
        img2 = img2.resize((230,140),Image.Resampling.LANCZOS)
        self.photo_img2=ImageTk.PhotoImage(img2)
        
        lbl_img2=Label(self.root,image=self.photo_img2,bd=4,relief=RIDGE)
        lbl_img2.place(x=0,y=0,width=230,height=140)
        
        # setting title
        lbl_title=Label(self.root,text="HOTEL MANAGEMENT SYSTEM",font=("times new roman",30,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=135,width=1400,height=50)
        
        
        # creating a frame
        main_frame=Frame(self.root,bd=4,relief=RIDGE)
        main_frame.place(x=0,y=180,width=1500,height=515)
        
        # creating menu label and setting it
        lbl_menu=Label(main_frame,text="MENU",font=("times new roman",20,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_menu.place(x=0,y=0,width=212)
        
        # creating a button frame
        btn_frame=Frame(main_frame,bd=4,relief=RIDGE)
        btn_frame.place(x=0,y=35,width=212,height=152)
        
        
        # creating buttons inside menu frame
        # creating a button as a customer button
        customer_btn=Button(btn_frame,text="CUSTOMER",command=self.customer_details,width=22,font=("times new roman",12,"bold"),bg="black",fg="pink",bd=0,cursor="hand1")
        customer_btn.grid(row=0,column=1)
        
        # ROOM BUTTON
        room_btn=Button(btn_frame,text="ROOMS",command=self.room_booking,width=22,font=("times new roman",12,"bold"),bg="black",fg="pink",bd=0,cursor="hand1")
        room_btn.grid(row=1,column=1)
        
        # DETAILS BUTTON
        det_btn=Button(btn_frame,text="DETAILS",width=22,font=("times new roman",12,"bold"),bg="black",fg="pink",bd=0,cursor="hand1")
        det_btn.grid(row=2,column=1)
        
        # REPORT BUTTON
        rep_btn=Button(btn_frame,text="REPORT",width=22,font=("times new roman",12,"bold"),bg="black",fg="pink",bd=0,cursor="hand1")
        rep_btn.grid(row=3,column=1)
        
        # LOGOUT BUTTON
        log_btn=Button(btn_frame,text="LOGOUT",width=22,font=("times new roman",12,"bold"),bg="black",fg="pink",bd=0,cursor="hand1")
        log_btn.grid(row=4,column=1)
        
        ########################## right side image ############################33
        
        
        img3=Image.open("C:\\Users\\sdher\\Desktop\\PyStay\\img\\counter.jpg")
        img3 = img3.resize((1155,323),Image.Resampling.LANCZOS)
        self.photo_img3=ImageTk.PhotoImage(img3)
        
        lbl_img3=Label(main_frame,image=self.photo_img3,bd=4,relief=RIDGE)
        lbl_img3.place(x=208,y=185,width=1155,height=323)
        
        ############################ images under menu section #####################
        
        img4=Image.open("C:\\Users\\sdher\\Desktop\\PyStay\\img\\res.jpg")
        img4 = img4.resize((210,160),Image.Resampling.LANCZOS)
        self.photo_img4=ImageTk.PhotoImage(img4)
        
        lbl_img4=Label(main_frame,image=self.photo_img4,bd=4,relief=RIDGE)
        lbl_img4.place(x=0,y=185,width=210,height=160)
        
        
        img5=Image.open("C:\\Users\\sdher\\Desktop\\PyStay\\img\\swimming.jpg")
        img5 = img5.resize((210,160),Image.Resampling.LANCZOS)
        self.photo_img5=ImageTk.PhotoImage(img5)
        
        lbl_img5=Label(main_frame,image=self.photo_img5,bd=4,relief=RIDGE)
        lbl_img5.place(x=0,y=345,width=210,height=165)
        
        
        ############################## images upper right image ##############################
        
        img6=Image.open("C:\\Users\\sdher\\Desktop\\PyStay\\img\\bedroom.jpg")
        img6 = img6.resize((200,185),Image.Resampling.LANCZOS)
        self.photo_img6=ImageTk.PhotoImage(img6)
        
        lbl_img6=Label(main_frame,image=self.photo_img6,bd=4,relief=RIDGE)
        lbl_img6.place(x=210,y=0,width=200,height=185)
        
        
        img7=Image.open("C:\\Users\\sdher\\Desktop\\PyStay\\img\\snooker.jpg")
        img7 = img7.resize((200,185),Image.Resampling.LANCZOS)
        self.photo_img7=ImageTk.PhotoImage(img7)
        
        lbl_img7=Label(main_frame,image=self.photo_img7,bd=4,relief=RIDGE)
        lbl_img7.place(x=410,y=0,width=200,height=185)
        
        img8=Image.open("C:\\Users\\sdher\\Desktop\\PyStay\\img\\food.jpg")
        img8 = img8.resize((200,185),Image.Resampling.LANCZOS)
        self.photo_img8=ImageTk.PhotoImage(img8)
        
        lbl_img8=Label(main_frame,image=self.photo_img8,bd=4,relief=RIDGE)
        lbl_img8.place(x=610,y=0,width=200,height=185)
        
        
        img9=Image.open("C:\\Users\\sdher\\Desktop\\PyStay\\img\\club.jpg")
        img9 = img9.resize((200,185),Image.Resampling.LANCZOS)
        self.photo_img9=ImageTk.PhotoImage(img9)
        
        lbl_img9=Label(main_frame,image=self.photo_img9,bd=4,relief=RIDGE)
        lbl_img9.place(x=810,y=0,width=200,height=185)
        
        
        img10=Image.open("C:\\Users\\sdher\\Desktop\\PyStay\\img\\bar.jpg")
        img10 = img10.resize((200,185),Image.Resampling.LANCZOS)
        self.photo_img10=ImageTk.PhotoImage(img10)
        
        lbl_img10=Label(main_frame,image=self.photo_img10,bd=4,relief=RIDGE)
        lbl_img10.place(x=1010,y=0,width=200,height=185)
        
        
        img11=Image.open("C:\\Users\\sdher\\Desktop\\PyStay\\img\\hll.jpg")
        img11 = img11.resize((150,185),Image.Resampling.LANCZOS)
        self.photo_img11=ImageTk.PhotoImage(img11)
        
        lbl_img11=Label(main_frame,image=self.photo_img11,bd=4,relief=RIDGE)
        lbl_img11.place(x=1210,y=0,width=150,height=185)
        
    ############################ creating function that connects our customer file ############################
    def customer_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Customer_Window(self.new_window)
        
    ########################### creating function that connects our room file ############################    
    def room_booking(self):
        self.new_window=Toplevel(self.root)
        self.app=Room_Booking(self.new_window)
        
        
        
"""     
def animate_title_color(self):
        colors=["red","green","blue","yellow","gold","orange"]
        self.lbl_title.config(fg=colors[self.color_index])
        self.color_index =self.color_index+1
        if self.color_index>=len(colors):
            self.color_index=0
        self.root.after(300, self.animate_title_color)   
        
        
        
        
        self.color_index=0
        self.animate_title_color()
        
        self.move_title()
        self.animate_title_color()
        
"""
    
        
        
        
        
        
        
        
if __name__ == "__main__":
    root=Tk()
    obj=HotelManagementSystem(root)
    root.mainloop()
   