import customtkinter as ctk
import json

root = ctk.CTk()
root.geometry('640x480')
root.minsize(640, 480)
root.maxsize(640, 480)
root.title("SchoolSys Writer")

def register(data):
    try:
        with open('files/student_data.json', 'r') as f:
            existing_data = json.load(f)
    except FileNotFoundError:
        # If the file doesn't exist yet, set existing_data to an empty list or dictionary
        existing_data = {}
    existing_data.update(data)
    with open('files/student_data.json', 'w') as json_file:
        json.dump(existing_data, json_file, indent=4)

def register_report():
    name = entry.get()
    student_id = entry1.get()
    student_class = entry2.get()
    age = entry3.get()
    final_grade = entry4.get()

    studentdata = {
            name : {
                'id' : student_id,
                'class' : student_class,
                'age' : age,
                'finalgrade' : final_grade
            }
        }
    register(studentdata)

label = ctk.CTkLabel(root, text="Create a student's report",
                     fg_color="transparent", font=('arial', 15))
entry = ctk.CTkEntry(master=root, width=200, font=("arial", 15), placeholder_text="Student's name...")
entry.place(x=20, y=60)
entry1 = ctk.CTkEntry(master=root, width=200, font=("arial", 15), placeholder_text="Student's ID...")
entry1.place(x=20, y=100)
entry2 = ctk.CTkEntry(master=root, width=200, font=("arial", 15), placeholder_text="Student's class...")
entry2.place(x=20, y=140)
entry3 = ctk.CTkEntry(master=root, width=200, font=("arial", 15), placeholder_text="Student's age...")
entry3.place(x=20, y=180)
entry4 = ctk.CTkEntry(master=root, width=200, font=("arial", 15), placeholder_text="Student's final grade...")
entry4.place(x=20, y=220)
#entry.bind("<Return>", on_enter)
label.place(x=25, y=25)
studentdata = {
            entry.get() : {
                'id' : entry1.get(),
                'class' : entry2.get(),
                'age' : entry3.get(),
                'finalgrade' : entry4.get()
            }
        }
button = ctk.CTkButton(master=root, width=200, text="Register Report", command=register_report)
button.place(x=20, y=260)

root.mainloop()