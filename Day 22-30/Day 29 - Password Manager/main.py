import tkinter as tk
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

#Password Generator Project from Course Day 5

def generate_password():

    password_input.delete(0, "end")

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = randint(8, 10)
    nr_symbols = randint(2, 4)
    nr_numbers = randint(2, 4)

    password_letters = [choice(letters) for _ in range(nr_letters)]
    password_symbols = [choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = ''.join(password_list)
    pyperclip.copy(password)
    password_input.insert(0, f"{password}")
    password = ''


    # print(f"Your password is: {password}")
# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website = website_input.get()
    username = username_input.get()
    password = password_input.get()

    if website == "" or password == "":
        messagebox.showwarning(title="Oops!", message="Make sure you didn't leave any fields empty!")


    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail/Username: {username},"
                                                  f" Password: {password}")
        if is_ok:
            with open("password_list.txt", "a") as data:
                data.write(f"{website} | {username} | {password} \n")

            website_input.delete(0, "end")
            username_input.delete(0, "end")
            password_input.delete(0, "end")



# ---------------------------- UI SETUP ------------------------------- #

window = tk.Tk()
window.title("MyPass")
window.config(padx=50, pady=50, bg="white")

#Canvas and BG image
canvas = tk.Canvas(width=200, height=200, bg="white", highlightthickness=0)
logo = tk.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(row=1, column=2)

#Website Row
website_label = tk.Label(text="Website: ")
website_label.grid(row=2, column=1)
website = ""
website_input = tk.Entry(width=35, textvariable=website)
website_input.grid(row=2, column=2, columnspan=2)
website_input.focus() #puts cursor in the website field

#Username Row
username_label = tk.Label(text="Email/Username: ")
username_label.grid(row=3, column=1)
username = ""
username_input = tk.Entry(width=35, textvariable=username)
username_input.grid(row=3, column=2, columnspan=2)
username_input.insert(0, "myemail@email.com") #populates username field with this.

#Password Row
password_label = tk.Label(text="Password: ")
password_label.grid(row=4, column=1)
password = ""
password_input = tk.Entry(width=21, textvariable=password)
password_input.grid(row=4, column=2)

password_gen_button = tk.Button(text="Generate Password", command=generate_password)
password_gen_button.grid(row=4, column=3)

#Add Button
add_password = tk.Button(text="Add", width=36, command=save)
add_password.grid(row=5, column=2, columnspan=2)






window.mainloop()