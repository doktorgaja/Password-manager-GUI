from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_label_input.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():

    website = website_input.get()
    email = username_email_input.get()
    password = password_label_input.get()
    new_data = {
        website:{
            "email":email,
            "password":password,
        }}

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", meessage="Please make sure you haven't left any fields empty.")
    else:
        try:
            # Probaj da procitas datu stranicu
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            # Ako nema sta da procita napravi novu
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            # Ako hocemo da update-ujemo a postoji file onda ovo izvrsavamao
            with open("data.json", "w") as data_file:
                data.update(new_data)
                with open("data.json", "w") as data_file:
                    json.dump(data, data_file, indent=4)
        finally:
            # na kraju ako sve ispunjava onda ako dodamo novu brisu se podaci i mozemo ponovo dodavati
            website_input.delete(0, END)
            password_label_input.delete(0, END)

def find_password():
        website = website_input.get()
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            messagebox.showinfo(title="Error", message="Data file not found.")
        else:
            if website in data:
                email = data[website]["email"]
                password = data[website]["password"]
                messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
            else:
                messagebox.showinfo(message="No details for the website exists")
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(pady=50, padx=50, bg="white")

canvas = Canvas(height=200, width=200,bg="white", highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:", bg="white", font=("Aerial", 10), highlightthickness=0)
website_label.grid(column=0, row=1)
website_label.config(padx=2, pady=2)
website_input = Entry(width=33)
website_input.grid(column=1, row=1)

username_email_label = Label(text="Email/Username:", bg="white", font=("Aerial", 10), highlightthickness=0)
username_email_label.grid(column=0, row=2)
username_email_label.config(padx=2, pady=2)
username_email_input = Entry(width=51)
username_email_input.insert(0, "nemanjagajic39@gmail.com")
username_email_input.grid(column=1, row=2, columnspan=2)

password_label = Label(text="Password:", bg="white", font=("Aerial", 10), highlightthickness=0)
password_label.grid(column=0, row=3)
password_label.config(padx=2, pady=2)
password_label_input = Entry(width=33)
password_label_input.grid(column=1, row=3)

button_generate_password = Button()
button_generate_password.config(text="Generate Password", bg="white", highlightthickness=0, command=generate_password)
button_generate_password.grid(column=2, row=3)

button_add = Button()
button_add.config(padx=1, text="Add", bg="white", width=43, command=save)
button_add.grid(column=1, row=4, columnspan=2)

search_button = Button()
search_button.config(padx=1, text="Search", bg="white", width=14, highlightthickness=0, command=find_password)
search_button.grid(column=2,row=1)
window.mainloop()


# za pisanje fajla - json.dump()
# za citanje fajla - json.load()
# za izmenu fajla - json.update()
