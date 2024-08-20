
import tkinter as tk
from tkinter import messagebox

root=tk.Tk()
root.title("simple adder")

tk.Label(root,text="celsius to farenheit")
tk.Label(root,text="farenheit to celsius")
entry1=tk.Entry(root)
entry1.grid(row=1,column=1,padx=10,pady=10)
add_button=tk.Button(root,text="celsius")

num1=float(entry1.get())
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9
root.mainloop()
