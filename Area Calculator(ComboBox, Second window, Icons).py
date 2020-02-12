#Area Calculator (GUI)

from tkinter import*
from tkinter import ttk

##GUI
root = Tk()
root.title("Computer Project : Area calculator")
root.geometry("563x680")
root.iconbitmap('C:/calculator icon.ico')

##Second Window(Members)
new_window = Toplevel()
new_window.title("Members")
new_window.geometry("795x435")
new_window.iconbitmap('C:/member icon.ico')

#Second Frame
second_title_frame = LabelFrame(new_window, padx=5,pady=5, bg = "PaleTurquoise")
second_title_frame.grid(padx=5, pady=5)

members_frame = LabelFrame(new_window, padx=5,pady=5, bg = "SkyBlue")
members_frame.grid(padx=5, pady=5)

second_control_frame = LabelFrame(new_window, padx=5,pady=5, bg = "Lavender")
second_control_frame.grid(padx=5, pady=5)

#Second Fonts
second_title_font = "Arial", 30, "bold", "underline"
members_font = "Arial", 20, "bold"

#Second Title Frame
second_title = Label(second_title_frame, text = "MEMBERS", font = second_title_font, fg = "black", bg = "PaleTurquoise")
second_title.grid(row = 0, column = 0)

#Members Frame
first_member = Label(members_frame, text = "Natthapong Hongpakmanoon M.2/1 Student number 48130", font = members_font, fg = "black", bg = "PaleTurquoise")
first_member.grid(row = 0, column = 0)

second_member = Label(members_frame, text = "Thanawai Lertkiettikun M.2/1 Student number 48131", font = members_font, fg = "black", bg = "PaleTurquoise")
second_member.grid(row = 1, column = 0)

third_member = Label(members_frame, text = "Punyapat Chintrapong M.2/1 Student number 48136", font = members_font, fg = "black", bg = "PaleTurquoise")
third_member.grid(row = 2, column = 0)

fourth_member = Label(members_frame, text = "Bhuwis Sunksiri M.2/1 Student number 48143", font = members_font, fg = "black", bg = "PaleTurquoise")
fourth_member.grid(row = 3, column = 0)

fifth_member = Label(members_frame, text = "Rutchanun Pairungrueng M.2/1 Student number 48145", font = members_font, fg = "black", bg = "PaleTurquoise")
fifth_member.grid(row = 4, column = 0)

sixth_member = Label(members_frame, text = "Nattapon Sripradub M.2/1 Student number 48613", font = members_font, fg = "black", bg = "PaleTurquoise")
sixth_member.grid(row = 5, column = 0)

#Second Control Frame
second_close_button = Button(second_control_frame, text = "CLOSE", font = second_title_font, bg = "OrangeRed", command = new_window.destroy)
second_close_button.grid(row = 0, column = 0, columnspan = 3)

##Definition
#Geometry Calculator
def Triangle():
    num1 = base_entry.get()
    num2 = height_entry.get()
    
    Label(output_frame, text = float(num1)*float(num2)/2, font = title_font, width = 25, \
    bg = "powder blue").grid(row = 0, column = 0)

def Rectangle():
    num1 = width_entry.get()
    num2 = height_entry.get()
    
    Label(output_frame, text = float(num1)*float(num2), font = title_font, width = 25, \
    bg = "powder blue").grid(row = 0, column = 0)

def Parallelogram():
    num1 = base_entry.get()
    num2 = height_entry.get()
    
    Label(output_frame, text = float(num1)*float(num2), font = title_font, width = 25, \
    bg = "powder blue").grid(row = 0, column = 0)

def Trapezium():
    num1 = width_entry.get()
    num2 = base_entry.get()
    num3 = height_entry.get()
    
    Label(output_frame, text = (float(num1)+float(num2))*float(num3)/2, font = title_font, width = 25, \
    bg = "powder blue").grid(row = 0, column = 0)

def Circle():
    num1 = radius_entry.get()
    
    Label(output_frame, text = (float(num1)*float(num1))*3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679, font = title_font, width = 25, \
    bg = "powder blue").grid(row = 0, column = 0)

