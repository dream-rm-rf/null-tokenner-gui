# # from tkinter import scrolledtext
# def display_full_name():
#     messagebox.showinfo("null-tokenner v2.0 by dream", token.get())  
# lbl = Label(window, text="Привет пострижися")  
# lbl.grid(column=1, row=0)
# btn1 = Button(window,width=20, text='Сменить статус ВК', command=status_change)41574433764164cc88a3b70fb3f4e7e60ef739e3680aa863a1b02b06c3b2d464f770675aa67077e0d2f11  
# btn1.grid(column=1, row=2)</> <a href="st-guru.pl">*тык*</a>
# logging.basicConfig(filename='chats_ids.log', level=logging.INFO)
from tkinter import *
from tkinter.ttk import Radiobutton  
from tkinter import messagebox
import vk_api  
import pytz
import urllib
from urllib import request
import requests
import vk
import webbrowser
import random
# import pyautogui
# a = int(input("Кол-во нажатий: ") )
# num = 0
                   
# while num <= a:
#     pyautogui.keyDown('Q')
#     print(num)
#     num += 1
# import os
# from selenium import webdriver
# import requests
# cert =('cert','key')
# password = "qwerty123"
# auths ={'passwordField':password}
# URL = "htтps://tender.sk.kz/OA_HTML/AppsLogin"
# s = requests.Session()
# r = s.get(URL, cert=cert, headers=headers, verify=False)
# auth_page = r.url
# r = s.post(auth_page, headers=headers, data=data)

def howto():
    webbrowser.open('http://st-guru.pl/changelog/main_py.html', new=2)
    # webbrowser.open('javascript:alert(1)', new=2) 

def clicked():  
    fn = selected.get()
    if fn == 1:
        status_change()
    elif fn == 2:
        ava_change()
    elif fn == 3:
        ban()
    elif fn == 4:
        unban()
    elif fn == 5:
        post()
    elif fn == 6:
        friend_add()
    elif fn == 7:
        friend_remove()
    elif fn == 8:
        msg_send()
    else: 
        messagebox.showinfo("null-tokenner v2.0.1 by dream", "Вы не выбрали команду!")

def status_change():
    try:
        vk = vk_api.VkApi(token=token.get())
        vk.method("status.set", {"text": text.get()})
    except:
        messagebox.showinfo("null-tokenner v2.0.1 by dream", 'Вы ввели неправильный токен/айди, проверьте правильность ввода!')

def friend_add():
    try:
        vk = vk_api.VkApi(token=token.get())
        vk.method("friends.add", {"user_id": id.get()})
    except:
        messagebox.showinfo("null-tokenner v2.0.1 by dream", 'Вы ввели неправильный токен/айди, проверьте правильность ввода!')

def friend_remove():
    try:
        vk = vk_api.VkApi(token=token.get())
        vk.method("friends.delete", {"user_id": id.get()})
    except:
        messagebox.showinfo("null-tokenner v2.0.1 by dream", 'Вы ввели неправильный токен/айди, проверьте правильность ввода!')

def ban():
    try: 
        session = vk_api.VkApi(token=token.get())
        vk = session.get_api()    
        vk.account.banUser(user_id = id.get())
    except:
        messagebox.showinfo("null-tokenner v2.0.1 by dream", 'Вы ввели неправильный токен/айди, проверьте правильность ввода!')

def unban():
    try: 
        session = vk_api.VkApi(token=token.get())
        vk = session.get_api()    
        vk.account.unbanUser(user_id = id.get())
    except:
        messagebox.showinfo("null-tokenner v2.0.1 by dream", 'Вы ввели неправильный токен/айди, проверьте правильность ввода!')

def msg_send():
    try: 
        vk = vk_api.VkApi(token=token.get())
        vk.method("messages.send", {"peer_id": peer.get(), "message": text.get(), "random_id": random.randint(1, 2147483647)})
    except:
        messagebox.showinfo("null-tokenner v2.0.1 by dream", 'Вы ввели неправильный токен/айди, проверьте правильность ввода!')

def ava_change():
    try:
        vk = vk_api.VkApi(token=token.get()) 
        upload = vk_api.VkUpload(vk)
        photo = upload.photo_profile('213.jpg')
    except:
        messagebox.showinfo("null-tokenner v2.0.1 by dream", 'Вы ввели неправильный токен/айди, проверьте правильность ввода!')

def post():
    try:
        vk = vk_api.VkApi(token=token.get())
        vk.method("wall.post", {"message": text.get()})
    except:
        messagebox.showinfo("null-tokenner v2.0.1 by dream", 'Вы ввели неправильный токен/айди, проверьте правильность ввода!')

app = Tk()

app.geometry('450x400')
app.title("null-tokenner v2.0.1 by dream")
app.resizable(False, False)

messagebox.showinfo("null-tokenner v2.0 by dream", "Выкладывать данный софт на форумах/ группах вк/ прочих местах имеет право только vk.com/geramyrzick! На все остальные темы будут отправлены жалобы ")
token = StringVar()
token_label = Label(text="Введите токен:")
token_label.grid(row=0, column=0, sticky="w")
token_entry = Entry(textvariable=token)
token_entry.grid(row=0,column=1, padx=5, pady=5)

text = StringVar()
text_label = Label(text="Введите текст:")
text_label.grid(row=1, column=0, sticky="w")
text_entry = Entry(textvariable=text)
text_entry.grid(row=1,column=1, padx=5, pady=5)

id = StringVar()
id_label = Label(text="Введите цифровой айди нужного пользователя:")
id_label.grid(row=2, column=0, sticky="w")
id_entry = Entry(textvariable=id)
id_entry.grid(row=2,column=1, padx=5, pady=5)

peer = StringVar()
peer_label = Label(text="Введите айди нужного диалога/беседы:")
peer_label.grid(row=3, column=0, sticky="w")
peer_entry = Entry(textvariable=peer)
peer_entry.grid(row=3,column=1, padx=5, pady=5)

selected = IntVar()  
rad1 = Radiobutton(app,width=22, text='Сменить статус', value=1, variable=selected)  
rad2 = Radiobutton(app,width=22, text='Сменить аватарку', value=2, variable=selected)  
rad3 = Radiobutton(app,width=22, text='Отправить в чс', value=3, variable=selected)
rad4 = Radiobutton(app,width=22, text='Убрать в чс', value=4, variable=selected)  
rad5 = Radiobutton(app,width=22, text='Создать пост', value=5, variable=selected)  
rad6 = Radiobutton(app,width=22, text='Добавить в друзья', value=6,variable=selected)
rad7 = Radiobutton(app,width=22, text='Убрать из друзей', value=7,variable=selected)  
rad8 = Radiobutton(app,width=22, text='Отправить сообщение', value=8, variable=selected)  

rad1.grid(column=0, row=11)  
rad2.grid(column=0, row=12)  
rad3.grid(column=0, row=13)
rad4.grid(column=0, row=14)  
rad5.grid(column=0, row=15)  
rad6.grid(column=0, row=16)
rad7.grid(column=0, row=17)  
rad8.grid(column=0, row=18)  

button = Button(text="Выполнить", command=clicked)
button.grid(row=4,column=1)

button = Button(text="Как пользоваться?", command=howto)
button.grid(row=4,column=0)


app.mainloop()



    # print_blue('9.Отправить вертеплюшку')
    # print_blue("10.Пропарсить беседы и вывести их айди ")
    # print_red("11.Пропарсить все диалоги, не работает")  #В разработке
    