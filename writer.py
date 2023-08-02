import json
import customtkinter as ctk
import tkinter.messagebox as messagebox

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
        existing_data = {}
    existing_data.update(data)
    with open('files/student_data.json', 'w') as json_file:
        json.dump(existing_data, json_file, indent=4)

def register_report():
    name = entry.get()
    student_id = entry1.get()
    student_class = optionmenu.get()
    age = entry3.get()
    final_grade = entry4.get()

    studentdata = {
        name: {
            'id': student_id,
            'class': student_class,
            'age': age,
            'finalgrade': final_grade
        }
    }
    
    # checking if name already exist
    try:
        with open('files/student_data.json', 'r') as f:
            existing_data = json.load(f)
            if name in existing_data:
                messagebox.showinfo("Error", "Student with the same name already exists.")
                return
    except FileNotFoundError:
        pass  # No need to handle if the file doesn't exist yet

    register(studentdata)
    messagebox.showinfo("Success", "Student report registered successfully.")

label = ctk.CTkLabel(root, text="Create a student's report",
                     fg_color="transparent", font=('arial', 15))
entry = ctk.CTkEntry(master=root, width=200, font=("arial", 15), placeholder_text="Student's name...")
entry.place(x=20, y=60)
entry1 = ctk.CTkEntry(master=root, width=200, font=("arial", 15), placeholder_text="Student's ID...")
entry1.place(x=20, y=100)
optionmenu = ctk.CTkOptionMenu(master=root, width=200, values=["6eme", "5eme", "4eme", "3eme"], fg_color='gray', font=("arial", 15))
optionmenu.place(x=20, y=140)
optionmenu.set("6eme")
entry3 = ctk.CTkEntry(master=root, width=200, font=("arial", 15), placeholder_text="Student's age...")
entry3.place(x=20, y=180)
entry4 = ctk.CTkEntry(master=root, width=200, font=("arial", 15), placeholder_text="Student's final grade...")
entry4.place(x=20, y=220)
label.place(x=25, y=25)
button = ctk.CTkButton(master=root, width=200, text="Register Report", command=register_report, font=("arial", 15))
button.place(x=20, y=260)

root.mainloop()