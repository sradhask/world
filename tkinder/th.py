import tkinter as tk
from tkinter import messagebox


celcius=float(entry1.get())
fahrenheight=float(entry2.get()) 
     
     
def fahrenheight to celcius(celcius):
try
     return (celsius* 9/5) + 32

def celcius to fahrenheight(fahrenheight):
           
     
      
       
root=tk.Tk()
root.title("simple adder")
label1=tk.Label(root,text="celsius to fahrenheit:")
entry1=tk.Entry()
label2=tk.Label(root,text="fahrenheight to celcius:")
entry2=tk.Entry()
button=tk.Button(root,text="submit")
label1.pack()
entry1.pack()
label2.pack()
entry2.pack()
button.pack()
root.mainloop()



