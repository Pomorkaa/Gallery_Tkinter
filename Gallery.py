#Создать приложение “Галерея”. На экране разместить две кнопки, которые перелистывают изображения.
# В центре окна приложения разместить объект, отображающий фотографии. Добавить минимум 5 фотографий.


from tkinter import *
import os


root = Tk()
root.title('Галерея')
root.geometry('400x500')
root.resizable(1, 1)

print(os.getcwd())
path = os.chdir("photo")  #поменяли на нужную папку
path = os.getcwd()       #проверили что то что надо
gallery = os.listdir(path)       #создали список с файлами
print(gallery)              #забрали список файлов
stroka = str(gallery)             #перевели в строчку
limit = stroka.count('png')       # посчитали количество файлов png

k = 0

def NEXT():
    k = gallery.index(img['file'])
    if k < limit - 1:
        k += 1
        img['file'] = gallery[k]
    else:
        k = 0
        img['file'] = gallery[k]

def BACK():
    k = gallery.index(img['file'])
    if k > 0:
        k -= 1
        img['file'] = gallery[k]
    else:
        k = limit - 1
        img['file'] = gallery[k]



names = Label(text='Гелерея',font=20)
names.pack()

img = PhotoImage(file=gallery[0])
lbl_img =Label(image=img, width= 300, height=400)
lbl_img.pack()

button1 = Button(text='Предыдущая', font=20,width= 20,command=BACK, activebackground='green')
button1.pack(side=LEFT)

button2 = Button(text='Следующая', font=20,width= 20,command=NEXT, activebackground='green')
button2.pack(side=RIGHT)

root.mainloop()

