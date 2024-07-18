import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3
from datetime import datetime

class CycleRentalApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Cycle Rental System")
        self.user_id = None  # Initialize user_id attribute
        self.username = None  # Initialize username attribute
        
        # Create frames
        self.create_frames()
        
        # Show login frame
        self.show_frame(self.login_frame)
    
    def create_frames(self):
        self.login_frame = tk.Frame(self.root)
        self.signup_frame = tk.Frame(self.root)
        self.rental_frame = tk.Frame(self.root)
        
        self.create_login_frame()
        self.create_signup_frame()
        self.create_rental_frame()
    
    def show_frame(self, frame):
        frame.tkraise()
    
    def create_login_frame(self):
        tk.Label(self.login_frame, text="Login", font=('Helvetica', 18, 'bold')).grid(row=0, column=0, columnspan=2, pady=10)
        tk.Label(self.login_frame, text="Username").grid(row=1, column=0)
        tk.Label(self.login_frame, text="Password").grid(row=2, column=0)
        
        self.login_username_entry = tk.Entry(self.login_frame)
        self.login_password_entry = tk.Entry(self.login_frame, show="*")
        
        self.login_username_entry.grid(row=1, column=1)
        self.login_password_entry.grid(row=2, column=1)
        
        tk.Button(self.login_frame, text="Login", command=self.login).grid(row=3, column=0, columnspan=2, pady=5)
        tk.Button(self.login_frame, text="Sign Up", command=lambda: self.show_frame(self.signup_frame)).grid(row=4, column=0, columnspan=2)
        
        self.login_frame.grid(row=0, column=0, sticky='nsew')
    
    def create_signup_frame(self):
        tk.Label(self.signup_frame, text="Sign Up", font=('Helvetica', 18, 'bold')).grid(row=0, column=0, columnspan=2, pady=10)
        tk.Label(self.signup_frame, text="Username").grid(row=1, column=0)
        tk.Label(self.signup_frame, text="Password").grid(row=2, column=0)
        
        self.signup_username_entry = tk.Entry(self.signup_frame)
        self.signup_password_entry = tk.Entry(self.signup_frame, show="*")
        
        self.signup_username_entry.grid(row=1, column=1)
        self.signup_password_entry.grid(row=2, column=1)
        
        tk.Button(self.signup_frame, text="Sign Up", command=self.signup).grid(row=3, column=0, columnspan=2, pady=5)
        tk.Button(self.signup_frame, text="Back to Login", command=lambda: self.show_frame(self.login_frame)).grid(row=4, column=0, columnspan=2)
        
        self.signup_frame.grid(row=0, column=0, sticky='nsew')
    
    def create_rental_frame(self):
        tk.Label(self.rental_frame, text="Cycle Rental", font=('Helvetica', 18, 'bold')).grid(row=0, column=0, columnspan=2, pady=10)
        tk.Label(self.rental_frame, text="User ID").grid(row=1, column=0)
        tk.Label(self.rental_frame, text="Username").grid(row=2, column=0)
        tk.Label(self.rental_frame, text="Cycle Number").grid(row=3, column=0)
        tk.Label(self.rental_frame, text="Rental Time").grid(row=4, column=0)
        tk.Label(self.rental_frame, text="Return Time").grid(row=5, column=0)
        
        self.user_id_label = tk.Label(self.rental_frame, text="")
        self.username_label = tk.Label(self.rental_frame, text="")
        self.cycle_number_combobox = ttk.Combobox(self.rental_frame, values=[str(i) for i in range(1, 11)])
        
        # Rental time components
        self.rental_hour_combobox = ttk.Combobox(self.rental_frame, values=[f"{h:02d}" for h in range(1, 13)])
        self.rental_minute_combobox = ttk.Combobox(self.rental_frame, values=[f"{m:02d}" for m in range(0, 60)])
        self.rental_ampm_combobox = ttk.Combobox(self.rental_frame, values=['AM', 'PM'])
        
        # Return time components
        self.return_hour_combobox = ttk.Combobox(self.rental_frame, values=[f"{h:02d}" for h in range(1, 13)])
        self.return_minute_combobox = ttk.Combobox(self.rental_frame, values=[f"{m:02d}" for m in range(0, 60)])
        self.return_ampm_combobox = ttk.Combobox(self.rental_frame, values=['AM', 'PM'])
        
        self.user_id_label.grid(row=1, column=1)
        self.username_label.grid(row=2, column=1)
        self.cycle_number_combobox.grid(row=3, column=1)
        
        # Positioning rental time components
        self.rental_hour_combobox.grid(row=4, column=1, padx=5)
        tk.Label(self.rental_frame, text=":").grid(row=4, column=2)
        self.rental_minute_combobox.grid(row=4, column=3, padx=5)
        self.rental_ampm_combobox.grid(row=4, column=4, padx=5)
        
        # Positioning return time components
        self.return_hour_combobox.grid(row=5, column=1, padx=5)
        tk.Label(self.rental_frame, text=":").grid(row=5, column=2)
        self.return_minute_combobox.grid(row=5, column=3, padx=5)
        self.return_ampm_combobox.grid(row=5, column=4, padx=5)
        
        tk.Button(self.rental_frame, text="Log Rental", command=self.log_rental_gui).grid(row=6, column=0, columnspan=2, pady=5)
        tk.Button(self.rental_frame, text="Update Return", command=self.update_return).grid(row=7, column=0, columnspan=2, pady=5)
        tk.Button(self.rental_frame, text="Show Rental History", command=self.show_rental_history).grid(row=8, column=0, columnspan=2, pady=5)
        tk.Button(self.rental_frame, text="Logout", command=self.logout).grid(row=9, column=0, columnspan=2, pady=5)
        
        self.rental_frame.grid(row=0, column=0, sticky='nsew')
    
    def log_rental_gui(self):
        cycle_number = self.cycle_number_combobox.get()
        rental_hour = self.rental_hour_combobox.get()
        rental_minute = self.rental_minute_combobox.get()
        rental_ampm = self.rental_ampm_combobox.get()
        return_hour = self.return_hour_combobox.get()
        return_minute = self.return_minute_combobox.get()
        return_ampm = self.return_ampm_combobox.get()
        
        rental_time = f"{rental_hour}:{rental_minute} {rental_ampm}"
        return_time = f"{return_hour}:{return_minute} {return_ampm}" if return_hour and return_minute and return_ampm else None
        
        if self.user_id and self.username and cycle_number and rental_time:
            log_rental(self.user_id, self.username, cycle_number, rental_time, return_time)
            messagebox.showinfo("Success", "Rental logged successfully")
        else:
            messagebox.showerror("Error", "Please fill all fields")
    
    def update_return(self):
        cycle_number = self.cycle_number_combobox.get()
        return_hour = self.return_hour_combobox.get()
        return_minute = self.return_minute_combobox.get()
        return_ampm = self.return_ampm_combobox.get()
        
        return_time = f"{return_hour}:{return_minute} {return_ampm}" if return_hour and return_minute and return_ampm else None
        
        if cycle_number and return_time:
            # Find the rental entry
            conn = get_db_connection()
            c = conn.cursor()
            c.execute("SELECT id FROM rentals WHERE user_id = ? AND cycle_number = ? AND return_time IS NULL", (self.user_id, cycle_number))
            rental = c.fetchone()
            if rental:
                update_return_time(rental[0], return_time)
                messagebox.showinfo("Success", "Return time updated successfully")
            else:
                messagebox.showerror("Error", "No active rental found for this cycle number")
            conn.close()
        else:
            messagebox.showerror("Error", "Please fill all fields")
    
    def show_rental_history(self):
        # Get rental history for the current user
        rental_history = get_rental_history(self.user_id)
        
        # Create a new window to display rental history
        history_window = tk.Toplevel(self.root)
        history_window.title("Rental History")
        
        # Create a text widget to display history
        history_text = tk.Text(history_window, height=10, width=40)
        history_text.grid(row=0, column=0, padx=10, pady=10)
        
        # Insert rental history data into the text widget
        if rental_history:
            history_text.insert(tk.END, "Cycle Number\tRental Time\tReturn Time\n")
            for rental in rental_history:
                cycle_number, rental_time, return_time = rental
                history_text.insert(tk.END, f"{cycle_number}\t{rental_time}\t{return_time}\n")
        else:
            history_text.insert(tk.END, "No rental history found.")
        
        # Close button to close the history window
        close_button = tk.Button(history_window, text="Close", command=history_window.destroy)
        close_button.grid(row=1, column=0, pady=10)
    
    def login(self):
        username = self.login_username_entry.get()
        password = self.login_password_entry.get()
        
        user = check_user_credentials(username, password)
        if user:
            self.user_id = user[0]
            self.username = username
            self.user_id_label.config(text=str(self.user_id))
            self.username_label.config(text=self.username)
            
            # Log login time
            log_login_time(self.user_id)
            
            self.show_frame(self.rental_frame)
        else:
            messagebox.showerror("Error", "Invalid username or password")
    
    def signup(self):
        username = self.signup_username_entry.get()
        password = self.signup_password_entry.get()
        
        if create_user(username, password):
            messagebox.showinfo("Success", "User created successfully. Please login.")
            self.show_frame(self.login_frame)
        else:
            messagebox.showerror("Error", "Username already exists")
    
    def logout(self):
        self.user_id = None
        self.username = None
        self.user_id_label.config(text="")
        self.username_label.config(text="")
        self.show_frame(self.login_frame)

