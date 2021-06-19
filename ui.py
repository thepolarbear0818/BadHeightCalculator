import PySimpleGUI as sg



# All the stuff inside your window.
layout = [  [sg.Text('Enter Your Height (cm) In the text box, then press calculate')],
            [sg.Button('Calculate')],
            [sg.Multiline(size=(30, 5), key='textbox')]]  # identify the multiline via key option



# Create the Window
window = sg.Window('Height Calculator', layout).Finalize()
#window.Maximize()
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    print('You height(cm)is:')
    print(values['textbox'])  # get the content of multiline via its unique key

window.close()
