from tkinter import *
import os
import json
from PIL import ImageTk,Image
from tkinter import messagebox
from tkinter import filedialog
import os

# Main Window Spec
main = Tk()
main.title('Item Calculators')
main.iconbitmap('Testing_Grounds_PY/Item Calculator/Images/icon/cha0scharly.ico')
main.geometry("542x238")
main.configure(bg="#11161d")

# Menu Buttons Frame
menu_frame = Frame(main, bg="#11161d")
menu_frame.grid(row=0, column=0, columnspan=2, sticky=W)

# Menu Items
# Need to switch File and Edit to Option Menus
# Go back to Lessons and run the Option Menu Lesson

# File
file_menu = Button(menu_frame, text="File", width=7, bg="#11161d", fg="#b5dfff")
file_menu.grid(row=0, column=0, pady=5)

# Edit
edit_menu = Button(menu_frame, text="Edit", width=7, bg="#11161d", fg="#b5dfff", borderwidth=2)
edit_menu.grid(row=0, column=1, pady=5)

# Exit
quit_button = Button(menu_frame, text="Exit", command=main.destroy, width=7, bg="#11161d", fg="#b5dfff")
quit_button.grid(row=0, column=2, pady=5)

# Run button Frame for different Calculators
run_button_frame = LabelFrame(main, text="Item Calculators",borderwidth=3, relief="groove", bg="#821e1e", fg="#b5dfff", font="bold")
run_button_frame.grid(row=1, column=0, sticky=N)
# Run button Frame for different Calculators
coming_soon = LabelFrame(main, text="Coming Soon",borderwidth=3, relief="groove", bg="#821e1e", fg="#b5dfff", font="bold")
coming_soon.grid(row=2, column=0, sticky=N)

# Note Filler Frame
filler_frame = LabelFrame(main, width=100, height=100, text="Patch Notes", borderwidth=3, relief="groove", bg="#11161d", fg="#b5dfff", font="bold")
filler_frame.grid(row=1, column=1,  rowspan=2, sticky=N)
patch_0_0_1_title = Label(filler_frame, text="Patch 0.0.1", bg="#11161d", fg="#b5dfff").pack()
patch_0_0_1_body1 = Label(filler_frame, text="- Creation of main window and second window interface", bg="#11161d", fg="#b5dfff").pack()
patch_0_0_1_body2 = Label(filler_frame, text="- Satisfactory Calculator added with item and normal calculator with notes", bg="#11161d", fg="#b5dfff").pack()
patch_0_0_1_body3 = Label(filler_frame, text="- Implementation of the item and normal calculator not finished yet.", bg="#11161d", fg="#b5dfff").pack()
patch_0_0_1_body4 = Label(filler_frame, text="- Addition of coming soon", bg="#11161d", fg="#b5dfff").pack()
patch_0_0_1_body5 = Label(filler_frame, text="- Factorio, Dyson Sphere, Starfeild, Infinifactory and ??? added", bg="#11161d", fg="#b5dfff").pack()
patch_0_0_1_body6 = Label(filler_frame, text="- Change to colour scheme in the Main Window", bg="#11161d", fg="#b5dfff").pack()
patch_0_0_1_body7 = Label(filler_frame, text="- Change to colour scheme in the Satisfactory Window", bg="#11161d", fg="#b5dfff").pack()
                         


def open_main_window():
    main.deiconify()

