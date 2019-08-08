import vk_api
from tkinter import *

root = Tk()
root.title('VKashechka')
root.geometry('400x720')

canvas = Canvas(root, width=400, height=720, bg='#212121')

canvas.create_text(200, 50, text='VKASHECHKA', font='Arial 18', fill='#ebebeb')

canvas.create_text(200, 100, text='Логин', font='Arial 16', fill='#ebebeb')

login = Entry(canvas, font='Arial 14')
login.place(x=90, y=130)

canvas.create_text(200, 200, text='Пароль', font='Arial 16', fill='#ebebeb')

password = Entry(canvas, font='Arial 14', show='*')
password.place(x=90, y=230)


def gotIt(log, pas):
    vk_session = vk_api.VkApi(log, pas)

    try:
        vk_session.auth()
        vk = vk_session.get_api()

        li_friends = vk.friends.get()['items']
        f = open('list.txt', 'r')
        li = list(map(lambda el: int(el[0:-1]), f.readlines()[0:-1]))

        for id in li_friends:
            if id in li:
                vk.friends.delete(user_id=id)
        f.close()

    except:
        pass


make_but = Button(canvas, text='ВЫПОЛНИТЬ', font='Arial 18', bg='#de3aa4')
make_but.bind('<Button-1>', lambda event: gotIt(login.get(), password.get()))
make_but.place(x=115, y=300)

canvas.pack()

root.mainloop()
