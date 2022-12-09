from tkinter import *
from tkinter import ttk, colorchooser
from PIL import ImageTk, Image

class main:
    def __init__(self,master):
        self.master = master
        self.color_fg = 'black'
        self.color_bg = 'white'
        self.old_x = None
        self.old_y = None
        self.penwidth = 5
        self.screen_width = self.master.winfo_screenwidth()
        self.screen_height = self.master.winfo_screenheight()
        self.drawWidgets()
        self.c.bind('<B1-Motion>',self.paint)#drwaing the line 
        self.c.bind('<ButtonRelease-1>',self.reset)

    def paint(self,e):
        if self.old_x and self.old_y:
            self.c.create_line(self.old_x,self.old_y,e.x,e.y,width=self.penwidth,fill=self.color_fg,capstyle=ROUND,smooth=True)

        self.old_x = e.x
        self.old_y = e.y

    def reset(self,e):    #reseting or cleaning the canvas 
        self.old_x = None
        self.old_y = None      

    def changeW(self,e): #change Width of pen through slider
        self.penwidth = e
           

    def clear(self):
        self.c.delete(ALL)

    def change_fg(self):  #changing the pen color
        self.color_fg=colorchooser.askcolor(color=self.color_fg)[1]

    def change_bg(self):  #changing the background color canvas
        self.color_bg=colorchooser.askcolor(color=self.color_bg)[1]
        self.c['bg'] = self.color_bg
        
    def load_image(self, imagePath):
        self.image = Image.open(imagePath)
        self.photo = ImageTk.PhotoImage(self.image)
        
        self.pw, self.ph = self.photo.width(), self.photo.height()
        '''
        if self.pw > self.c.winfo_width():
            self.kw = round(self.pw // self.c.winfo_width())
            self.pw = round(self.pw / self.kw)
        
        if self.ph > self.c.winfo_height():
            self.kh = round(self.ph / self.c.winfo_height())
            self.ph = round(self.ph / self.kh)
        '''
        self.ph_resized = int(self.c.winfo_width() * self.ph / self.pw)
        self.pw_resized = int(self.c.winfo_height() * self.pw / self.ph)
        
        
        self.image_resized = self.image.resize((self.pw_resized, self.ph_resized),Image.Resampling.LANCZOS)
        self.photo_resized = ImageTk.PhotoImage(self.image_resized)
        
        
        self.c.create_image(self.c.winfo_width()/2,self.c.winfo_height()/2,image=self.photo_resized)
        
    def load_image1(self):
        self.load_image('res/1.jpg')
    
    def load_image2(self):
        self.load_image('res/2.jpg')
    
    def load_image3(self):
        self.load_image('res/3.jpg')
    
    def load_image4(self):
        self.load_image('res/4.jpg')
    
    def load_image5(self):
        self.load_image('res/5.jpg')

    def drawWidgets(self):
        self.controls = Frame(self.master,padx = 5,pady = 5)
        Label(self.controls, text='Размер кисти:',font=('arial 18')).grid(row=0,column=0)
        self.slider = ttk.Scale(self.controls,from_= 5, to = 100,command=self.changeW,orient=VERTICAL)
        self.slider.set(self.penwidth)
        self.slider.grid(row=0,column=1,ipadx=30)
        self.controls.pack(side=LEFT)
        
        self.c = Canvas(self.master,width=self.screen_width/1.5,height=self.screen_height/1.5,bg=self.color_bg,)
        self.c.pack(fill=BOTH,expand=True)
        
        

        menu = Menu(self.master)
        self.master.config(menu=menu)
        filemenu = Menu(menu)
        colormenu = Menu(menu)
        menu.add_cascade(label='Картинка', menu=filemenu)
        filemenu.add_command(label='Картинка 1',command=self.load_image1)
        filemenu.add_command(label='Картинка 2',command=self.load_image2)
        filemenu.add_command(label='Картинка 3',command=self.load_image3)
        filemenu.add_command(label='Картинка 4',command=self.load_image4)
        filemenu.add_command(label='Картинка 5',command=self.load_image5)
        menu.add_cascade(label='Цвета',menu=colormenu)
        colormenu.add_command(label='Цвет кисти',command=self.change_fg)
        colormenu.add_command(label='Цвет фона',command=self.change_bg)
        optionmenu = Menu(menu)
        menu.add_cascade(label='Опции',menu=optionmenu)
        optionmenu.add_command(label='Очистить лист',command=self.clear)
        optionmenu.add_command(label='Выйти',command=self.master.destroy)

    













    

