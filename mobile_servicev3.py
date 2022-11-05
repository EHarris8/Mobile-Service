#Emma Harris-Broad
#Version 3

import tkinter as tk
from tkinter import ttk
from tkinter import *
from functools import partial
import math

#creating the frame
root = tk.Tk()
frame = Frame(width=300, pady=10, padx=10)
frame.grid()
root.title("Suzy's Professional Mobile Service")
img = PhotoImage(file='logo.png')
logo_label = Label(root, image=img)
logo_label.img = img
logo_label.grid(row=0)
jobs_list = []

label=Label(root, text='Enter Job Number Here')
label.grid(row=1)
job_number_entry = Entry(root)
job_number_entry.grid(row=2)

label=Label(root, text='Enter Customer Name Here')
label.grid(row=3)
customer_name_entry = Entry(root)
customer_name_entry.grid(row=4)

label=Label(root, text='Enter Distance Travelled to Customer Here in Kilometers')
label.grid(row=5)
distance_entry = Entry(root)
distance_entry.grid(row=6)

label=Label(root, text='Enter Minutes Spent on Virus Protection Here')
label.grid(row=7)
virus_minutes_entry = Entry(root)
virus_minutes_entry.grid(row=8)

label=Label(root, text='Did the Job Require WOF and Tune services? Y/N')
label.grid(row=9)
wof_tune_entry = Entry(root)
wof_tune_entry.grid(row=10)
#submit button (enter job)
def submit():
    global job_number_entry
    global customer_name_entry
    global distance_entry
    global virus_minutes_entry
    global wof_tune_entry
    job_num = job_number_entry.get()
    int(job_num)
    customer_name = customer_name_entry.get()
    str(customer_name)
    distance = distance_entry.get()
    virus_minutes = virus_minutes_entry.get()
    virus_minutes = float(virus_minutes)
    wof_tune = wof_tune_entry.get()
    str(wof_tune)
    wof_tune = wof_tune.upper()
    distance = float(distance)
    cost = 10
    cost = int(cost)
    round(distance)
    if distance > 5:
        distance_cost=(distance-5) * 0.5 + 10
        cost += distance_cost
    if wof_tune == 'Y':
        cost += 100
    virus_cost = virus_minutes * .8
    cost += virus_cost
    print(cost)
    #calculate cost
    jobs_info = f"""Job Number: {job_num}
Customer Name: {customer_name}
Total Cost: ${cost:.2f}
"""
    jobs_list.append(jobs_info)
#show all jobs button
def all_jobs():
    global counter
    counter = 0
    
    all_jobs_box = Toplevel()
    all_jobs_frame = Frame(all_jobs_box)
    all_jobs_frame.grid()

    img = PhotoImage(file='logo.png')
    logo_label = Label(all_jobs_frame, image=img)
    logo_label.img = img
    logo_label.grid(row=0)

    all_jobs_heading = Label(all_jobs_frame, text = "All Jobs")
    all_jobs_heading.grid(row=1)

    all_jobs_display = Frame(all_jobs_frame)
    all_jobs_display.grid(row=2)

    global all_jobs_summary
    all_jobs_summary = Label(all_jobs_display, text=jobs_list[counter])
    all_jobs_summary.grid(row=0)

    all_jobs_buttons_frame = Frame(all_jobs_frame)
    all_jobs_buttons_frame.grid(row=3)
    global previous_button
    previous_button = Button(all_jobs_buttons_frame, text="Previous", state=DISABLED, command=lambda:previous_but(counter, jobs_list))
    previous_button.grid(row=0, column = 0)
    global next_button
    next_button = Button(all_jobs_buttons_frame, text="Next", command=lambda:next_but(counter, jobs_list))
    next_button.grid(row=0, column = 1)
    if len(jobs_list) == 1:
        next_button.config(state=DISABLED)
    def next_but(counter, jobs_list):
        counter += 1
        all_jobs_summary.config(text=jobs_list[counter])
        check(jobs_list)

    def previous_but(counter, jobs_list):
        counter -=1
        all_jobs_summary.config(text=jobs_list[counter])
        check(jobs_list)
    
    def check(jobs_list):
        if counter < len(jobs_list)-1:
            next_button.config(state=NORMAL)
        if counter == len(jobs_list)-1:
            next_button.config(state=DISABLED)
        if counter > 0:
            previous_button.config(state=NORMAL)
        if counter == 0:
            previous_button.config(state=DISABLED)
    
submit_button = ttk.Button(root, text="Enter Job", command=submit)
submit_button.grid(row=11)
all_jobs_button = ttk.Button(root, text="Show All Jobs", command=all_jobs)
all_jobs_button.grid(row=12)


root.mainloop()
