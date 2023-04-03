#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install qrcode')


# In[ ]:


import PySimpleGUI as sg
import qrcode


layout = [
    [sg.Text("Enter text to generate QR code:")],
    [sg.InputText(key="-INPUT-")],
    [sg.Button("Create"), sg.Button("Exit")],
    [sg.Image(key="-IMAGE-")]
]


window = sg.Window("QR Code Generator App", layout)


while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == "Exit":
        break
    if event == "Create":
        text = values["-INPUT-"]
        if text:
            qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
            qr.add_data(text)
            qr.make(fit=True)
            img = qr.make_image(fill_color="black", back_color="white")
            window["-IMAGE-"].update(data=img.tobytes())
        else:
            sg.popup("Please enter some text.", title="Error")


window.close()


# In[ ]:




