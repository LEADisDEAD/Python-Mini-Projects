# Password gen (terminal)
import tkinter as tk
from tkinter import messagebox
import json
import random
import string



lower_letters = list(string.ascii_lowercase)
upper_letters = list(string.ascii_uppercase)
specials = list(string.punctuation)
digits = list(string.digits)
def PasswordGenerator():

    password = []
    password += random.choices(digits,k=3)
    password += random.choices(lower_letters,k=3)
    password += random.choices(upper_letters,k=3)
    password += random.choices(specials,k=3)

    random.shuffle(password)
    passw = "".join(password)

    password_entry.delete(0, tk.END)  # Clear current entry
    password_entry.insert(0, passw)

    return passw

def save_password():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(username)==0 or len(password)==0:
        messagebox.showwarning(title="Warning",message="Please dont leave the space blank!")
        return

    new_data= {
        website:{
            "username":username,
            "password":password
        }
    }

    try:
        with open("passwords.json","r") as file:
            data = json.load(file)
    except FileNotFoundError:
        data = {}

    data.update(new_data)

    with open("passwords.json","w") as file:
        json.dump(data,file,indent=4)

    messagebox.showinfo(title="Success",message="Password saved successfully")
    website_entry.delete(0,tk.END)
    password_entry.delete(0,tk.END)
    username_entry.delete(0,tk.END)


def search_password():

    website = website_entry.get()

    try:
        with open("passwords.json","r") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showerror(title="Error", message="Data file not found")
        return

    if website in data:
        username = data[website]["username"]
        password = data[website]["password"]

        messagebox.showinfo(title=website, message=f"Username: {username}\n Password: {password}")

    else:
        messagebox.showwarning(title="Not found",message="No data exists for the website")

# ------------UI------------

root = tk.Tk()
root.title("Password Manager")
root.geometry("400x400")

titmid = tk.Label(text="Password Manager",font = ("Roboto",16))
titmid.pack(pady=10)

website_label = tk.Label(text="Website:",font=("Verdana", 13))
website_label.place(x=75,y=70)


website_entry = tk.Entry(font=("Arial", 16))
website_entry.place(x=75,y=100)
website_entry.focus()

username_label = tk.Label(text="Username:",font=("Verdana", 13))
username_label.place(x=75,y=140)

username_entry = tk.Entry(font=("Arial", 16))
username_entry.place(x=75,y=170)


password_label = tk.Label(text="Password:",font=("Verdana", 13))
password_label.place(x=75,y=210)

password_entry = tk.Entry(font=("Arial", 16))
password_entry.place(x=75,y=240)

generate_button = tk.Button(text="Generate Password", command=PasswordGenerator,height=2,width=15)
generate_button.place(x=75,y=280)

search_button = tk.Button(text="Search", command=search_password,height=2,width=15)
search_button.place(x=208,y=280)

add_button = tk.Button(text="Save", width=34, height = 2,command=save_password)
add_button.place(x=75,y=330)

root.mainloop()

