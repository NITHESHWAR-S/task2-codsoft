import tkinter as tk
from tkinter import ttk
import random
import string

def generate_password():
    try:
        length = int(length_entry.get())
        if length <= 0:
            password_label.config(text="Please enter a positive integer")
        else:
            lowercase_letters = string.ascii_lowercase
            uppercase_letters = string.ascii_uppercase
            digits = string.digits
            special_characters = string.punctuation

            all_characters = lowercase_letters + uppercase_letters + digits + special_characters

            password = ''.join(random.choices(all_characters, k=length))
            password_entry.delete(0, tk.END)
            password_entry.insert(tk.END, password)
            password_label.config(text="Generated Password:")
    except ValueError:
        password_label.config(text="Please enter a valid integer for the password length")

def accept_password():
    username = username_entry.get()
    password = password_entry.get()
    if username and password:
        # Add your code here to save the username and password
        print("Username:", username)
        print("Password:", password)
        username_entry.delete(0, tk.END)
        length_entry.delete(0, tk.END)
        password_entry.delete(0, tk.END)
        password_label.config(text="Password accepted")
    else:
        password_label.config(text="Please enter username and password")

def reset_password():
    username_entry.delete(0, tk.END)
    length_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)
    password_label.config(text="")

root = tk.Tk()
root.title("Password Manager")

style = ttk.Style()
style.configure('TLabel', font=('Arial', 12), foreground='black')
style.configure('TButton', font=('Arial', 12), foreground='black', background='#388E3C')
style.configure('TEntry', font=('Arial', 12))


username_label = ttk.Label(root, text="Enter username:")
username_label.grid(row=0, column=0, padx=10, pady=10)

username_entry = ttk.Entry(root)
username_entry.grid(row=0, column=1, padx=10, pady=10)

length_label = ttk.Label(root, text="Enter password length:")
length_label.grid(row=1, column=0, padx=10, pady=10)

length_entry = ttk.Entry(root)
length_entry.grid(row=1, column=1, padx=10, pady=10)

password_frame = ttk.Frame(root)
password_frame.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

password_label = ttk.Label(password_frame, text="Generated Password:", style='TLabel')
password_label.grid(row=0, column=0, padx=(0, 5))

password_entry = ttk.Entry(password_frame)
password_entry.grid(row=0, column=1)


generate_button = ttk.Button(root, text="Generate Password", command=generate_password, style='TButton')
generate_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

accept_button = ttk.Button(root, text="Accept Password", command=accept_password, style='TButton')
accept_button.grid(row=4, column=0, padx=10, pady=10)

reset_button = ttk.Button(root, text="Reset Password", command=reset_password, style='TButton')
reset_button.grid(row=4, column=1, padx=10, pady=10)

root.mainloop()
