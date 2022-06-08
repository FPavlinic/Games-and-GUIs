# used libraries
from tkinter import *


# font used in GUI of miles to km converter
FONT = ("Arial", 11)


def miles_to_km():
    """Converts miles to kms"""
    miles = float(miles_input.get())
    km = round(miles * 1.609344, 2)
    km_result_label.config(text=km)


# window of miles to km converter
window = Tk()
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)

# input for value of miles
miles_input = Entry(width=7, justify="center", font=FONT)
miles_input.focus()
miles_input.grid(column=1, row=0)

# miles label
miles_label = Label(text="Miles", font=FONT)
miles_label.grid(column=2, row=0)
miles_label.config(padx=10, pady=5)

# equal label between miles and kms
equal_to_label = Label(text="is equal to", font=FONT)
equal_to_label.grid(column=0, row=1)
equal_to_label.config(padx=10, pady=5)

# output for value of kms
km_result_label = Label(text=0, justify="center", font=FONT)
km_result_label.grid(column=1, row=1)

# kms label
km_label = Label(text="Km", font=FONT)
km_label.grid(column=2, row=1)
km_label.config(padx=10, pady=5)

# button to call function miles_to_km
calc_button = Button(text="Calculate", command=miles_to_km, font=FONT)
calc_button.grid(column=1, row=2)
calc_button.config(padx=10, pady=5)

# keep the window open
window.mainloop()
