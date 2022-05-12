from tkinter import *
from tkinter import ttk
import googletrans

class Main:
    def __init__(self):
        self.root = Tk()
        self.root.title("Translator")
        self.root.geometry("1920x1080")
        self.root.config(bg = 'white')


        self._control = True
        self.root.bind("<Return>", lambda x: Main.translateFunction(self))
        self.root.bind("<Shift-C>", lambda x: Main.changeLanguages(self))
        self.root.bind("<Shift-D>", lambda x: Main.themeChange(self))
        #Canvas Area

        self.blueCanvas = Canvas(self.root, bg = 'lightblue', width = 3000, height = 100)
        self.blueCanvas.place(x = 0, y = 0)

        self.canvasExitButton = ttk.Button(self.blueCanvas, text = "Quit", command =lambda: Main.quitFunction(self))
        self.canvasExitButton.place(x = 1200, y = 40)

        self.canvasClearButton = Button(self.blueCanvas, text = "Clear", command =lambda: Main.clearFunction(self))
        self.canvasClearButton.place(x=1050, y = 40)

        self.canvasDarkModeButton = ttk.Button(self.blueCanvas, text = "Dark",command=lambda:Main.themeChange(self))
        self.canvasDarkModeButton.place(x=900, y= 40)
        
        ####

        self.photoChange = PhotoImage(file = "change.png", width=80, height=55)

        self.list1 = ["Turkish", "English", "German", "French", "Italian", "Arabic", "Russian", "Spanish", "Chinese", "Kurmancca", "Finnish"]
        self.list2 = ["tr", "en", "de", "fr", "it", "ar", "ru", "es", "zh-cn", "ku", "fi"]

        self.textArea1 = Text(self.root, borderwidth = 5)
        self.textArea1.place(x=260,y=300)
        self.textArea1.insert(INSERT, "Cevirmek istediginiz metni giriniz.")

        self.textArea2 = Text(self.root, state = DISABLED, borderwidth = 5)
        self.textArea2.place(x=905,y=300)

        self.comboBox1 = ttk.Combobox(self.root, values = self.list1)
        self.comboBox1.place(x=500, y=250)
        self.comboBox1.set(self.list1[0])
        self.comboBox2 = ttk.Combobox(self.root, values = self.list1)
        self.comboBox2.place(x=1150,y=250)
        self.comboBox2.set(self.list1[1])

        self.translateButton = Button(self.root, text = "Translate", fg = 'black', bg = 'white',command = lambda: Main.translateFunction(self))
        self.translateButton.place(x=865,y=730)
        self.changeButton = Button(self.root,image = self.photoChange, fg = 'black', bg = 'white',command = lambda: Main.changeLanguages(self))
        self.changeButton.place(x=860, y=225)

        self.root.mainloop()
    
    def translateFunction(self):

        self.textArea2.config(state = NORMAL)
        self.textArea2.delete(1.0, 'end-1c')
        self.translator = googletrans.Translator()
        self.sentence = self.textArea1.get(1.0,'end-1c')
        self.result = self.translator.translate(self.sentence, dest = self.list2[self.comboBox2.current()], src = self.list2[self.comboBox1.current()]).text
        self.textArea2.insert(INSERT, self.result)
        self.textArea2.config(state = DISABLED)

    def changeLanguages(self):
        
        self.textArea2.config(state = NORMAL)
        self.current2 = self.comboBox2.current()
        self.comboBox2.set(self.list1[self.comboBox1.current()])
        self.comboBox1.set(self.list1[self.current2])
        
        self.textArea2Get = self.textArea1.get(1.0, 'end-1c')
        self.textArea1Get = self.textArea2.get(1.0, 'end-1c')
        self.textArea1.delete(1.0, 'end-1c')
        self.textArea2.delete(1.0, 'end-1c')
        self.textArea1.insert(INSERT, self.textArea1Get)
        self.textArea2.insert(INSERT, self.textArea2Get)

        self.textArea2.config(state = DISABLED)
    
    def quitFunction(self):
        self.root.destroy()

    def clearFunction(self):
        self.textArea2.config(state = NORMAL)
        self.textArea1.delete(1.0, 'end-1c')
        self.textArea2.delete(1.0, 'end-1c')
        self.textArea2.config(state = DISABLED)

    def themeChange(self):
        if self._control == True:
            self.root.config(bg = "black")
            self.textArea1.config(bg = 'black', fg = 'white')
            self.textArea2.config(bg = 'black', fg = 'white')
            self.canvasDarkModeButton.config(text = 'Light')
            self.style= ttk.Style()
            self.style.theme_use('clam')
            self.style.configure("TCombobox", fieldbackground= "black", background= "black", foreground = 'white')
            self.translateButton.config(fg = 'white', bg='black')
            self.changeButton.config(fg = 'white', bg = 'black')
            self.blueCanvas.config(bg = 'darkblue')

            self._control = False
        else:
            self.root.config(bg = "white")
            self.textArea1.config(bg = 'white', fg = 'black')
            self.textArea2.config(bg = 'white', fg = 'black')
            self.canvasDarkModeButton.config(text = 'Dark')
            self.translateButton.config(fg = 'black', bg='white')
            self.changeButton.config(fg = 'black', bg = 'white')
            self.blueCanvas.config(bg = 'lightblue')
            self.style.configure("TCombobox", fieldbackground= "white", background= "white", foreground = 'black')
            self._control = True

Main()