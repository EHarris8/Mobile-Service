#Emma Harris-Broad
#Version 6 - final fixups

import tkinter as tk
from tkinter import ttk
from tkinter import *
from functools import partial
import math

#creating the frame
class mobile_service:
    def __init__(self, parent):
        self.frame = Frame(width=300, pady=10, padx=10)
        self.frame.grid()
        #logo
        img = PhotoImage(file='logo.png')
        self.logo_label = Label(self.frame, image=img)
        self.logo_label.img = img
        self.logo_label.grid(row=0)
        self.jobs_list = []

        self.error_frame= Frame(self.frame)
        self.error_frame.grid(row=1)
        #job number entry
        self.label=Label(self.frame, text='Enter Job Number Here')
        self.label.grid(row=2)
        self.job_number_entry = Entry(self.frame)
        self.job_number_entry.grid(row=3)
        #if error, shows up underneath
        self.job_errors_label = Label(self.error_frame, text="")
        self.job_errors_label.grid(row=4)
        #customer name entry    
        self.label=Label(self.frame, text='Enter Customer Name Here')
        self.label.grid(row=5)
        self.customer_name_entry = Entry(self.frame)
        self.customer_name_entry.grid(row=6)
        #if error, shows up underneath
        self.customer_name_errors_label = Label(self.error_frame, text="")
        self.customer_name_errors_label.grid(row=7)
        #distance travelled entry
        self.label=Label(self.frame, text='Enter Distance Travelled to Customer Here in Kilometers')
        self.label.grid(row=8)
        self.distance_entry = Entry(self.frame)
        self.distance_entry.grid(row=9)
        #if error, shows up underneath
        self.distance_errors_label = Label(self.error_frame, text="")
        self.distance_errors_label.grid(row=10)
        #virus protection minutes entry   
        self.label=Label(self.frame, text='Enter Minutes Spent on Virus Protection Here')
        self.label.grid(row=11)
        self.virus_minutes_entry = Entry(self.frame)
        self.virus_minutes_entry.grid(row=12)
        #if error, shows up underneath
        self.virus_errors_label = Label(self.error_frame, text="")
        self.virus_errors_label.grid(row=13)
        #wof and tune entry 
        self.label=Label(self.frame, text='Did the Job Require WOF and Tune services? y/n')
        self.label.grid(row=14)
        self.wof_tune_entry = Entry(self.frame)
        self.wof_tune_entry.grid(row=15)
        #if error, shows up underneath
        self.wof_tune_errors_label = Label(self.error_frame, text="")
        self.wof_tune_errors_label.grid(row=16)
        #submit button
        self.submit_button = ttk.Button(self.frame, text="Enter Job", command=self.check)
        self.submit_button.grid(row=18)
        #show all jobs button
        self.all_jobs_button = ttk.Button(self.frame, text="Show All Jobs", command=lambda: self.all_jobs(self.jobs_list))
        self.all_jobs_button.grid(row=19)
    #checking for errors in entries
    def check(self):
        job_num = self.job_number_entry.get()
        customer_name = self.customer_name_entry.get()
        distance = self.distance_entry.get()
        virus_minutes = self.virus_minutes_entry.get()
        wof_tune = self.wof_tune_entry.get()
        #to change the error label underneath the corresponding entry box
        self.job_errors_label.config(text="")
        self.distance_errors_label.config(text="")
        self.virus_errors_label.config(text="")
        self.customer_name_errors_label.config(text="")
        self.wof_tune_errors_label.config(text="")
        try:
            job_num = int(job_num)
            job_errors = "n"

            if job_num < 0:
                job_errors = "y"
                error = "Please enter a number above zero."
                self.job_errors_label.config(text=error)
        except ValueError:
            job_errors ="y"
            error = "Please enter an acceptable job number (no text/decimals/negatives)."
            self.job_errors_label.config(text=error)
        try:
            distance = float(distance)
            distance_error ="n"

            if distance <= 0 or distance > 100:
                distance_error = "y"
                error = "Please enter an acceptable distance between 0 - 100 in kilometres."
                self.distance_errors_label.config(text=error)
        except ValueError:
            distance_error = "y"
            error = "Please enter a number (no text required)."
            self.distance_errors_label.config(text=error)
        try:
            virus_minutes = int(virus_minutes)
            virus_error = "n"

            if virus_minutes < 1 or virus_minutes > 300:
                virus_error = "y"
                error = "Please enter an acceptable time taken on virus protection in minutes between 0 to 300."
                self.virus_errors_label.config(text=error)
        except ValueError:
            virus_error = "y"
            error = "Please enter an acceptable number of minutes (no text/decimals/negatives)."
            self.virus_errors_label.config(text=error)
        customer_error = "n"
        if customer_name == "":
            customer_error = "y"
            error = "Please enter a customer name."
            self.customer_name_errors_label.config(text=error)
        try:
            if wof_tune == "y" or wof_tune == "n":
                wof_tune_error = "n"
            else:
                wof_tune_error = "y"
                error = "Please enter either a 'y' for yes or an 'n' for no."
                self.wof_tune_errors_label.config(text=error)
        except ValueError:
            wof_tune_error = "y"
            error = "Please enter either a 'y' for yes or an 'n' for no."
            self.wof_tune_errors_label.config(text=error)
        #once there are no errors it will submit the jobs
        if job_errors == "n" and distance_error == "n" and virus_error == "n" and customer_error == "n" and wof_tune_error == "n":
            self.submit(self)
    def all_jobs(self, jobs_list):
        alljobs(self,jobs_list)
    #submit button (enter job)
    def submit(self, partner):
        self.job_num = self.job_number_entry.get()
        self.customer_name = self.customer_name_entry.get()
        self.distance = self.distance_entry.get()
        self.virus_minutes = self.virus_minutes_entry.get()
        self.virus_minutes = float(self.virus_minutes)
        self.wof_tune = self.wof_tune_entry.get()
        self.wof_tune = self.wof_tune.upper()
        self.distance = float(self.distance)
        self.cost = 10
        self.cost = int(self.cost)
        round(self.distance)
        #calculating distance
        if self.distance > 5:
            self.distance_cost=(self.distance-5) * 0.5 
            self.cost += self.distance_cost
        #wof tune calculation
        if self.wof_tune == 'Y':
            self.cost += 100
        #virus minutes calculation
        self.virus_cost = self.virus_minutes * .8
        self.cost += self.virus_cost
        print(self.cost)
        #calculate cost
        self.jobs_info = f"""Job Number: {self.job_num}
    Customer Name: {self.customer_name}
    Total Cost: ${self.cost:.2f}
    """
        self.jobs_list.append(self.jobs_info)
