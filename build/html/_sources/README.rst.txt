Галерея
==========================================
Галерея фото с возможностью переключения изображений

В коде введена переменная k определяющая номер текущего 
отображаемого изображения. По умолчанию показывает первую фотографию в папке. Предполагается, что все фото в формате .png

.. code::

    k = 0

Переключение изображения осуществляется через **Button**

.. code::

    button1 = Button(text='Предыдущая', font=20,width= 20,command=BACK, activebackground='green')
    button1.pack(side=LEFT)

    button2 = Button(text='Следующая', font=20,width= 20,command=NEXT, activebackground='green')
    button2.pack(side=RIGHT)


Изображение реализовано через **Label** со свойством *image*

.. code::

    img = PhotoImage(file=gallery[0])
    lbl_img =Label(image=img, width= 300, height=400)
    lbl_img.pack()

**nextImage()**

Выводит на экран следующее изображение и работает с **k**

Реализована проверка на наличие следующего изображения
.. code::

    def NEXT():
    k = gallery.index(img['file'])
    if k < limit - 1:
        k += 1
        img['file'] = gallery[k]
    else:
        k = 0
        img['file'] = gallery[k]

Когда пользователь долистает до последнего изображения- следующее нажатие клавиши отобразит первое изображение в папке.
Таким образом пользователь будет иметь возможность листать фото в любую сторону по кругу без ошибок.

Проверка на предыдущее изображение работает аналогичноб только проверяет на **k = limit - 1**
.. code::

   def BACK():
    k = gallery.index(img['file'])
    if k > 0:
        k -= 1
        img['file'] = gallery[k]
    else:
        k = limit - 1
        img['file'] = gallery[k]




Смена изображения происходит заменой значения в свойстве *image*








