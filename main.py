import customtkinter as ctk
import json


def final_grade(firstname, lastname):
    with open('files/' + firstname.lower() + '_' + lastname.lower() + '.json') as f:
        data = json.load(f)

    # grades
    subjects = data['SUBJECTS']
    maths = data['MATHS']
    pc = data['PC']
    english = data['ENGLISH']
    science = data['SCIENCE']
    i = (maths + pc + english + science)//subjects
    return i


def give_grade(grade):
    if grade < 10:
        return "F"
    elif grade < 12 and grade > 10:
        return 'D'
    elif grade < 14 and grade > 12:
        return 'C'
    elif grade < 16 and grade > 14:
        return 'B-'
    elif grade < 18 and grade > 16:
        return 'B+'
    elif grade < 20 and grade > 18:
        return 'A'
    elif grade == 20:
        return "A+"
    else:
        return


def get_class(firstname, lastname):
    with open('files/' + firstname.lower() + '_' + lastname.lower() + '.json') as f:
        data = json.load(f)
    classs = data["CLASS"]
    return classs


root = ctk.CTk()
root.geometry('640x480')
root.minsize(640, 480)
root.maxsize(640, 480)
root.title("SchoolSys Reader")

label = ctk.CTkLabel(root, text="Type a student's name to get his report...",
                     fg_color="transparent", font=('arial', 15))
label.place(x=20, y=25)
# label.pack()


def draw_report(grade):
    # progressbar = ctk.CTkProgressBar(root, orientation="horizontal")
    # progressbar.configure(mode="indeterminate", variable= grade)
    finalgrade = ctk.CTkLabel(root, text=(
        "Final Grade : " + grade), fg_color="transparent", font=('arial', 20))
    finalgrade.place(x=20, y=100)

def on_enter(event):
    entry.delete(0, ctk.END)
    name = entry.get()
    grp = str(name).split("\n")
    if len(grp) == 2:
        print("noir")
        firstname = grp[0]
        lastname = grp[1]
        finalgrade = final_grade(firstname, lastname)
        grade = give_grade(finalgrade)
        classs = get_class(firstname, lastname)
        draw_report(grade=finalgrade)


entry = ctk.CTkEntry(master=root, width=200, font=("arial", 10))
entry.place(x=20, y=50)
entry.bind("<Return>", on_enter)

root.mainloop()
