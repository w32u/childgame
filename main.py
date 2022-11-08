from tkinter import *
import memorypuzzle, paint

class Menu(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)

        self.parent = parent
        self.setUI()
    
    def setUI(self):
        self.parent.title("Menu_ChildGame")  # Устанавливаем название окна
        self.pack(fill=BOTH, expand=1, side=TOP)  # Размещаем активные элементы на родительском окне
        
        red_btn = Button(self, text="КРАСКА", width=30,
                         command=lambda: paint.main()) # Создание кнопки:  Установка текста кнопки, задание ширины кнопки (10 символов), функция вызываемая при нажатии кнопки.
        red_btn.grid(row=0, column=1)

def main():
    root = Tk()
    root.geometry("850x500+300+300")
    app = Menu(root)
    root.mainloop()


if __name__ == '__main__':
    main()