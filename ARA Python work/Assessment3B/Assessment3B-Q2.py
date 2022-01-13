# Assessment 3B Question 2
# Timothy Williams, tsw0050@arastudent.ac.nz

from tkinter import *
from tkinter.messagebox import * # required a seperate import for some reason was working buggy on my machine

def get_demerit_points(driving_speed, speed_limit, light_trailer = False, school_zone = False, holiday_period = False):
    '''
    Function works out the demerit point penalty for a driving speed in a particular speed zone
    '''
    # all speeds in km/h any additons to speed_limit (e.g. speed_limit + 20) are additional speed categories
    TRAILER_LENIENCY = 5
    SCHOOL_ZONE_LENIENCY = 4
    HOLIDAY_LENIENCY = 4
    DEFAULT_LENIANCY_SPEED = speed_limit + 10

    # No mandatory penalty unless driver breaks the rules past leniency criteria
    mandatory_penalty = False

    # test for each speed category and if speed >= 10 over the limit then check leniency rules
    if speed_limit < driving_speed:
        penalty_points = 10

        if driving_speed <= DEFAULT_LENIANCY_SPEED:
            if any([light_trailer, school_zone, holiday_period]):

                #Check if any leniency rules are broken and set mandatory penalty
                if driving_speed > speed_limit + TRAILER_LENIENCY and light_trailer: mandatory_penalty = True
                if driving_speed > speed_limit + SCHOOL_ZONE_LENIENCY and school_zone: mandatory_penalty = True
                if driving_speed > speed_limit + HOLIDAY_LENIENCY and holiday_period: mandatory_penalty = True
        else:
            penalty_points += 10
            mandatory_penalty = True

            #check rest of speed categories 21-30 // 31-35 // 36+ and add demerits for each tier
            if driving_speed > speed_limit + 20:
                penalty_points += 15
            if driving_speed > speed_limit + 30:
                penalty_points += 5
            if driving_speed > speed_limit + 35:
                penalty_points += 10
    else:
        penalty_points = 0
    return (mandatory_penalty, penalty_points)

def exit_program(event):
    '''
    Function lets the user check if they meant to exit before leaving with a yes/no dialogue, then closes everything neatly
    '''
    # ask do you want to exit?
    exit_value = askyesno(title = "Demerit points calculator", message = "Do you want to exit?")
    if exit_value:
        main_window.destroy()
    return None

def reset_fields():
    '''
    Reset text fields and tickboxes to default
    '''
    driving_speed_entry.set("")
    radiobutton_b.select()
    towing_tick.deselect()
    school_tick.deselect()
    holiday_tick.deselect()
    clear_answer()
    return None

def clear_answer():
    '''
    Functions clears answer to calculate points function in answer_box_frame
    '''
    previous_answer = answer_box_frame.pack_slaves()
    for item in previous_answer:
        item.destroy()
    return None

def help_menu_handler(ver = False):
    '''
    Function controls the menu options
    '''

    #show (display instructions) & about menu options
    if ver:
        showinfo(title = "Demerit points calculator", message = f"Version {ver}\nWritten by Timothy Williams")
    else:
        showinfo(title = "Demerit points calculator", message = "Enter the driving speed.\nSelect the speed limit.\nSelect trailer/school/holiday situation.\nClick calculate points.\nClick Reset to reset the values.")
    return None

def result_display(demerit_result,drive_speed,speed_limit):
    '''
    Function tells calculate_points function what result to display handling the demerit_result arg
    Aim is to tidy up calculate points function and stop doubling up
    '''
    if demerit_result[1] != 0:
        if demerit_result[0]:
            printable = f"The mandatory penalty for driving at\n {drive_speed}km/h in a {speed_limit}km/h zone is {demerit_result[1]} points."
        else:
            printable = f"The discretional penalty for driving at\n {drive_speed}km/h in a {speed_limit}km/h zone is {demerit_result[1]} points."
    else:
        printable = f"{drive_speed}km/h in a {speed_limit}km/h is not speeding."
    return printable

