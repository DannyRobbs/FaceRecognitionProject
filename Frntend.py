from tkinter import *
from tkinter import ttk
import AttendanceProject


root = Tk()

content = ttk.Frame(root, padding=(3, 3, 3, 3))
frame = ttk.Frame(content, borderwidth=1, relief="ridge", width=560, height=480)
frameTwo = ttk.Frame(content, borderwidth=1, relief="ridge", width=260, height=480)
frameThree = ttk.Frame(content, borderwidth=0)
users = Listbox(frameTwo)



def start_recognition():
    # TODO: Add the image recognition video opener here
    # Also, return the user that was added so we can show
    assume_user_from_image_recog = AttendanceProject.mainfunction()
    global users
    users.insert(END, assume_user_from_image_recog)


ok = ttk.Button(frameThree, text="Start Video", command=start_recognition)
cancel = ttk.Button(frameThree, text="Cancel", command=root.destroy)


title = ttk.Label(frame, text='Click the "start video" below to begin taking attendance')

content.grid(column=0, row=0, sticky=(N, S, E, W))
frame.grid(column=0, row=0, columnspan=2, rowspan=2, sticky=(N, S, E, W))
frameTwo.grid(column=2, row=0, rowspan=3, sticky=(N, S, E, W))
frameThree.grid(column=0, row=3, sticky=(N, S, E, W))
title.place(x=280, y=240, anchor='center')
users.pack(side=LEFT, fill=BOTH)
ok.grid(column=0, row=0)
cancel.grid(column=1, row=0)


root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
content.columnconfigure(0, weight=3)
content.columnconfigure(1, weight=3)
content.columnconfigure(2, weight=3)
content.columnconfigure(3, weight=1)
content.columnconfigure(4, weight=1)
content.rowconfigure(1, weight=1)

root.mainloop()