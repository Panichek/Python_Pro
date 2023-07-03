'''
1. Створити графічну програму з 8 кнопками
при натискані на кнопку зміни кольору має змінитись колір всіх кнопки на жовтий
'''
from tkinter import *

root = Tk()


class Screen:
    def __init__(self, buttons):
        self.buttons = buttons

        for button in self.buttons:
            button.pack()

    def change_color(self, color):
        for button in self.buttons:
            button.config(bg=color)


screen1 = Screen([Button(root, text="1", command=lambda: print("1")),
                  Button(root, text="2", command=lambda: print("2")),
                  Button(root, text="3", command=lambda: print("3")),
                  Button(root, text="4", command=lambda: print("4")),
                  Button(root, text="5", command=lambda: print("5")),
                  Button(root, text="6", command=lambda: print("6")),
                  Button(root, text="7", command=lambda: print("7")),
                  Button(root, text="8", command=lambda: print("8"))])
color_button = Button(root, text="Зміна коліру", command=lambda: screen1.change_color("yellow")).pack()
root.mainloop()