def calculate_points(event):
    '''
    Function runs the demerit points calculation from Q1 taking inputs from the GUI
    '''
    ds = driving_speed_entry.get()
    sl = speed_limit_option.get()
    to = towing_option.get()
    so = school_option.get()
    ho = holiday_option.get()
    clear_answer()

    if ds.strip():
        if ds.isdigit():
            ds = int(ds)
            sl = int(sl)
            demerit_result = get_demerit_points(ds, sl, to, so, ho)
            printable = result_display(demerit_result,ds,sl)
            demerit_result_label = Label(answer_box_frame, text = f"{printable}")
            demerit_result_label.pack()
        elif ds.count(".") == 1 and ds.replace(".", "").isdigit():
            ds = float(ds)
            sl = int(sl)
            demerit_result = get_demerit_points(ds, sl, to, so, ho)
            printable = result_display(demerit_result,ds,sl)
            demerit_result_label = Label(answer_box_frame, text = f"{printable}")
            demerit_result_label.pack()
        else:
            speed_numeric_label = Label(answer_box_frame, text = "The driving speed needs to be numeric.")
            speed_numeric_label.pack()
    else:
        please_enter_label = Label(answer_box_frame, text = "Please enter a driving speed.")
        please_enter_label.pack()

    return None


VERSION = 1.0
# Placeholder for lambda functions needed for event calls to functions
PLACEHOLDER = " "

main_window = Tk()
main_window.title("Demerit points calculator")
main_window.geometry("380x160")
main_window.resizable(width = False, height = False)

# Main program section
# Driven speed entry
input_frame = Frame(main_window)
input_frame.pack(anchor=W)
description = Label(input_frame, text = "Driving speed") 
description.grid(row=0,column=0)

driving_speed_entry = StringVar()
text_field = Entry(input_frame, textvariable = driving_speed_entry) # use driving_speed_entry.get() to call later
text_field.grid(row=0, column=1)
text_field.focus()

#speed limit radiobuttons
speed_limit_option = IntVar()
speed_limit_frame = Frame(main_window)
speed_limit_frame.pack(anchor=W)
radio_label = Label(speed_limit_frame, text = "Speed limit:")
radio_label.pack(side=LEFT)

radiobutton_a = Radiobutton(speed_limit_frame, text="30km/h", variable = speed_limit_option, value = 30)
radiobutton_b = Radiobutton(speed_limit_frame, text="50km/h", variable = speed_limit_option, value = 50)
radiobutton_c = Radiobutton(speed_limit_frame, text="100km/h", variable = speed_limit_option, value = 100)
radiobutton_a.pack(side=LEFT)
radiobutton_b.pack(side=LEFT)
radiobutton_c.pack(side=LEFT)
radiobutton_b.select()


#special conditions check boxes
checkbox_frame = Frame(main_window)
checkbox_frame.pack(anchor=W)

towing_option = BooleanVar()
school_option = BooleanVar()
holiday_option = BooleanVar()

towing_tick = Checkbutton(checkbox_frame, text="Towing light trailer", variable = towing_option)
towing_tick.pack(side=LEFT)
towing_tick.deselect()

school_tick = Checkbutton(checkbox_frame, text="In school zone", variable = school_option)
school_tick.pack(side=LEFT)
school_tick.deselect()

holiday_tick = Checkbutton(checkbox_frame, text="Holiday period", variable = holiday_option)
holiday_tick.pack(side=LEFT)
holiday_tick.deselect()


# Calc & Reset Buttons & Answer box
bottom_options_frame = Frame(main_window)
bottom_options_frame.pack()

# calc button
calculate_points_button = Button(bottom_options_frame, text = "Calculate points", command = lambda: calculate_points(PLACEHOLDER))
calculate_points_button.grid(row=0,column=0)
# reset button
reset_button = Button(bottom_options_frame, text = "Reset", command = reset_fields) 
reset_button.grid(row=0,column=1)
# calc anwer box frame
answer_box_frame = Frame(main_window)
answer_box_frame.pack()

# MENU SYSTEM

menu_bar = Menu(main_window)

speed_menu = Menu(menu_bar, tearoff=0)
speed_menu.add_command(label = "Calculate points", command = lambda: calculate_points(PLACEHOLDER))
speed_menu.add_command(label = "Reset", command = reset_fields)
speed_menu.add_separator()
speed_menu.add_command(label = "Exit", command = lambda: exit_program(PLACEHOLDER))
menu_bar.add_cascade(label = "Speed", menu = speed_menu)

help_menu = Menu(menu_bar, tearoff=0)
help_menu.add_command(label = "Display instructions", command = help_menu_handler)
help_menu.add_command(label = "About", command = lambda: help_menu_handler(VERSION))
menu_bar.add_cascade(label = "Help", menu = help_menu)

# Main commands and setup
main_window.config(menu = menu_bar)
main_window.bind("<Return>", calculate_points)
main_window.bind("<Escape>", exit_program)
main_window.protocol("WM_DELETE_WINDOW", lambda: exit_program(PLACEHOLDER))

main_window.mainloop()