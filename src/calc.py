import tkinter as tk

root = tk.Tk()

root.title("Windows Calculator Replica")
root.iconbitmap("images/calc-icon.ico")
root.geometry("329x379")
root["bg"] = "#343434"

e = tk.Entry(root, width=17, font=("Helvetica", 25), bg="#343434", fg="white")
e.insert(0, "0")
e.grid(row=0, column=0, columnspan=4)