def satisfactory():
    sat_calc = Tk()
    sat_calc.title('Satisfactory Calculator')
    sat_calc.iconbitmap('Testing_Grounds_PY/Item Calculator/Images/icon/satisfactory_img.ico')
    sat_calc.geometry("408x827")
    sat_calc.config(bg="#4c5b5f")

    # Menu Frame
    sat_menu_frame = Frame(sat_calc, bg="#4c5b5f")
    sat_menu_frame.grid(row=0, column=0, columnspan=2, sticky=W)

    # Menu Items: 
    # File and edit - need to be menus and to be populated
    # Save and load - need to add functions to this

    # File
    sat_file_menu = Button(sat_menu_frame, text="File", bg="#4c5b5f", fg="#e49245", width=5)
    sat_file_menu.grid(row=0, column=0, pady=5)

    # Edit
    sat_edit_menu = Button(sat_menu_frame, text="Edit", bg="#4c5b5f", fg="#e49245", width=5)
    sat_edit_menu.grid(row=0, column=1, pady=5)

    # Save funcation
    def sat_save():
        file_path = filedialog.asksaveasfilename(initialdir="Testing_Grounds_PY/Item Calculator/sat_saves", defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if file_path:
            try:
                with open(file_path, 'w') as file:
                    text_content = sat_notes.get("1.0", "end-1c")
                    file.write(text_content)
                sys_notes.config(text=f"File saved: {file_path}")
            except Exception as e:
                sys_notes.config(text=f"Error saving file: {str(e)}")
    # save Button
    sat_save_button = Button(sat_menu_frame, text="Save", command=sat_save, bg="#4c5b5f", fg="#e49245", width=5)
    sat_save_button.grid(row=0, column=2, pady=5)

    # Load
    
    def sat_open():
        sat_calc.filename = filedialog.askopenfilename(initialdir="H:\Code\Testing_Grounds_PY\Tk_images", defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])

    sat_load_button = Button(sat_menu_frame, text="load", command=sat_open, bg="#4c5b5f", fg="#e49245", width=5)
    sat_load_button.grid(row=0, column=3, pady=5)

    # Exit

    sat_exit_menu = Button(sat_menu_frame, text="Exit", command=lambda:[open_main_window(),sat_calc.destroy()], bg="#4c5b5f", fg="#e49245", width=5)
    sat_exit_menu.grid(row=0, column=4, pady=5)

    # Quit
    
    sat_quit_menu = Button(sat_menu_frame, text="Quit", command=lambda:[main.quit(), sat_calc.quit()], bg="#4c5b5f", fg="#e49245", width=5)
    sat_quit_menu.grid(row=0, column=5, pady=5)

    # System Notes
    sys_notes = LabelFrame(sat_calc, text="", padx=20, pady=1)
    sys_notes.grid(row=1, column=0, columnspan=2)

    # Item Calc frame
    sat_item_frame = LabelFrame(sat_calc, text="Item Calculator", bg="#4c5b5f", fg="#e49245")
    sat_item_frame.grid(row=2, column=0)

    #Item Calculator
    
    # Item Calculator Function
    def calculate_ingredients():
        try:
            item_name = item_var.get()
            required_amount = float(input_var.get())

            #Build the full path to the Item Data folder
            item_data_folder = os.path.join(os.path.dirname(__file__), "item_data")

            with open(os.path.join(item_data_folder, f'{item_name}.json')) as file:
                item_data = json.load(file)

            result = item_data[item_name]["Result"]
            ingredients = item_data[item_name]["Ingredients"]

            required_ingredients = {ingredient: required_amount / result * amount for ingredient, amount in ingredients.items()}

            formatted_output = "\n".join([f"{ingredient}: {amount}" for ingredient, amount in required_ingredients.items()])
            ingredient_output.config(text=formatted_output)

        except (ValueError, FileNotFoundError, KeyError):
            result_label.config(text="Invalid item or input.")

    # Load the item names from the item_data directory
    item_data_folder = os.path.join(os.path.dirname(__file__), "item_data")
    item_files = [file.split(".")[0] for file in os.listdir(item_data_folder)]
    item_var = StringVar()
    item_var.set(item_files[0])

    # Item Dropdown
    item_label = Label(sat_item_frame, text="Select Item:", fg="#e49245", bg="#4c5b5f", padx=10, pady=1)
    item_dropdown = OptionMenu(sat_item_frame, item_var, *item_files)
    item_label.pack()
    item_dropdown.pack()
    item_dropdown.config(fg="#e49245", bg="#4c5b5f")
    item_dropdown["menu"].config(fg="#e49245", bg="#4c5b5f")

    # Input for the Required amount/m
    input_label = Label(sat_item_frame, text="Enter Required Amount:", fg="#e49245", bg="#4c5b5f", padx=10, pady=1)
    input_var = Entry(sat_item_frame, fg="#e49245", bg="#4c5b5f",)
    input_label.pack()
    input_var.pack()

    # Calculate Results Button
    calculate_button = Button(sat_item_frame, padx=10, pady=1, text="🔻Calculate Ingredients /m🔻", command=calculate_ingredients, fg="#e49245", bg="#4c5b5f")
    calculate_button.pack()

    # Labels for the results
    result_label = Label(sat_item_frame, text="", fg="#e49245", bg="#4c5b5f", padx=10, pady=1)
    result_label.pack()
    ingredient_output = Label(sat_item_frame, text="", fg="#e49245", bg="#4c5b5f", padx=10, pady=1)
    ingredient_output.pack()

    # Normal Calculator Frame
    sat_calc_frame = LabelFrame(sat_calc, text="Calculator", bg="#4c5b5f", fg="#e49245")
    sat_calc_frame.grid(row=1, column=1)
    
    '''
    BREAK
    '''

    # Standard Calculator
    e = Entry(sat_calc_frame, width=30, borderwidth=5, fg="#e49245", bg="#4c5b5f")
    e.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

    # Number Functions
    def button_click(number):
        current = e.get()
        e.delete(0, END)
        e.insert(0, str(current) + str(number))

    # Clear Entry
    def button_ce():
        e.delete(0, END)

    # Addition Function
    def button_plus():
        first_number = e.get()
        global f_num 
        global math 
        math = "plus"
        f_num = int(first_number)
        e.delete(0, END)

    # Subtraction Function
    def button_minus():
        first_number = e.get()
        global f_num 
        global math 
        math = "minus"
        f_num = int(first_number)
        e.delete(0, END)

    # Muntiplcation Function
    def button_times():
        first_number = e.get()
        global f_num 
        global math 
        math = "times"
        f_num = int(first_number)
        e.delete(0, END)

    #Divition Function
    def button_divide():
        first_number = e.get()
        global f_num 
        global math 
        math = "divide"
        f_num = int(first_number)
        e.delete(0, END)

    # Output Result
    def button_equal():
        second_number = e.get()
        e.delete(0, END)

        if math == "plus":
            e.insert(0, f_num + int(second_number))

        if math == "minus":
            e.insert(0, f_num - int(second_number))

        if math == "times":
            e.insert(0, f_num * int(second_number))

        if math == "divide":
            e.insert(0, f_num / int(second_number))



    # Define layout
    button_1 = Button(sat_calc_frame, text="1", padx=20, pady=10, fg="#e49245", bg="#4c5b5f", command=lambda: button_click(1))
    button_2 = Button(sat_calc_frame, text="2", padx=20, pady=10, fg="#e49245", bg="#4c5b5f", command=lambda: button_click(2))
    button_3 = Button(sat_calc_frame, text="3", padx=20, pady=10, fg="#e49245", bg="#4c5b5f", command=lambda: button_click(3))
    button_4 = Button(sat_calc_frame, text="4", padx=20, pady=10, fg="#e49245", bg="#4c5b5f", command=lambda: button_click(4))
    button_5 = Button(sat_calc_frame, text="5", padx=20, pady=10, fg="#e49245", bg="#4c5b5f", command=lambda: button_click(5))
    button_6 = Button(sat_calc_frame, text="6", padx=20, pady=10, fg="#e49245", bg="#4c5b5f", command=lambda: button_click(6))
    button_7 = Button(sat_calc_frame, text="7", padx=20, pady=10, fg="#e49245", bg="#4c5b5f", command=lambda: button_click(7))
    button_8 = Button(sat_calc_frame, text="8", padx=20, pady=10, fg="#e49245", bg="#4c5b5f", command=lambda: button_click(8))
    button_9 = Button(sat_calc_frame, text="9", padx=20, pady=10, fg="#e49245", bg="#4c5b5f", command=lambda: button_click(9))
    button_0 = Button(sat_calc_frame, text="0", padx=20, pady=10, fg="#e49245", bg="#4c5b5f", command=lambda: button_click(0))
    button_plus = Button(sat_calc_frame, text="+", padx=17, pady=10, fg="#e49245", bg="#4c5b5f", command= button_plus)
    button_equal = Button(sat_calc_frame, text="=", padx=100, pady=10, fg="#e49245", bg="#4c5b5f", command=button_equal)
    button_clear = Button(sat_calc_frame, text="Clear", padx=37, pady=10, fg="#e49245", bg="#4c5b5f", command=button_ce)

    button_minus = Button(sat_calc_frame, text="-", padx=19, pady=10, fg="#e49245", bg="#4c5b5f", command= button_minus)
    button_times = Button(sat_calc_frame, text="*", padx=19, pady=10, fg="#e49245", bg="#4c5b5f", command= button_times)
    button_divide = Button(sat_calc_frame, text="/", padx=19, pady=10, fg="#e49245", bg="#4c5b5f", command= button_divide)

    # Button Layout

    button_1.grid(row=3, column=0)
    button_2.grid(row=3, column=1)
    button_3.grid(row=3, column=2)

    button_4.grid(row=2, column=0)
    button_5.grid(row=2, column=1)
    button_6.grid(row=2, column=2)

    button_7.grid(row=1, column=0)
    button_8.grid(row=1, column=1)
    button_9.grid(row=1, column=2)

    button_0.grid(row=4, column=0,)

    button_clear.grid(row=4, column=1, columnspan=2)
    button_equal.grid(row=5, column=0, columnspan=4)

    button_plus.grid(row=1, column=3)
    button_minus.grid(row=2, column=3)
    button_times.grid(row=3, column=3)
    button_divide.grid(row=4, column=3)


    # Notes Frame
    sat_notes_frame = LabelFrame(sat_calc, text="Notes", bg="#4c5b5f", fg="#e49245")
    sat_notes_frame.grid(row=2, column=0, columnspan=2)

    sat_notes = Text(sat_notes_frame, bg="#4c5b5f", fg="#e49245", width=50, height=30)
    sat_notes.grid(row=0, column=0, columnspan=2)



