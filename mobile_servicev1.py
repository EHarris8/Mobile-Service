#Emma Harris-Broad

import tkinter as tk
from tkinter import ttk
from tkinter import *
from functools import partial
import math


root = tk.Tk()
frame = Frame(width=300, pady=10, padx=10)
frame.grid()
root.title("Suzy's Professional Mobile Service")
#display business logo

label=Label(root, text='Enter Job Number Here')
label.grid(row=0)
job_number_entry = Entry(root)
job_number_entry.grid(row=1)

label=Label(root, text='Enter Customer Name Here')
label.grid(row=2)
customer_name_entry = Entry(root)
customer_name_entry.grid(row=3)

label=Label(root, text='Enter Distance Travelled to Customer Here in Kilometers')
label.grid(row=4)
distance_entry = Entry(root)
distance_entry.grid(row=5)

label=Label(root, text='Enter Minutes Spent on Virus Protection Here')
label.grid(row=6)
virus_minutes_entry = Entry(root)
virus_minutes_entry.grid(row=7)

label=Label(root, text='Did the Job Require WOF and Tune services? Y/N')
label.grid(row=8)
wof_tune_entry = Entry(root)
wof_tune_entry.grid(row=9)

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
    float(virus_minutes)
    wof_tune = wof_tune_entry.get()
    str(wof_tune)
    wof_tune = wof_tune.upper()
    distance = float(distance)
    distance = round(distance)
    if distance <= 5:
        distance_cost = 10
        print(distance_cost)
    elif distance > 5:
        distance_cost=(distance-5) * 0.5 + 10
        print(distance_cost)
        return distance_cost
    if wof_tune == 'Y':
        wof_cost = 100
        print(wof_cost)
    elif wof_tune == 'N':
        wof_cost = 0
        print(wof_cost)
    else:
        print('Invalid WOF statement')
        
def all_jobs():
    print(distance_cost)
    
submit_button = ttk.Button(root, text="Enter Job", command=submit)
submit_button.grid(row=10)
all_jobs_button = ttk.Button(root, text="Show All Jobs", command=all_jobs)
all_jobs_button.grid(row=11)


root.mainloop()
