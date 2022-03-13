#!/usr/bin/python

import tkinter as tk
import tkinter.filedialog
from pathlib import Path


# tkinter GUI section
top = tk.Tk()

frm_input = tk.Frame()
frm_dir = tk.Frame()
frm_output = tk.Frame()

frm_input.pack()
frm_dir.pack()

lbl_entry = tk.Label(master = frm_input, text = "INSERT SPOTIFY PLAYLIST", pady = 10, width = 80)
lbl_entry.pack()

ent_link = tk.Entry(master = frm_input, width = 90, bd = 3)
ent_link.pack(side = tk.LEFT)

lbl_out = tk.Label(master = frm_output, width = 109, bg = 'red', fg = 'white')
lbl_out.pack()

def submit():
    frm_output.pack_forget()
    input = ent_link.get()
    if len(input) == 0:
         lbl_out['text'] = "INVALID LINK"
         frm_output.pack()

def clear():
    ent_link.delete(0, 'end')

btn_submit = tk.Button(master = frm_input, text = "SUBMIT", command = submit)
btn_submit.pack(side = tk.LEFT)
btn_clear = tk.Button(master = frm_input, text = "CLEAR", command = clear)
btn_clear.pack(side = tk.LEFT)

# path for image for dir button
files_dir = Path('files')
file_to_open = files_dir / 'folder.png'
img_dir = tk.PhotoImage(file = file_to_open)

def selectdir():
    path = tk.filedialog.askdirectory(title = 'SELECT FOLDER')

btn_dir = tk.Button(master = frm_dir, image = img_dir, command = selectdir)
lbl_dir = tk.Label(master = frm_dir, text = "SELECT DOWNLOAD LOCATION", pady = 10)
lbl_dir.pack(side = tk.LEFT)
btn_dir.pack()

top.mainloop()