def setup_database():
    conn = sqlite3.connect('cycle_rental.db')
    c = conn.cursor()
    
    # Create users table
    c.execute('''CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT UNIQUE NOT NULL,
                    password TEXT NOT NULL)''')
    
    # Create rentals table
    c.execute('''CREATE TABLE IF NOT EXISTS rentals (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id INTEGER NOT NULL,
                    cycle_number TEXT NOT NULL,
                    rental_time TEXT NOT NULL,
                    return_time TEXT,
                    FOREIGN KEY (user_id) REFERENCES users (id))''')
    
    # Create login history table
    c.execute('''CREATE TABLE IF NOT EXISTS login_history (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id INTEGER NOT NULL,
                    login_time TEXT NOT NULL,
                    FOREIGN KEY (user_id) REFERENCES users (id))''')
    
    conn.commit()
    conn.close()

def get_db_connection():
    conn = sqlite3.connect('cycle_rental.db')
    return conn

def create_user(username, password):
    conn = get_db_connection()
    c = conn.cursor()
    try:
        c.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False
    finally:
        conn.close()

def check_user_credentials(username, password):
    conn = get_db_connection()
    c = conn.cursor()
    c.execute("SELECT id FROM users WHERE username = ? AND password = ?", (username, password))
    user = c.fetchone()
    conn.close()
    return user

