from importlib.resources import contents
from optparse import Values
from tkinter import Listbox
from xml.sax.handler import feature_namespace_prefixes
import PySimpleGUI as sg
import os.path
import random
import string

password_list = [
    [
        sg.FolderBrowse(),
        sg.In(size=(25,1), enable_events=True, key = "-Pass-" )
    ],

    [
    sg.Listbox(
        values=[], enable_events=True, size = (40, 20), 
        key="-Pass List-")
    ],
]
show_text = [
        [sg.Text("Passwords: ", size=(40,1))],
        [sg.Multiline(size=(70,30), key = "-Text-")],
        [sg.Button("Password Generator")],
        [sg.Button("Save")]
]

layout = [
    [

    sg.Column(password_list),
    sg.VSeparator(),
    sg.Column(show_text)

    ]
]

window = sg.Window("Your passwords", layout)

while True:
    event, values = window.read()
    if event == "Exit" or event == sg.WIN_CLOSED:
        break
    if event == "-Pass-":
        folder = values["-Pass-"]
        try:
            file_list = os.listdir(folder)
        except:
            file_list = []

        fnames = [
            f
            for f in file_list
            if os.path.isfile(os.path.join(folder, f))
            and f.lower().endswith((".txt"))
        ]
        window["-Pass List-"].update(fnames)
    elif event == "-Pass List-":
            file_selection = values["-Pass List-"][0]
            with open(os.path.join(folder, file_selection)) as file:
                contents = file.read()
                window["-Text-"].update(contents)
    elif event == "Password Generator" and len(values["-Pass List-"]) > 0:
        with open(os.path.join(folder, file_selection), "w") as file:
            password = "".join([random.choice(string.ascii_letters + string.punctuation + string.digits) for _ in range(10)])
            file.write(password)
    elif event == "Save" and len(values["-Pass List-"]) > 0:
        with open(os.path.join(folder, file_selection), "w") as file:
            file.write(values["-Text-"])