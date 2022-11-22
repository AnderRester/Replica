# from tkinter import *
import ctypes
from tkinter import Tk, Label


class WindowSetting:
    root = Tk()

    # def __init__(self):
    #     self.root = Tk()
    def say_it(self, event):
        print("My name is Jeff " + event.char)

    def controller(self, event):
        if(event.char == "w"):
            print("up")
        elif(event.char == "s"):
            print("down")
        elif(event.char == "a"):
            print("left")
        elif(event.char == "d"):
            print("right")
    def open_window(self):
        user32 = ctypes.windll.user32
        screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
        # print((screensize[0], "x", screensize[1]).replace(' ', ''))
        # test = str(screensize[0]) + "x" + str(screensize[1])
        # screensize_params = (screensize[0], "x", screensize[1]).replace(' ', '')
        # print(test)

        self.root.title("Тестирование Python")
        # root.geometry(test)
        self.root.attributes("-fullscreen", False)

        # controller
        self.root.bind("<Key>", self.controller)
        # self.root.bind("<Key>", self.say_it())
        # def move_aside:

        self.root.mainloop()


# Press the green button in the gutter to run the script.

if __name__ == '__main__':
    class_instance = WindowSetting()
    class_instance.open_window()

    # root = Tk()
    #
    #
    # def key_pressed(event):
    #     w = Label(root, text="KeyPressed:" + event.char)
    #     w.place(x=70, y=90)
    #     print("KeyPressed:" + event.char)
    #
    # root.bind("<Key>", key_pressed)
    #
    # root.mainloop()
