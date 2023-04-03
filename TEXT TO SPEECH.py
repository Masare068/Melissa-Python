#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import PySimpleGUI as sg
import pyttsx3

engine = pyttsx3.init()

layout = [[sg.Text("Enter the text you want to speak:")],
          [sg.Input(key="-INPUT-")],
          [sg.Radio("Male voice", group_id="VOICE", key="-MALE-", default=True), 
           sg.Radio("Female voice", group_id="VOICE", key="-FEMALE-")],
          [sg.Button("Speak"), sg.Button("Cancel")]]


window = sg.Window("Text-to-Speech App", layout)

def speak(text, voice_type):
    if voice_type == "male":
        engine.setProperty("voice", "english_male")
    else:
        engine.setProperty("voice", "english_female")

    engine.say(text)
    engine.runAndWait()

while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED or event == "Cancel":
        break

    if event == "Speak":
        text = values["-INPUT-"]
        if values["-MALE-"]:
            speak(text, "male")
        elif values["-FEMALE-"]:
            speak(text, "female")

window.close()


# In[ ]:




