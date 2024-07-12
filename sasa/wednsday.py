from datetime import datetime
import tkinter as tk
from tkinter import ttk

class Clinic:
    def __init__(self, day, start_time, end_time, doctor, room, specialty, sub_specialty):
        self.day = day
        self.start_time = start_time
        self.end_time = end_time
        self.doctor = doctor
        self.room = room
        self.specialty = specialty
        self.sub_specialty = sub_specialty

    def __str__(self):
        return f"{self.day}, {self.start_time.strftime('%H:%M')}-{self.end_time.strftime('%H:%M')}, {self.doctor}, {self.room}, {self.specialty}, {self.sub_specialty}"

def convert_time(time_str):
    return datetime.strptime(time_str, '%H:%M')


# Define the clinic schedule
clinics = [
        Clinic('Wednesday', convert_time('08:00'), convert_time('09:00'), 'Dr. Harris', 'Room 115', 'Cardiology', 'Pediatric Cardiology'),
        Clinic('Wednesday', convert_time('09:00'), convert_time('10:00'), 'Dr. Clark', 'Room 116', 'Neurology', 'Epilepsy'),
        Clinic('Wednesday', convert_time('10:00'), convert_time('11:00'), 'Dr. Lewis', 'Room 117', 'Oncology', 'Radiation Oncology'),
        Clinic('Wednesday', convert_time('11:00'), convert_time('12:00'), 'Dr. Walker', 'Room 118', 'Pediatrics', 'Neonatology'),
        Clinic('Wednesday', convert_time('12:00'), convert_time('13:00'), 'Dr. Hall', 'Room 119', 'Orthopedics', 'Sports Medicine'),
        Clinic('Wednesday', convert_time('13:00'), convert_time('14:00'), 'Dr. Allen', 'Room 120', 'Gastroenterology', 'Hepatology'),
        Clinic('Wednesday', convert_time('14:00'), convert_time('15:00'), 'Dr. Young', 'Room 121', 'Pulmonology', 'Sleep Medicine')
]

# Create the main application window
root = tk.Tk()
root.title("Clinic Schedule")
root.geometry("800x400")

# Create a Treeview widget
tree = ttk.Treeview(root, columns=("Day", "Start Time", "End Time", "Doctor", "Room", "Specialty", "Sub-Specialty"), show='headings')
tree.pack(padx=20, pady=20, fill=tk.BOTH, expand=True)

# Define the column headings
tree.heading("Day", text="Day")
tree.heading("Start Time", text="Start Time")
tree.heading("End Time", text="End Time")
tree.heading("Doctor", text="Doctor")
tree.heading("Room", text="Room")
tree.heading("Specialty", text="Specialty")
tree.heading("Sub-Specialty", text="Sub-Specialty")

# Define the column widths
tree.column("Day", width=100)
tree.column("Start Time", width=100)
tree.column("End Time", width=100)
tree.column("Doctor", width=150)
tree.column("Room", width=100)
tree.column("Specialty", width=150)
tree.column("Sub-Specialty", width=150)

# Insert the clinic details into the Treeview
for clinic in clinics:
    tree.insert("", tk.END, values=(clinic.day, clinic.start_time.strftime('%H:%M'), clinic.end_time.strftime('%H:%M'), clinic.doctor, clinic.room, clinic.specialty, clinic.sub_specialty))

# Create a Terminate button
terminate_button = tk.Button(root, text="Terminate", command=root.destroy)
terminate_button.pack(pady=20)

# Run the application
root.mainloop()

