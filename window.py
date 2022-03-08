from tkinter import *


class Example(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent, background="white")
        self.parent = parent
        self.initUI()

    def initUI(self):
        self.parent.title("Simple")

        self.pack(fill=BOTH, expand=1)

        quitButton = Button(self, text='Выход', command=self.quit)
        quitButton.place(x=50, y=50)


def main():
    root = Tk()
    root.geometry("250x150+300+300")
    app = Example(root)
    root.mainloop()


main()