import sys
import os
import tkinter

def resource_path(relative_path):
    folder = getattr(sys, "_MEIPASS", os.path.abspath("."))
    return os.path.join(folder, relative_path)

# Create main window
window = tkinter.Tk()
window.title("Death Counter")
window.geometry("300x500")
window.config(bg="#121212")
window.resizable(False, False)

death_count = 0

# Save current death count to file
def save_death_count():
    with open("death_count.txt", "w") as file:
        file.write(str(death_count))

# Load saved death count from file        
def load_death():
    global death_count
    try:
        with open("death_count.txt", "r") as file:   
            death_count = int(file.read())
    except ValueError:
        death_count = 0
        
# Increase death count
def add_death():
    global death_count
    death_count = death_count + 1
    save_death_count()
    label.config(text=death_count)

# Decrease death count
def undo_death():
    global death_count

    if death_count > 0:
        death_count = death_count - 1
        save_death_count()
        label.config(text=death_count)

# Reset death count
def reset_death():
    global death_count
    death_count = 0
    save_death_count()
    label.config(text=death_count)

# Load saved count if save file exists
if os.path.exists("death_count.txt"):
    load_death()
else:
    death_count = 0   

# Create death count display
label = tkinter.Label(window, text=death_count, font=("Arial", 48), fg="#f2f2f2", bg="#121212")
label.place(relx=0.5, y=65, anchor="n")

# Create Writing-label
title_label = tkinter.Label(window, text="YOU DIED!", font=("Arial", 24, "bold" ), fg="#b00020")
title_label.place(relx=0.5, y=15, anchor="n")
title_label.config(bg="#121212")

# implement skull.png
skull_image = tkinter.PhotoImage(file=resource_path("skull_new.png"))
skull_image = skull_image.subsample(8)
skull_label = tkinter.Label(window, image=skull_image, bg="#121212")
skull_label.place(relx=0.5, y=140, anchor="n")

# Create death button
death_button = tkinter.Button(window, text="Death", command=add_death, bg="#2b2b2b", fg="#f2f2f2", activebackground="#b00020", activeforeground="#ffffff", font=("Arial", 12, "bold"), width=8, height=2, relief="flat", bd=0, cursor="hand2")
death_button.place(relx=0.75, y=345, anchor="n")

# Create undo button
undo_death_button = tkinter.Button(window, text="Undo", command=undo_death, bg="#2b2b2b", fg="#f2f2f2", activebackground="#b00020", activeforeground="#ffffff", font=("Arial", 12, "bold"), width=8, height=2, relief="flat", bd=0, cursor="hand2")
undo_death_button.place(relx=0.25, y=345, anchor="n")

# Create reset button
reset_button = tkinter.Button(window, text="Reset", command=reset_death, bg="#2b2b2b", fg="#f2f2f2", activebackground="#b00020", activeforeground="#ffffff", font=("Arial", 12, "bold"), width=8, height=2, relief="flat", bd=0, cursor="hand2")
reset_button.place(relx=0.5, y=405, anchor="n")

window.mainloop()