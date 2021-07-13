try:
    from tkinter import *
    from PIL import Image, ImageTk
    import googletrans
    from googletrans import Translator
    import pyttsx3
    window = Tk()
    window.title('Google Translator')
    window.geometry('500x630')
    window.minsize(width = 500, height = 630)

    bot = pyttsx3.init()
    voices = bot.getProperty('voices')
    bot.setProperty("voice", voices[1].id)
    window.resizable(height = False, width = False)
    window.iconbitmap('logo.ico')

    def docenglish():
        INPUT = o1.get(1.0, END)
        t = Translator()
        a = t.translate(INPUT,src="vi",dest="en")
        b = a.text
        bot.say(b)
        bot.runAndWait()

    def clear():
        o1.delete(1.0, END)
        o2.delete(1.0, END)


    def tran():
        INPUT = o1.get(1.0, END)
        t = Translator()
        a = t.translate(INPUT,src="vi",dest="en")
        b = a.text
        o2.insert(END, b)
    a = Image.open('background.png')  
    anh = ImageTk.PhotoImage(a)
    bg = Label(window, image=anh)
    bg.place(x=0, y=0)

    chu = Label(window, text='Google Dịch', fg='White', bd=0, bg = '#00132C')
    chu.config(font=('Transformers Movie.ttf', 30))
    chu.pack(pady=10)

    o1 = Text(window, width=28, height=8, font=('ROBOTO', 16))
    o1.pack(pady=20)
    dich = Button(window, text="Dịch", font=(
        ('Arial'), 10, 'bold'), bg='#303030', fg="#FFFFFF", command = tran)
    dich.place(x=150, y=311)
    xoa = Button(window, text="Xóa", font=(
        ('Arial'), 10, 'bold'), bg='#303030', fg="#FFFFFF", command = clear)
    xoa.place(x=304, y=311)

    doctv = Button(window, text = 'Đọc TV', font=(
        ('Arial'), 10, 'bold'), bg='#303030', fg="#FFFFFF")
    doctv.place(x = 78, y = 311 )

    docta = Button(window, text = 'Đọc TA', font=(
        ('Arial'), 10, 'bold'), bg='#303030', fg="#FFFFFF", command = docenglish )
    docta.place(x = 350, y = 311)
    o2 = Text(window, width=28, height=8, font=('ROBOTO', 16))
    o2.pack(pady=50)
    code = Label(window, text="Code by Huypc", fg='#FFFFFF', bg = '#002E4D')
    code.pack(pady=10)

    window.mainloop()
except Exception as bug:
    print(bug)