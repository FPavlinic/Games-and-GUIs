# used libraries
from tkinter import *
from tkinter import messagebox
from random import choice, shuffle, randint
import pyperclip
import json


def generate_password():
    """Generates a password from the sets of letters, numbers and symbols"""

    # sets of characters
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    # chose randomly how many characters of each set will be in the password
    letters_list = [choice(letters) for _ in range(randint(8, 10))]
    numbers_list = [choice(numbers) for _ in range(randint(2, 4))]
    symbols_list = [choice(symbols) for _ in range(randint(2, 4))]

    # concatenate characters into single list
    password_list = letters_list + numbers_list + symbols_list

    # shuffle to randomize order of characters --> stronger password
    shuffle(password_list)

    # join characters into a single string
    password = "".join(password_list)

    # clear entry in GUI
    password_entry.delete(0, END)
    # insert generated password in an entry
    password_entry.insert(0, password)
    # copy generated password to clipboard
    pyperclip.copy(password)


def save():
    """Saves username and password for a specified website"""

    # get values entered in GUI
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()
    new_data = {website: {"username": username, "password": password}}

    # check if input is incomplete
    if len(website) == 0 or len(username) == 0 or len(password) == 0:
        messagebox.showwarning(title="Oops", message="Please don't leave any fields empty!")
    else:
        try:
            # check if file with passwords already exists
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            # if not create it
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            # add new data to it
            data.update(new_data)
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            # clear entries in GUI
            website_entry.delete(0, END)
            password_entry.delete(0, END)


def find_password():
    """Finds password for specified website in the file"""

    # get name of website
    website = website_entry.get()
    try:
        # check if data for that website exists
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
            username = data[website]['username']
            password = data[website]['password']
    except FileNotFoundError:
        # file doesn't exist
        messagebox.showinfo(title="Error", message="Data File Found")
    except KeyError:
        # there is no data for specified website
        messagebox.showinfo(title="Error", message=f"No details for {website} exists")
    else:
        # data is found and shown in pop-up window
        messagebox.showinfo(title=website, message=f"Username: {username}"
                                                   f"\nPassword: {password}")


# set up GUI window
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# set up design of the window
canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

# labels
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)
username_label = Label(text="Email/Username:")
username_label.grid(column=0, row=2)
password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

# entries
website_entry = Entry(width=21)
website_entry.focus()
website_entry.grid(column=1, row=1, columnspan=1, sticky="EW")
username_entry = Entry(width=35)
username_entry.grid(column=1, row=2, columnspan=2, sticky="EW")
password_entry = Entry(width=21)
password_entry.grid(column=1, row=3, sticky="EW")

# buttons
search_button = Button(text="Search", command=find_password)
search_button.grid(column=2, row=1, sticky="EW")
gen_pass_button = Button(text="Generate Password", command=generate_password)
gen_pass_button.grid(column=2, row=3, sticky="EW")
add_button = Button(text="Add", width=36, command=save)
add_button.grid(column=1, row=4, columnspan=2, sticky="EW")

# keep window open
window.mainloop()
