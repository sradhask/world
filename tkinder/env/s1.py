import tkinter as tk
from tkinter import messagebox

def celsius_to_fahrenheit():
    try:
        celsius = float(entry1.get())
        fahrenheit = (celsius * 9/5) + 32
        messagebox.showinfo("Result", f"{celsius}°C is {fahrenheit}°F")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number.")

def fahrenheit_to_celsius():
    try:
        fahrenheit = float(entry1.get())
        celsius = (fahrenheit - 32) * 5/9
        messagebox.showinfo("Result", f"{fahrenheit}°F is {celsius}°C")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number.")

root = tk.Tk()
root.title("Temperature Converter")

tk.Label(root, text="Celsius to Fahrenheit").grid(row=0, column=0, padx=10, pady=10)
tk.Label(root, text="Fahrenheit to Celsius").grid(row=0, column=1, padx=10, pady=10)

entry1 = tk.Entry(root)
entry1.grid(row=1, column=0, padx=10, pady=10)

tk.Button(root, text="Convert to Fahrenheit", command=celsius_to_fahrenheit).grid(row=2, column=0, padx=10, pady=10)
tk.Button(root, text="Convert to Celsius", command=fahrenheit_to_celsius).grid(row=2, column=1, padx=10, pady=10)

root.mainloop()
