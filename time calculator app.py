import tkinter as tk
from tkinter import messagebox
import datetime

# Create the main application window
root = tk.Tk()
root.title("Videos Time Calculator")  # Set window title
root.geometry("300x450")  # Set window size

# List to store tasks
tasks = []
total_time = 0

def add_duration():
    """Adds a task to the list."""

    global total_time
    seconds = seconds_entry.get()  # Get task from the entry field
    minutes = minutes_entry.get()
    hours = hours_entry.get()

    if not seconds:
        seconds = 0
    if not minutes:
        minutes = 0
    if not hours:
        hours = 0

    time = int(seconds) +  60*int(minutes) + 3600*int(hours)
    if time > 0:
        tasks.append(time)  # Add task to the list
        task_listbox.insert(tk.END, str(datetime.timedelta(seconds=time)))  # Display task in the listbox
        total_time += int(time)
        total_time_label['text'] = str(datetime.timedelta(seconds=int(total_time)))
        speed_time_label['text'] = str(datetime.timedelta(seconds=int(round(total_time/1.75))))
        seconds_entry.delete(0, tk.END)  # Clear input field
        minutes_entry.delete(0, tk.END)
        hours_entry.delete(0, tk.END)

    else:
        messagebox.showwarning("Warning", "Input cannot be empty or negative!")  # Show warning if input is empty

def remove_duration():
    """Removes selected task from the list."""
    global total_time
    try:
        selected_task_index = task_listbox.curselection()[0]  # Get index of selected task
        total_time -= int(tasks[selected_task_index])
        total_time_label['text'] = str(datetime.timedelta(seconds=total_time))
        speed_time_label['text'] = str(datetime.timedelta(seconds=int(round(total_time/1.75))))
        task_listbox.delete(selected_task_index)  # Remove task from listbox
        del tasks[selected_task_index]  # Remove task from the list

    except IndexError:
        messagebox.showwarning("Warning", "No duration selected!")  # Show warning if no task is selected

# Creating input field, buttons, and task list
root.rowconfigure(0, weight=2)
root.rowconfigure(1, weight=2)
root.rowconfigure(2, weight=2)
root.rowconfigure(3, weight=2)
root.rowconfigure(4, weight=2)
root.rowconfigure(5, weight=2)
root.rowconfigure(6, weight=2)
root.columnconfigure(0, weight=2)
root.columnconfigure(1, weight=2)
root.columnconfigure(2, weight=2)

hours_entry = tk.Entry(root, width=12)  # Input field for entering tasks
hours_entry.grid(column=0,row=1)

hours_entry_label = tk.Label(root, width=12, height=1, text="Hours:")
hours_entry_label.config(state='disabled')
hours_entry_label.grid(column=0,row=0)

minutes_entry = tk.Entry(root, width=12)  # Input field for entering tasks
minutes_entry.grid(column=1,row=1)

minutes_entry_label = tk.Label(root, width=12, height=1, text="Minutes:")
minutes_entry_label.config(state='disabled')
minutes_entry_label.grid(column=1,row=0)

seconds_entry = tk.Entry(root, width=12)  # Input field for entering tasks
seconds_entry.grid(column=2,row=1)

seconds_entry_label = tk.Label(root, width=12, height=1, text="Seconds:")
seconds_entry_label.config(state='disabled')
seconds_entry_label.grid(column=2,row=0)

total_time_label = tk.Label(root, width=20, height=1, text="Total time:")
total_time_label.config(state='disabled')
total_time_label.grid(column=0,row=2)

total_time_label = tk.Label(root, width=20, height=1, text=str(datetime.timedelta(seconds=total_time)))
total_time_label.config(state='disabled')
total_time_label.grid(column=0,row=3)

speed_time_label = tk.Label(root, width=20, height=1, text="Sped up time:")
speed_time_label.config(state='disabled')
speed_time_label.grid(column=2,row=2)

speed_time_label = tk.Label(root, width=20, height=1, text=str(datetime.timedelta(seconds=round(total_time/1.75))))
speed_time_label.config(state='disabled')
speed_time_label.grid(column=2,row=3)

arrow = tk.Label(root, width=20, height=1, text="-->")
arrow.config(state='disabled')
arrow.grid(column=1,row=2,rowspan=2)

add_button = tk.Button(root, text="Add duration", command=add_duration)  # Button to add tasks
add_button.grid(column=0,row=4,columnspan=3)  # Display the button

remove_button = tk.Button(root, text="Remove duration", command=remove_duration)  # Button to remove tasks
remove_button.grid(column=0,row=5,columnspan=3)  # Display the button

task_listbox = tk.Listbox(root, width=40, height=15)  # Listbox to display tasks
task_listbox.grid(column=0,row=6,columnspan=3)  # Add spacing around the listbox

# Run the application
root.mainloop()