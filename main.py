from tkinter import *
from PIL import Image,ImageTk
import json
import urllib.request

def image(filename,width,heigh):
    photo=Image.open(filename).resize((width,heigh))
    return ImageTk.PhotoImage(photo)

def delete():
    text4.delete('1.0', END)

def translate_to():
    text = text3.get()
    #调用有道软件进行翻译，请求结果返回给text
    text = urllib.request.urlopen(
        'https://translate.google.cn/translate_a/single?client=t&sl=de&tl=en&hl=en&dt=at&dt=bd&dt=ex&dt=ld&dt=md&dt=qca&dt=rw&dt=rm&dt=ss&dt=t&ie=UTF-8&oe=UTF-8&otf=1&ssel=3&tsel=0&kc=1&tk={0}&q={1}' + urllib.parse.quote(text))
    #解码json数据
    translator_text = json.loads(text.read())
    text4.insert(END, '原  文：  ')
    #返回str中'src'字符串
    text4.insert(END, translator_text['translateResult'][0][0]['src'])
    text4.insert(END, '\n翻  译：  ')
    #返回str中'tgt'字符串
    text4.insert(END, translator_text['translateResult'][0][0]['tgt'])
    text4.insert(END, '\n\n')
    text3.delete(0, END)

root=Tk()
root.geometry('800x400')
root.iconbitmap('pen.ico')
root.title('随心翻译')

canvas = Canvas(root, width=800, height=400)
image1 = image('translate_two.jpg', 800, 400)
canvas.create_image(400, 200, image=image1)
canvas.pack()

#第一个语言提示
label1 = Label(root, text="语言：", font='Arial 10 bold', fg='#696969', bg='#B0E0E6')
label1.place(relx=40/800, rely=40/400, relwidth=110/800, relheight=30/400)

label1_language = Label(root, text='中 文', font='Arial 15 bold', fg='#696969', bg='#B0E0E6')
label1_language.place(relx=40/800,rely=80/400,relwidth=110/800,relheight=80/400)

#第二个语言提示
label2=Label(root,text="翻译为：", font='Arial 10 bold',fg='#696969',bg='#B0E0E6')
label2.place(relx=40/800,rely=190/400,relwidth=110/800,relheight=30/400)

label2_language = Label(root, text='英 文', font='Arial 15 bold', fg='#696969', bg='#B0E0E6')
label2_language.place(relx=40/800,rely=230/400,relwidth=110/800,relheight=80/400)

#第三个语言提示
label3=Label(root,text="请输入你想翻译的文本",font='Arial 10 bold',fg='#696969',bg='#B0E0E6')
label3.place(relx=180/800,rely=60/400,relwidth=150/800,relheight=30/400)

#第三个文本框输入你想翻译的文本
text3 = Entry(root,font='Arial 12 bold',fg='#696969')
text3.place(relx=180/800,rely=100/400,relwidth=250/800,relheight=160/400)

#第一个按钮
button1=Button(root,text='翻译', command=translate_to,font='Arial 10 bold',fg='#696969',bg='#B0E0E6')
button1.place(relx=450/800,rely=120/400,relwidth=50/800,relheight=50/400)

#第二个按钮
button1=Button(root,text='清空', command=delete,font='Arial 10 bold',fg='#696969',bg='#B0E0E6')
button1.place(relx=450/800,rely=190/400,relwidth=50/800,relheight=50/400)

#第四个文本框翻译结果
text4 = Text(root,font='Arial 12 bold',fg='#696969')
text4.place(relx=520/800,rely=100/400,relwidth=250/800,relheight=160/400)


root.mainloop()