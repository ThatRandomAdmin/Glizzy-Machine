import tkinter as tk
from tkinter import *
from tkinter import filedialog as fd
from tkinter.ttk import *
import threading
import multiprocessing
import os
import shutil

def dupe(numberOf, fldr):
    y = 0
    for path in os.listdir(fldr):
        if os.path.isfile(os.path.join(fldr, path)):
            y += 1
    x = y + 1
    while get_directory_size(fldr) <= numberOf:
        savePath = fldr + 'glizzy' + str(x) + ".jpeg"
        shutil.copy('glizzy.jpeg', savePath)
        x += 1
        numberOf -= 1

def get_directory_size(directory):
    total = 0
    try:
        for entry in os.scandir(directory):
            if entry.is_file():
                total += entry.stat().st_size
            elif entry.is_dir():
                total += get_directory_size(entry.path)
    except NotADirectoryError:
        return os.path.getsize(directory)
    except PermissionError:
        return 0
    return total

def main():
    root = tk.Tk()
    root.title("Glizzy Machine!")
    root.resizable(False, False)

    label = tk.Label(master=root, width=20, height=2, text="Enter folder size:")
    label.config(font=("", 20))
    label.grid(row=0, column=0, columnspan=2, sticky="nsew")

    inputvar = tk.Text(master=root, height = 1, width = 20)
    inputvar.grid(row=1, column=0, sticky="nsew")

    label1 = tk.Label(master=root, width=20, height=2, text="Gigabytes")
    label1.grid(row=1, column=1, sticky="nsew")

    def refresh():
        label.configure(text="Enter folder size:")

    def go():
        numberOfgb = inputvar.get(1.0, "end-1c")
        if numberOfgb == "":
            label.configure(text="Please enter a number!")
            label.after(1200, refresh)
        else:
            try:
                float(numberOfgb)
            except ValueError:
                label.configure(text="Please enter a number!")
                label.after(1200, refresh)
            else:
                fldr = fd.askdirectory() + "/"
                numberOfb = float(numberOfgb) * 1073741824
                threading.Thread(target=dupe, args=[numberOfb, fldr]).start()
                for child in root.winfo_children():
                    child.configure(state='disable')
                loading(numberOfb, fldr)


    btn = tk.Button(master=root, width=20, height=2, text="Generate", command=go)
    btn.grid(row=3, column=0, columnspan=2, sticky="nsew")

    root.mainloop()

def loading(genSize, fldr):
    root1 = tk.Tk()
    root1.title("Glizzy Machine!")
    root1.resizable(False, False)

    label = tk.Label(master=root1, width=20, height=2, text="Progress:")
    label.pack()

    pb1 = Progressbar(root1, orient='horizontal', length=100, mode='determinate')
    pb1.pack(expand=True)

    def progress(genSize, fldr):
            while get_directory_size(fldr) < genSize:
                pb1['value'] = (get_directory_size(fldr) / genSize) * 100
            label.configure(text='Done!')

    btn = tk.Button(master=root1, width=20, height=2, text="Quit", command=quit)
    btn.pack()

    threading.Thread(target=progress, args=[genSize, fldr]).start()

    root1.mainloop()

main()