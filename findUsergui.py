import PySimpleGUI as sg
import threading
import findUser

def long_operation_thread(usr, pwd, user, type, window):
    findUser.login('https://vall-trk.aspgov.com/eTRAKiT_Admin/EtrakitUserList.aspx?lt=PUBLIC_REGISTERED', findUser.driver_setup(), usr, pwd, user, type)
    window.write_event_value('-THREAD-', 'User Has Been Found!')

sg.theme("BlueMono")
layout = [[sg.Text('eTrakit Username: ', size=(19, 1)), sg.InputText(key="eTrakitUser")],
         [sg.Text('eTrakit Password: ', size=(19, 1)), sg.InputText('', key='eTrakitPassword', password_char='*')],
         [sg.Text('Username Lookup: ', size=(19, 1)), sg.InputText(key="user")],
         [sg.Combo(['PUBLIC','CONTRACTOR'], size=(20, 1),readonly=True, default_value='PUBLIC',key='type')],
         [sg.Button("FIND")],
         [sg.StatusBar("", size=(20, 1), key='Status')]
         ]

window = sg.Window('eTrakitUserFinder', layout, size=(600,175))
prompt = window['Status'].update
input_key_list = [key for key, value in window.key_dict.items()
    if isinstance(value, sg.Input)]
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event=="Exit":
        break
    elif event == "FIND":
        if all(map(str.strip, [values[key] for key in input_key_list])):
            prompt("Running Extract...")
            threading.Thread(target=long_operation_thread, args=(values["eTrakitUser"], values["eTrakitPassword"], values["user"], values["type"], window), daemon=True).start()
        else:
            prompt("Please Complete All Fields")
    elif event == "-THREAD-":
        prompt(values[event])