#Buttons Implemented
sat_open = Button(run_button_frame, text="Satisfactory Calculator", width=17, command=lambda: [satisfactory(), main.withdraw()], bg="#11161d", fg="#b5dfff")
sat_open.grid(row=0, column=0)

# Buttons coming soon
factorio_open = Button(coming_soon, text="Factorio", state=DISABLED, width=17, bg="#11161d", fg="#b5dfff")
factorio_open.grid(row=0, column=0)
dysonSphere_open = Button(coming_soon, text="Dyson Sphere", state=DISABLED, width=17, bg="#11161d", fg="#b5dfff")
dysonSphere_open.grid(row=1, column=0)
starField_open = Button(coming_soon, text="Star Field", state=DISABLED, padx=36, bg="#11161d", fg="#b5dfff")
starField_open.grid(row=2, column=0)
infinifactory_open = Button(coming_soon, text="Infinifactory", state=DISABLED, width=17, bg="#11161d", fg="#b5dfff")
infinifactory_open.grid(row=3, column=0)
question_open = Button(coming_soon, text="???", state=DISABLED, width=17, bg="#11161d", fg="#b5dfff")
question_open.grid(row=4, column=0)

# clickable Images frame for ads? Maybe?
image_frame = Frame(main)
image_frame.grid(row=3, column=0, columnspan=2)

main.mainloop()