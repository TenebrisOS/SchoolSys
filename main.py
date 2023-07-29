import customtkinter as ctk
import json

with open('files/student_data.json') as f:
    data = json.load(f)

root = ctk.CTk()
root.geometry('640x480')
root.minsize(640, 480)
root.maxsize(640, 480)
root.title("SchoolSys Reader")

label = ctk.CTkLabel(root, text="Type a student's name to get his report...",
                     fg_color="transparent", font=('arial', 15))
label.place(x=20, y=25)
# label.pack()


def draw_report(grade, age, classes, id):
    # progressbar = ctk.CTkProgressBar(root, orientation="horizontal")
    # progressbar.configure(mode="indeterminate", variable= grade)
    agectk = ctk.CTkLabel(root, text=(
        "Age : " + str(age)), fg_color="transparent", font=('arial', 20))
    agectk.place(x=20, y=150)
    classctk = ctk.CTkLabel(root, text=(
        "Class : " + str(classes)), fg_color="transparent", font=('arial', 20))
    classctk.place(x=20, y=200)
    idctk = ctk.CTkLabel(root, text=(
        "ID : " + str(id)), fg_color="transparent", font=('arial', 20))
    idctk.place(x=20, y=250)
    finalgrade = ctk.CTkLabel(root, text=(
        "Final Grade : " + str(grade)), fg_color="transparent", font=('arial', 20))
    finalgrade.place(x=20, y=100)
    if grade > 10:
        label = ctk.CTkLabel(root, text=("Admitted !!"),
                             text_color="green", font=('arial', 40))
        label.place(x=200, y=90)


def on_enter(event):
    name = entry.get()
    entry.delete(0, ctk.END)
    print(name)
    correctedName = name.title()
    studentdata = data[correctedName]
    id = studentdata["id"]
    classes = studentdata['class']
    age = studentdata['age']
    grade = studentdata['finalgrade']
    draw_report(grade=grade, age=age, classes=classes, id=id)


entry = ctk.CTkEntry(master=root, width=200, font=("arial", 15))
entry.place(x=20, y=50)
entry.bind("<Return>", on_enter)

root.mainloop()
