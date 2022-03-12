#!/usr/bin/python

import tkinter as tk
import tkinter.filedialog
from pathlib import Path

# tkinter GUI section
top = tk.Tk()

frm_input = tk.Frame()
frm_dir = tk.Frame()

frm_input.pack()
frm_dir.pack()

lbl_entry = tk.Label(master = frm_input, text = "insert spotify playlist link", pady = 10, width = 80)
lbl_entry.pack()

ent_link = tk.Entry(master = frm_input, width = 90, bd = 3)
ent_link.pack(side = tk.LEFT)

btn_submit = tk.Button(master = frm_input, text = "Submit")
btn_submit.pack(side = tk.LEFT)

# path for image for dir button
files_dir = Path("files")
file_to_open = files_dir / "folder.png"
img_dir = tk.PhotoImage(file = file_to_open)

btn_dir = tk.Button(master = frm_dir, image = img_dir)
lbl_dir = tk.Label(master = frm_dir, text = "select download destination", pady = 10)
lbl_dir.pack(side = tk.LEFT)
btn_dir.pack()

top.mainloop()
