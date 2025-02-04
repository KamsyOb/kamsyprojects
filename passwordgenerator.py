import tkinter as tk
from tkinter import messagebox
import random
import string

# Function to generate the password

def generate_password():
    try:
        # Get the number of characters
        characterno = int(char_length_entry.get())

        # Build the character set based on user choices
        characters = string.ascii_lowercase  # Always include lowercase letters
        if include_upper_var.get():
            characters += string.ascii_uppercase
        if include_digits_var.get():
            characters += string.digits
        if include_special_var.get():
            characters += string.punctuation

        # Generate a random password
        if characters:
            password = ''.join(random.choice(characters) for _ in range(characterno))
            password_label.config(text=password)
        else:
            messagebox.showerror("Error", "Please select at least one character type!")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number for the password length.")

# Function to copy password to clipboard
def copy_to_clipboard():
    root.clipboard_clear()
    root.clipboard_append(password_label.cget("text"))
    root.update()
    messagebox.showinfo("Success", "Password copied to clipboard!")

# Set up the main application window
root = tk.Tk()
root.geometry("400x400")
root.title("Password Generator")
root.resizable(False, False)

# Title label
tk.Label(root, text="Password Generator", font=("Helvetica", 16)).pack(pady=10)

# Password length input
tk.Label(root, text="Password Length:", font=("Helvetica", 12)).pack()
char_length_entry = tk.Entry(root, font=("Helvetica", 12), justify="center")
char_length_entry.pack(pady=5)

# Options for password requirements
include_upper_var = tk.BooleanVar()
include_digits_var = tk.BooleanVar()
include_special_var = tk.BooleanVar()

tk.Checkbutton(root, text="Include Uppercase Letters", variable=include_upper_var, font=("Helvetica", 12)).pack(anchor="w", padx=50)
tk.Checkbutton(root, text="Include Numbers", variable=include_digits_var, font=("Helvetica", 12)).pack(anchor="w", padx=50)
tk.Checkbutton(root, text="Include Special Characters", variable=include_special_var, font=("Helvetica", 12)).pack(anchor="w", padx=50)

# Button to generate the password
tk.Button(root, text="Generate Password", command=generate_password, font=("Helvetica", 12)).pack(pady=10)

# Label to display the generated password
password_label = tk.Label(root, text="", font=("Helvetica", 14), fg="blue")
password_label.pack(pady=10)

# Button to copy the password to clipboard
tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard, font=("Helvetica", 12)).pack(pady=10)

# Run the application
root.mainloop()
