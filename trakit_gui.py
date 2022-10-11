import PySimpleGUI as sg
import threading
import user_extract

def long_operation_thread(ou, op, window):
    user_extract.get('https://vall-trk.aspgov.com/eTRAKiT_Admin/EtrakitUserList.aspx?lt=PUBLIC_REGISTERED', user_extract.driver_setup(), ou, op)
    window.write_event_value('-THREAD-', 'All Users Have Been Extracted !')

sg.theme("BlueMono")
layout = [[sg.Text('Trakit Username: ', size=(19, 1)), sg.InputText(key="TrakitUser")],
         [sg.Text('Trakit Password: ', size=(19, 1)), sg.InputText('', key='TrakitPassword', password_char='*')],
         [sg.Button("Extract")],
         [sg.StatusBar("", size=(20, 1), key='Status')]
         ]

window = sg.Window('eTRAKIT USER LIST', layout, size=(600,225))
prompt = window['Status'].update
input_key_list = [key for key, value in window.key_dict.items()
    if isinstance(value, sg.Input)]
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event=="Exit":
        break
    elif event == "Scrap":
        if all(map(str.strip, [values[key] for key in input_key_list])):
            prompt("Running Extract...")
            threading.Thread(target=long_operation_thread, args=(values["TrakitUser"], values["TrakitPassword"], window), daemon=True).start()
        else:
            prompt("Please Complete All Fields")
    elif event == "-THREAD-":
        prompt(values[event])