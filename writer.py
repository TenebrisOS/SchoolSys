import customtkinter as ctk
import json

root = ctk.CTk()
root.geometry('640x480')
root.minsize(640, 480)
root.maxsize(640, 480)
root.title("SchoolSys Writer")

label = ctk.CTkLabel(root, text="Create a student's report",
                     fg_color="transparent", font=('arial', 15))
entry = ctk.CTkEntry(master=root, width=200, font=("arial", 15), placeholder_text="Student's name...")
entry.place(x=20, y=60)
entry2 = ctk.CTkEntry(master=root, width=200, font=("arial", 15), placeholder_text="Student's class...")
entry2.place(x=20, y=100)
entry3 = ctk.CTkEntry(master=root, width=200, font=("arial", 15), placeholder_text="Student's age...")
entry3.place(x=20, y=140)
entry4 = ctk.CTkEntry(master=root, width=200, font=("arial", 15), placeholder_text="Student's final grade...")
entry4.place(x=20, y=180)
#entry.bind("<Return>", on_enter)
label.place(x=25, y=25)

root.mainloop()