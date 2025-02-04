
import random
import tkinter as tk

quotes = [
    "Believe you can and you're halfway there. – Theodore Roosevelt",
    "The only way to do great work is to love what you do. – Steve Jobs",
    "Act as if what you do makes a difference. It does. – William James",
    "Success is not how high you have climbed, but how you make a positive difference to the world. – Roy T. Bennett",
    "Your limitation—it's only your imagination.",
    "Push yourself, because no one else is going to do it for you."
]

counter = 0

def show_quote():
    global counter
    random_quote = random.choice(quotes)
    quote_lable.config(text=random_quote)
    counter += 1
    counter_label.config(text=f"Quotes viewed: {counter}")


root = tk.Tk()
root.title("Daily Motivation")
root.geometry("300x150")
root.resizable(False, False)

quote_lable = tk.Label(root, text="", wraplength = 380, font=("Helvetica", 12), justify="center")
quote_lable.pack(pady=20)

counter_label = tk.Label(root, text="Quotes viewed: 0", font=("Helvetica", 10))
counter_label.pack(pady=5)

new_quote_button = tk.Button(root, text="New Quote", command=show_quote, font=("Helvetica", 10))
new_quote_button.pack(pady=10)

show_quote()
root.mainloop()
