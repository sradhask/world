import tkinter as tk
from tkinter import messagebox
def add_numbers():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        result =num1 + num2
        messagebox.showinfo("Result", f"The result of adding {num1} and {num2} is {result}")
    except ValueError:
        messagebox.showerror("Error","please enter valid numbers.")
                                

root=tk.Tk()
root.title("simple")
tk.Label(root,text="add:").grid(row=0,column=0,padx=10,pady=10)
tk.Label(root,text="sub:").grid(row=1,column=0,padx=10,pady=10)
tk.Label(root,text="mul:").grid(row=2)