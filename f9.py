import tkinter as tk
from tkinter import ttk

def convert_temperature():
    try:
        temp = float(entry.get())
        from_unit = from_unit_combobox.get()
        to_unit = to_unit_combobox.get()
        
        if from_unit == to_unit:
            result.set(temp)
            return
        
        if from_unit == "Celsius":
            if to_unit == "Fahrenheit":
                result.set((temp * 9/5) + 32)
            elif to_unit == "Kelvin":
                result.set(temp + 273.15)
        elif from_unit == "Fahrenheit":
            if to_unit == "Celsius":
                result.set((temp - 32) * 5/9)
            elif to_unit == "Kelvin":
                result.set(((temp - 32) * 5/9) + 273.15)
        elif from_unit == "Kelvin":
            if to_unit == "Celsius":
                result.set(temp - 273.15)
            elif to_unit == "Fahrenheit":
                result.set(((temp - 273.15) * 9/5) + 32)
    except ValueError:
        result.set("Invalid input")

# Create the main window
root = tk.Tk()
root.title("Temperature Converter")

# Create and place widgets
tk.Label(root, text="Temperature:").grid(row=0, column=0, padx=10, pady=10)
entry = tk.Entry(root)
entry.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="From:").grid(row=1, column=0, padx=10, pady=10)
from_unit_combobox = ttk.Combobox(root, values=["Celsius", "Fahrenheit", "Kelvin"])
from_unit_combobox.grid(row=1, column=1, padx=10, pady=10)
from_unit_combobox.set("Celsius")

tk.Label(root, text="To:").grid(row=2, column=0, padx=10, pady=10)
to_unit_combobox = ttk.Combobox(root, values=["Celsius", "Fahrenheit", "Kelvin"])
to_unit_combobox.grid(row=2, column=1, padx=10, pady=10)
to_unit_combobox.set("Fahrenheit")

convert_button = tk.Button(root, text="Convert", command=convert_temperature)
convert_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

result = tk.StringVar()
tk.Label(root, text="Result:").grid(row=4, column=0, padx=10, pady=10)
tk.Label(root, textvariable=result).grid(row=4, column=1, padx=10, pady=10)

# Run the application
root.mainloop()
