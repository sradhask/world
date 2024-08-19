
import tkinter as tk
from tkinter import messagebox


celcius=float(entry1.get())
fahrenheight=float(entry2.get()) 
     
def celsius_to_fahrenheit(celsius):
    
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    
    return (fahrenheit - 32) * 5/9

root=tk.Tk()
root.title("simple adder")
tk.label(root,text="celsius to farenheit")
tk.label(root,text="farenheit to celsius")
entry1=tk.Entry
entry1.grid(row=0,column=0,padx=10,pady=10)
entry2=tk.Entry
entry1.grid(row=1,column=1,padx=10,pady=10)
add_button=tk.Button(root,text="celsius")
add_button=tk.Button(root,text="farenheit")
root.mainloop()
