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
                                
def sub_numbers():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        result =num1 - num2
        messagebox.showinfo("Result", f"The result of adding {num1} and {num2} is {result}")
    except ValueError:
        messagebox.showerror("Error","please enter valid numbers.")

def div_numbers():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        result =num1 / num2
        messagebox.showinfo("Result", f"The result of adding {num1} and {num2} is {result}")
    except ValueError:
        messagebox.showerror("Error","please enter valid numbers.")
def mul_numbers():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        result =num1 *  num2
        messagebox.showinfo("Result", f"The result of adding {num1} and {num2} is {result}")
    except ValueError:
        messagebox.showerror("Error","please enter valid numbers.")


root=tk.Tk()
root.title("simple")
tk.Label(root,text="add:").grid(row=0,column=0,padx=10,pady=10)
tk.Label(root,text="sub:").grid(row=1,column=0,padx=10,pady=10)
tk.Label(root,text="div:").grid(row=2,column=0,padx=10,pady=10)
tk.Label(root,text="mul:").grid(row=2,column=1,padx=10,pady=10)

entry1=tk.Entry(root)
entry1.grid(row=0,column=1,padx=10,pady=10)
entry2=tk.Entry(root)
entry2.grid(row=1,column=1,padx=10,pady=10)

add_button=tk.Button(root,text="add",command=add_numbers)
add_button.grid(row=3,column=1,padx=10,pady=10)

sub_button=tk.Button(root,text="sub",command=sub_numbers)
sub_button.grid(row=3,column=0,padx=10,pady=10)

div_button=tk.Button(root,text="div",command=div_numbers)
div_button.grid(row=2,column=0,padx=10,pady=10)

mul_button=tk.Button(root,text="mul",command=mul_numbers)
mul_button.grid(row=2,column=1,padx=10,pady=10)
root.mainloop()




