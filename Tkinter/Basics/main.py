"""
#import tkinter module
from tkinter import *

def on_click():
    try:
        val_1 = int(Entry_1.get())
        val_2 = int(Entry_2.get())
        result = val_1+val_2
        print(result)
        Entry_3.delete(0, END)  # Clear any previous content
        Entry_3.insert(0, result)  # Insert the result into Entry_3
    except ValueError:
        Entry_3.config(fg="red")  # Set text color to red if there's an error
        Entry_3.delete(0, END)
        Entry_3.insert(0, "Invalid input")

def clear_1():
       Entry_1.delete(0, END)  # Clear any previous content
       Entry_2.delete(0, END)  # Clear any previous content
       Entry_3.delete(0, END)  # Clear any previous content

root = Tk()
root.title("Calculator")
root.iconbitmap('D:\Python\Tkinter\Basics\Images\Timer.ico')
#root.geometry('400x400+700+300')
root.resizable(0,0)
root.config(bg = '#123456')

# Configure the size of rows and columns
root.rowconfigure(0, minsize=50)  # Set the minimum height of row 0 to 50 pixels
root.rowconfigure(1, minsize=50)  # Set the minimum height of row 1 to 50 pixels
root.rowconfigure(2, minsize=50)  # Set the minimum height of row 2 to 50 pixels

root.columnconfigure(0, minsize=100)  # Set the minimum width of column 0 to 100 pixels
root.columnconfigure(1, minsize=200)  # Set the minimum width of column 1 to 200 pixels


#label_1 = Label(root, text = "STM32 ARR Calculator",font=('Arial', 15), bg ='#E6F2FF')
label_2 = Label(root, text = "Enter the 1st digit:",font=('Arial', 10), bg ='#E6F2FF')
label_2.grid(row = 0, column = 0)

label_3 = Label(root, text = "Enter the 2nd digit:",font=('Arial', 10), bg ='#E6F2FF')
label_3.grid(row = 1, column = 0)

label_4 = Label(root, text = "Result:",font=('Arial', 10), bg ='#E6F2FF')
label_4.grid(row = 2, column = 0)

Entry_1 = Entry(root, width=50, borderwidth=1)
Entry_1.grid(row = 0, column=1)

Entry_2 = Entry(root, width=50, borderwidth=5)
Entry_2.grid(row = 1, column=1)

Entry_3 = Entry(root, width=50, borderwidth=5)
Entry_3.grid(row = 2, column=1)
Entry_3.bind("<Key>", lambda e: "break")

button_1 = Button(root,text = "Result",command=on_click)
button_1.grid(row =3,column=1)

button_2 = Button(root,text = "Clear",command= clear_1)
button_2.grid(row =3,column=2)

root.mainloop()
"""

from tkinter import *

def calculate_arr():
    try:
        clock_freq = float(entry_clock_freq.get()) * unit_multiplier[variable_clock_unit.get()]
        desired_freq = float(entry_desired_freq.get()) * unit_multiplier[variable_desired_unit.get()]

        arr_value = int((clock_freq / desired_freq) - 1)

        entry_arr.delete(0, END)
        entry_arr.insert(0, str(arr_value))
    except ValueError:
        entry_arr.delete(0, END)
        entry_arr.insert(0, "Invalid input")

root = Tk()
root.title("STM32F407 Timer6 ARR Calculator")
root.geometry("400x250")

# Units and their multipliers
units = ["MHz", "kHz", "Hz"]
unit_multiplier = {"MHz": 1e6, "kHz": 1e3, "Hz": 1}

# Labels
Label(root, text="Clock Frequency:").grid(row=0, column=0, padx=10, pady=5, sticky="e")
Label(root, text="Desired Frequency:").grid(row=1, column=0, padx=10, pady=5, sticky="e")
Label(root, text="ARR Value:").grid(row=2, column=0, padx=10, pady=5, sticky="e")

# Entry widgets
entry_clock_freq = Entry(root, width=20)
entry_clock_freq.grid(row=0, column=1, padx=10, pady=5)
entry_desired_freq = Entry(root, width=20)
entry_desired_freq.grid(row=1, column=1, padx=10, pady=5)
entry_arr = Entry(root, width=20)
entry_arr.grid(row=2, column=1, padx=10, pady=5)

# Dropdown boxes for units
variable_clock_unit = StringVar(root)
variable_clock_unit.set(units[0])
clock_unit_dropdown = OptionMenu(root, variable_clock_unit, *units)
clock_unit_dropdown.grid(row=0, column=2, padx=5, pady=5, sticky="w")

variable_desired_unit = StringVar(root)
variable_desired_unit.set(units[0])
desired_unit_dropdown = OptionMenu(root, variable_desired_unit, *units)
desired_unit_dropdown.grid(row=1, column=2, padx=5, pady=5, sticky="w")

# Button
Button(root, text="Calculate", command=calculate_arr).grid(row=3, column=1, padx=10, pady=10)

root.mainloop()
