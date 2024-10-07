from tkinter import *
import os

def shutdown():
    x = "shutdown /s /t 0"
    os.system(x)

def restart():
    y = "shutdown /r /t 0"
    os.system(y)

def logout():
    z = "shutdown /l"
    os.system(z)

# Developed by Himanshu Singh
master = Tk()
master.title("CYP")
master.geometry("230x230")
master.configure(bg="cadetblue1")

# Create Labels
Label(master, text="Choose what you want !!", bg="darkolivegreen1", font=("jost", 10)).pack(pady=20)

# Create Buttons
Button(master, text="Shutdown", command=shutdown, width=15).pack(pady=5)
Button(master, text="Restart", command=restart, width=15).pack(pady=5)
Button(master, text="Log Out", command=logout, width=15).pack(pady=5)

master.mainloop()
