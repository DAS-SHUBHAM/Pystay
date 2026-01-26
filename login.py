import tkinter as tk
from tkinter import messagebox, ttk
import database
import hotel

class CleanLoginApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management System")
        self.root.geometry("800x500") 
        self.root.configure(bg="#0f172a")
        
        # Center the window
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = (screen_width - 800) // 2
        y = (screen_height - 500) // 2
        self.root.geometry(f"800x500+{x}+{y}")
        self.root.resizable(False, False)

        # Fade in effect variables
        self.root.attributes("-alpha", 0.0)
        self.fade_alpha = 0.0
        
        # UI Setup
        self.setup_ui()
        
        # Start animations
        self.fade_in()
        self.slide_up_animation()

    def setup_ui(self):
        # Main Canvas for background and card shape
        self.canvas = tk.Canvas(self.root, bg="#0f172a", bd=0, highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)

        # Draw subtle background shapes
        self.draw_background_shapes()

        # Login Card Container (Initially off-screen for animation)
        self.card_y = 600 # Start below screen
        self.target_card_y = 25 # Target Y position (centered)
        
        # Card dimensions - Restored compact size
        self.card_width = 400
        self.card_height = 450 
        self.card_x = (800 - self.card_width) // 2
        
        # Draw initial card shape on canvas
        self.card_item = self.canvas.create_polygon(
            self.get_rounded_rect_coords(self.card_x, self.card_y, self.card_width, self.card_height, 20),
            smooth=True, fill="#020617", outline="#1e293b", width=1
        )
        
        # Frame to hold the input widgets
        self.main_frame = tk.Frame(self.root, bg="#020617")
        
        # Initialize with Login View
        self.show_login_view()

    def clear_frame(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()

    def show_login_view(self):
        self.clear_frame()
        
        # Title
        tk.Label(self.main_frame, text="Welcome Back", font=("Segoe UI", 20, "bold"), bg="#020617", fg="#f8fafc").pack(pady=(20, 5))
        tk.Label(self.main_frame, text="Sign in to continue", font=("Segoe UI", 10), bg="#020617", fg="#94a3b8").pack(pady=(0, 25))

        # Inputs
        self.login_user_entry = self.create_input_field(self.main_frame, "Username")
        self.login_pass_entry = self.create_input_field(self.main_frame, "Password", is_password=True)
        
        # Login Button
        login_btn = tk.Button(self.main_frame, text="Log In", font=("Segoe UI", 11, "bold"), 
                                   bg="#38bdf8", fg="#0f172a", activebackground="#0ea5e9", activeforeground="#0f172a",
                                   bd=0, cursor="hand2", width=25, pady=8, command=self.perform_login)
        login_btn.pack(pady=20)
        
        login_btn.bind("<Enter>", lambda e: e.widget.config(bg="#0ea5e9"))
        login_btn.bind("<Leave>", lambda e: e.widget.config(bg="#38bdf8"))

        # Switch to Register
        tk.Button(self.main_frame, text="Don't have an account? Sign Up", font=("Segoe UI", 9), 
                  bg="#020617", fg="#38bdf8", activebackground="#020617", activeforeground="#0ea5e9",
                  bd=0, cursor="hand2", command=self.show_register_view).pack()

        # Status Label
        self.status_label = tk.Label(self.main_frame, text="", font=("Segoe UI", 9), bg="#020617", fg="#ef4444")
        self.status_label.pack(pady=10)

    def show_register_view(self):
        self.clear_frame()
        
        # Title
        tk.Label(self.main_frame, text="Create Account", font=("Segoe UI", 20, "bold"), bg="#020617", fg="#f8fafc").pack(pady=(15, 5))
        tk.Label(self.main_frame, text="Join us today", font=("Segoe UI", 10), bg="#020617", fg="#94a3b8").pack(pady=(0, 15))

        # Inputs
        self.reg_user_entry = self.create_input_field(self.main_frame, "Username")
        self.reg_pass_entry = self.create_input_field(self.main_frame, "Password", is_password=True)
        
        # Register Button
        reg_btn = tk.Button(self.main_frame, text="Sign Up", font=("Segoe UI", 11, "bold"), 
                                   bg="#22c55e", fg="#0f172a", activebackground="#16a34a", activeforeground="#0f172a",
                                   bd=0, cursor="hand2", width=25, pady=8, command=self.perform_register)
        reg_btn.pack(pady=15)
        
        reg_btn.bind("<Enter>", lambda e: e.widget.config(bg="#16a34a"))
        reg_btn.bind("<Leave>", lambda e: e.widget.config(bg="#22c55e"))

        # Switch to Login
        tk.Button(self.main_frame, text="Already have an account? Sign In", font=("Segoe UI", 9), 
                  bg="#020617", fg="#38bdf8", activebackground="#020617", activeforeground="#0ea5e9",
                  bd=0, cursor="hand2", command=self.show_login_view).pack()

        # Status Label
        self.status_label = tk.Label(self.main_frame, text="", font=("Segoe UI", 9), bg="#020617", fg="#ef4444")
        self.status_label.pack(pady=5)

    def create_input_field(self, parent, placeholder, is_password=False):
        container = tk.Frame(parent, bg="#020617")
        container.pack(pady=5, padx=30, fill="x")
        
        tk.Label(container, text=placeholder, font=("Segoe UI", 9), bg="#020617", fg="#64748b", anchor="w").pack(fill="x")
        
        entry = tk.Entry(container, font=("Segoe UI", 11), bg="#1e293b", fg="white", 
                         bd=0, highlightthickness=2, highlightbackground="#1e293b", highlightcolor="#38bdf8",
                         insertbackground="white")
        if is_password:
            entry.config(show="•")
        
        entry.pack(fill="x", ipady=6)
        return entry

    def draw_background_shapes(self):
        self.canvas.create_oval(-50, -50, 200, 200, fill="#132038", outline="")
        self.canvas.create_oval(600, 400, 900, 700, fill="#132038", outline="")

    def get_rounded_rect_coords(self, x, y, w, h, r):
        return [x+r, y, x+w-r, y, x+w, y, x+w, y+r, x+w, y+h-r, x+w, y+h, x+w-r, y+h, x+r, y+h, x, y+h, x, y+h-r, x, y+r, x, y, x+r, y]

    def fade_in(self):
        if self.fade_alpha < 1.0:
            self.fade_alpha += 0.05
            self.root.attributes("-alpha", self.fade_alpha)
            self.root.after(25, self.fade_in)

    def slide_up_animation(self):
        step = (self.card_y - self.target_card_y) / 10
        if self.card_y > self.target_card_y:
            self.card_y -= step
            if self.card_y < self.target_card_y: 
                self.card_y = self.target_card_y

            self.canvas.coords(self.card_item, self.get_rounded_rect_coords(self.card_x, self.card_y, self.card_width, self.card_height, 20))
            self.main_frame.place(x=self.card_x + 20, y=self.card_y + 20, width=self.card_width - 40, height=self.card_height - 40)
            
            if self.card_y > self.target_card_y:
                self.root.after(16, self.slide_up_animation)
        else:
            self.card_y = self.target_card_y
            self.canvas.coords(self.card_item, self.get_rounded_rect_coords(self.card_x, self.card_y, self.card_width, self.card_height, 20))
            self.main_frame.place(x=self.card_x + 20, y=self.card_y + 20, width=self.card_width - 40, height=self.card_height - 40)

    def shake_card(self, count=0, direction=1):
        if count < 10:
            offset = 5 * direction
            self.main_frame.place(x=self.card_x + 20 + offset, y=self.target_card_y + 20)
            self.root.after(40, lambda: self.shake_card(count+1, direction*-1))
        else:
            self.main_frame.place(x=self.card_x + 20, y=self.target_card_y + 20)

    def perform_login(self):
        username = self.login_user_entry.get()
        password = self.login_pass_entry.get()

        if not username or not password:
            self.status_label.config(text="Please fill in all fields", fg="#ef4444")
            self.shake_card()
            return

        try:
            if database.verify_login(username, password):
                self.status_label.config(text="Login Successful!", fg="#22c55e")
                self.root.after(500, self.launch_hotel)
            else:
                self.status_label.config(text="Invalid credentials", fg="#ef4444")
                self.shake_card()
        except Exception as e:
            self.status_label.config(text="Database Error", fg="#ef4444")
            print(f"Error: {e}")

    def perform_register(self):
        username = self.reg_user_entry.get()
        password = self.reg_pass_entry.get()

        if not username or not password:
            self.status_label.config(text="All fields are required", fg="#ef4444")
            self.shake_card()
            return

        try:
            if database.register_user(username, password):
                messagebox.showinfo("Success", "Account Created Successfully!")
                self.show_login_view()
            else:
                self.status_label.config(text="Username already exists", fg="#ef4444")
                self.shake_card()
        except Exception as e:
            self.status_label.config(text="Registration Failed", fg="#ef4444")
            print(f"Error: {e}")

    def launch_hotel(self):
        self.root.destroy()
        root = tk.Tk()
        app = hotel.HotelManagementSystem(root)
        root.mainloop()

if __name__ == "__main__":
    try:
        root = tk.Tk()
        app = CleanLoginApp(root)
        root.mainloop()
    except Exception as e:
        print(f"Startup Error: {e}")