#show all jobs button
class alljobs():
    def __init__(self, partner, jobs_list):
        self.counter = 0
        #frame set up
        self.all_jobs_box = Toplevel()
        self.all_jobs_frame = Frame(self.all_jobs_box)
        self.all_jobs_frame.grid()
        #logo set up
        img = PhotoImage(file='logo.png')
        self.logo_label = Label(self.all_jobs_frame, image=img)
        self.logo_label.img = img
        self.logo_label.grid(row=0)

        self.all_jobs_heading = Label(self.all_jobs_frame, text = "All Jobs")
        self.all_jobs_heading.grid(row=1)

        self.all_jobs_display = Frame(self.all_jobs_frame)
        self.all_jobs_display.grid(row=2)

        self.all_jobs_summary = Label(self.all_jobs_display, text=jobs_list[self.counter])
        self.all_jobs_summary.grid(row=0)

        self.all_jobs_buttons_frame = Frame(self.all_jobs_frame)
        self.all_jobs_buttons_frame.grid(row=3)
        #previous button
        self.previous_button = Button(self.all_jobs_buttons_frame, text="Previous", state=DISABLED, command=lambda:self.previous_but(self.counter, jobs_list))
        self.previous_button.grid(row=0, column = 0)
        #next button
        self.next_button = Button(self.all_jobs_buttons_frame, text="Next", command=lambda:self.next_but(self.counter, jobs_list))
        self.next_button.grid(row=0, column = 1)
        #if only one job has been submitted, next button is disabled
        if len(jobs_list) == 1:
            self.next_button.config(state=DISABLED)
    #when next button is pressed it cycles through the job list 
    def next_but(self, counter, jobs_list):
        self.counter += 1
        self.all_jobs_summary.config(text=jobs_list[self.counter])
        self.check_but(jobs_list)
    #opposite of next button
    def previous_but(self, counter, jobs_list):
        self.counter -=1
        self.all_jobs_summary.config(text=jobs_list[self.counter])
        self.check_but(jobs_list)
    #checking if the next button and previous button should be disabled or not
    def check_but(self, jobs_list):
        if self.counter < len(jobs_list)-1:
            self.next_button.config(state=NORMAL)
        if self.counter == len(jobs_list)-1:
            self.next_button.config(state=DISABLED)
        if self.counter > 0:
            self.previous_button.config(state=NORMAL)
        if self.counter == 0:
            self.previous_button.config(state=DISABLED)
    

#main routine
if __name__ =="__main__":
    root = tk.Tk()
    root.title("Suzy's Professional Mobile Service")
    something = mobile_service(root)
    root.mainloop()
