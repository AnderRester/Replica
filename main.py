# from tkinter import *
import ctypes
from tkinter import Tk, Label

# class Window_settings:
#     def open_window():
#         user32 = ctypes.windll.user32
#         screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
#         # print((screensize[0], "x", screensize[1]).replace(' ', ''))
#         # test = str(screensize[0]) + "x" + str(screensize[1])
#         # screensize_params = (screensize[0], "x", screensize[1]).replace(' ', '')
#         # print(test)
#         root = Tk()
#         root.title("Тестирование Python")
#         # root.geometry(test)
#         root.attributes("-fullscreen", False)
#
#         # controlls
#         def controlls_switch():
#             if(root.bind())
#             return print("My name is Jeff")
#
#         root.bind("<Key>", say_it)
#         # def move_aside:
#
#         root.mainloop()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    root = Tk()


    def key_pressed(event):
        w = Label(root, text="KeyPressed:" + event.char)
        w.place(x=70, y=90)
        print("KeyPressed:" + event.char)

    root.bind("<Key>", key_pressed)

    root.mainloop()
