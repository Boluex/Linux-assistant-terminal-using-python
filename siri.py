import wifimangement_linux as wifi
from whatsapp_bot import whatsapp_bot

# /usr/bin/gnome-calculator
# /usr/bin/gnome-calendar
# google-chrome
# gnome-text-editor
# gnome-www-browser
# gnome-todo 
# gnome-control-center
# gnome-system-monitor
# ssh user@host 'shutdown now'
# reboot
import subprocess
import os
import vlc
v=os.listdir('/home')
c=v[0]
home_path=f'/home/{c}'
check_dir=os.listdir(f'/home/{c}/Music')
# if 'Theophilus Sunday Daily Search My Heart.mp3' in check_dir:
#     print('yes')
# else:
#     print('no')
# print(check_dir)
# p=vlc.MediaPlayer()
# p.pause()'
# p.play())
# os.system('gnome-calendar','gnome-calculator','google-chrome','gnome-text-editor','gnome-www-browser','gnome-todo ')  
# os.system('rfkill unblock bluetooth')  turn on
# os.system('rfkill block bluetooth')  turn off
# subprocess.Popen('')

# def linux_assistant():
#     list_opt=['chrome','todo','calendar','calculator','editor','browser']
#     list_opt_2=['gnome-calendar','']
#     print('hi deji,I am your personal linux assistant...How may i help you today?')
    # enter_val=input('Your search:').lower()
    # split_text=enter_val.split(' ')
#     # print(split_text[1])
#     d=f'gnome-{split_text[1]}'
#     if d in list_opt_2:
#         print('yes')
#     elif 'settings' in split_text[1]:
#         os.system('gnome-control-center')
#     elif 'stats' in split_text[1]:
#         os.system('gnome-system-monitor')
#     elif 'editor' in  split_text[1]:
#         os.system('gnome-text-editor')
#     elif 'browser' in  split_text[1]:
#         os.system('gnome-www-browser')
    

# linux_assistant()

data_commands={
    'calendar':'gnome-calendar',
    'calculator':'gnome-calculator',
    'chrome':'google-chrome',
    'editor':'gnome-text-editor',
    'browser':'gnome-www-browser',
    'vscode':'code',
    'music':'rhythmbox',
    'files':'nautilus',
    'settings':'gnome-control-center',
    'stats':'gnome-system-monitor',
}

settings_commands={
    'on bluetooth':'rfkill unblock bluetooth',
    'off bluetooth':'rfkill block bluetooth',
    # 'on wifi':wifi.on(),
    # 'off wifi':wifi.off(),
    
}
def linux_assistant():
    print('hi deji,I am your personal linux assistant...How may i help you today?')
    print('To open apps just type open and your desired app name...e.g open editor')
    enter_val=input('Your search:').lower()
    split_text=enter_val.split(' ')
    # try:
    if 'open' in enter_val:
        while True:
            try:
                get_data_command=data_commands.get(split_text[1])
                #   print(get_data_command)
                v=os.system(get_data_command)
                enter_val=input('Your search:').lower()
                split_text=enter_val.split(' ')
                os.close(v)
            except OSError:
                print('App not found')
            if 'bye' in split_text:
                break
        print('Bye Oladeji')
                
    elif 'search' in enter_val:
            c=whatsapp_bot(enter_val)
            print(c)
    elif 'on bluetooth'  in enter_val:
         os.system(settings_commands.get(enter_val))
    elif 'off bluetooth'  in enter_val:
         os.system(settings_commands.get(enter_val))
    elif 'on wifi'  in enter_val:
        #  settings_commands.get(enter_val)
        wifi.on()
    elif 'off wifi'  in enter_val:
        #  settings_commands.get(enter_val)
        wifi.off()
        
    # except:
    #      print('Oops you are not connected to the internet')

linux_assistant()
# wifi.on()