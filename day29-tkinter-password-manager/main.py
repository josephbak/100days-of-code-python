from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from random import randint, choice, shuffle
import pyperclip
from tkmacosx import Button as button
import json



# Constant
BLACK = "#0e0d03"
WHITE = "#fefefd"
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    # nr_letters = random.randint(8, 10)
    # nr_symbols = random.randint(2, 4)
    # nr_numbers = random.randint(2, 4)

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    # for char in range(nr_letters):
    #     password_list.append(random.choice(letters))
    #
    # for char in range(nr_symbols):
    #     password_list += random.choice(symbols)
    #
    # for char in range(nr_numbers):
    #     password_list += random.choice(numbers)

    password_list = password_letters + password_symbols + password_numbers

    shuffle(password_list)

    password = "".join(password_list)
    # for char in password_list:
    #     password += char

    # print(f"Your password is: {password}")

    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():

    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty.")
    else:
        try:
            with open("data.json", "r") as data_file:
                #Write to Json file
                #json.dump(new_data, data_file, indent=4)

                # Read from Json file
                # data = json.load(data_file)
                # print(data)

                #Update the data with a new data
                data = json.load(data_file)  #Reading old data
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)   #Updating old data with new data

            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)    #saving updated data
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)
# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():

    website = website_entry.get()
    # email = email_entry.get()

    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} exists.")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

im = Image.open("logo.png")
logo_img = ImageTk.PhotoImage(im.convert("L"))
canvas = Canvas(height=200, width=200)
canvas.config(bg=WHITE)
# logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

#Labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)
passward_label = Label(text="Password:")
passward_label.grid(row=3, column=0)


#Entries
website_entry = Entry(width=22)
website_entry.grid(row=1, column=1)
website_entry.focus()
email_entry = Entry(width=40)
email_entry.grid(row=2, column= 1, columnspan=2)
email_entry.insert(0, "joe@email.com")
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)


#Buttons
search_button = button(text="Search", width=130, command = find_password)
search_button.grid(row= 1, column= 2)
generate_password_button = button(text="Generage Password", command = generate_password)
generate_password_button.grid(row=3, column=2)
add_button = button(text="Add", width=330, command=save)
add_button.grid(row=4, column=1, columnspan=2)


window.mainloop()
