import tkinter as tk
import random
import string

def generate_password():
    length = int(length_entry.get())
    
    if length < 1:
        password_label.config(text="Password length must be at least 1.")
        return

    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    password_label.config(text="Generated Password: " + password)

app = tk.Tk()
app.title("Random Password Generator")

length_label = tk.Label(app, text="Password Length:")
length_label.pack(pady=5)

length_entry = tk.Entry(app)
length_entry.pack(pady=5)

generate_button = tk.Button(app, text="Generate Password", command=generate_password)
generate_button.pack(pady=5)

password_label = tk.Label(app, text="")
password_label.pack(pady=5)

app.mainloop()