#Control
def Result():
    if geometry_values.get() == "Triangle":
        Triangle()

    elif geometry_values.get() == "Rectangle":
        Rectangle()

    elif geometry_values.get() == "Parallelogram":
        Parallelogram()

    elif geometry_values.get() == "Trapezium":
        Trapezium()

    elif geometry_values.get() == "Circle":
        Circle()

    else:
        Label(output_frame, text = "ERROR", font = title_font, width = 25, \
    bg = "powder blue").grid(row = 0, column = 0)

def Clear():
    width_entry.delete(0,END)
    height_entry.delete(0,END)
    base_entry.delete(0,END)
    radius_entry.delete(0,END)

def Close():
    root.destroy()
    print("Thank you.")

##Fonts
title_font = "Arial", 25, "bold", "underline"
general_font = "Arial", 15, "bold"

##Frames
title_frame = LabelFrame(root, padx=5,pady=5, bg = "PaleTurquoise")
title_frame.grid(padx=5, pady=5)

setting_frame = LabelFrame(root, padx=5,pady=5, bg = "SkyBlue")
setting_frame.grid(padx=5, pady=5)

output_frame = LabelFrame(root, padx=5,pady=5, bg = "Turquoise")
output_frame.grid(padx=5, pady=5)

control_frame = LabelFrame(root, padx=5,pady=5, bg = "Lavender")
control_frame.grid(padx=5, pady=5)
 
info_frame = LabelFrame(root, padx=5,pady=5, bg = "RoyalBlue")
info_frame.grid(padx=5, pady=5)

##Title Frame
title = Label(title_frame, text = "Area Calculator", font = title_font, fg = "black", bg = "PaleTurquoise")
title.grid(row = 0, column = 0)

##Setting Frame
geometry = Label(setting_frame, text = "Geometry :", font = general_font,bg = "SkyBlue")
geometry.grid(row = 0, column = 0)

##Combo box
geometry_values = ttk.Combobox(setting_frame, width = 15, height = 15, values = ["Triangle", "Rectangle", "Parallelogram", "Trapezium", "Circle"])
geometry_values.grid(row = 0, column = 1)
geometry_values.set("Select Geometry")

#Input
width = Label(setting_frame,text = "Width(side1): ", font = general_font, bg = "SkyBlue")
width.grid(row = 1, column = 0)
width_entry = Entry(setting_frame, font = general_font)
width_entry.grid(row = 1, column = 1, columnspan = 2)

height = Label(setting_frame,text = "Height: ", font = general_font, bg = "SkyBlue")
height.grid(row = 2, column = 0)
height_entry = Entry(setting_frame, font = general_font)
height_entry.grid(row = 2, column = 1, columnspan = 2)

base = Label(setting_frame,text = "Base(side2): ", font = general_font, bg = "SkyBlue")
base.grid(row = 3, column = 0)
base_entry = Entry(setting_frame, font = general_font)
base_entry.grid(row = 3, column = 1, columnspan = 2)

radius = Label(setting_frame,text = "Radius: ", font = general_font, bg = "SkyBlue")
radius.grid(row = 4, column = 0)
radius_entry = Entry(setting_frame, font = general_font)
radius_entry.grid(row = 4, column = 1, columnspan = 2)

##Output Frame
output_area = Label(output_frame, text = "RESULT HERE", font = title_font, width = 25, bg = "Lavender")
output_area.grid(row = 0, column = 0)

##Control Frame
print_button = Button(control_frame, text = "RESULT", font = title_font, bg = "Orange", command = Result)
print_button.grid(row = 0, column = 0)

clear_button = Button(control_frame, text = "CLEAR", font = title_font, bg = "DarkOrange", command = Clear)
clear_button.grid(row = 0, column = 1)

close_button = Button(control_frame, text = "CLOSE", font = title_font, bg = "OrangeRed", command = Close)
close_button.grid(row = 0, column = 2)

##Info Frame
Label(info_frame, fg="white", bg = "RoyalBlue", text='''Thank you for using this program.

This calculator is used for calculating an area.

In order for it to calculate, these're the steps you need to follow.

1.Choose one of the choices which is placed next to the "Geometry" word.

2.Write the numbers inside the "writing-brackets" which different geometries need different formulas.
    1)Triangle = Height, Base
    2)Rectangle = Width(side 1), Height
    3)Parallelogram = Height, Base
    4)Trapezium = Width(side 1), Height, Base
    5)Circle = Radius

3.Click the "Result Button to get the result of the area of a certain geometry.''').grid()

root.mainloop()
