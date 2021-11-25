import tkinter as tk

def main():
    root = tk.Tk()
    goBtn = tk.Button(master=root, text="-")
    goBtn.grid(row=0, column=0, sticky="nsew")