def log_rental(user_id, username, cycle_number, rental_time, return_time=None):
    conn = get_db_connection()
    c = conn.cursor()
    c.execute("INSERT INTO rentals (user_id, cycle_number, rental_time, return_time) VALUES (?, ?, ?, ?)",
              (user_id, cycle_number, rental_time, return_time))
    conn.commit()
    conn.close()

def update_return_time(rental_id, return_time):
    conn = get_db_connection()
    c = conn.cursor()
    c.execute("UPDATE rentals SET return_time = ? WHERE id = ?", (return_time, rental_id))
    conn.commit()
    conn.close()

def get_rental_history(user_id):
    conn = get_db_connection()
    c = conn.cursor()
    c.execute("SELECT cycle_number, rental_time, return_time FROM rentals WHERE user_id = ?", (user_id,))
    rental_history = c.fetchall()
    conn.close()
    return rental_history

def log_login_time(user_id):
    conn = get_db_connection()
    c = conn.cursor()
    login_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    c.execute("INSERT INTO login_history (user_id, login_time) VALUES (?, ?)", (user_id, login_time))
    conn.commit()
    conn.close()

if __name__ == "__main__":
    setup_database()
    root = tk.Tk()
    app = CycleRentalApp(root)
    root.geometry("400x400")
    root.mainloop()
