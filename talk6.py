import requests
import tkinter
from tkinter import messagebox
kari = ''
mode = 0
d = ''
list = []
# mode = 0はo 1はx
counting = 2.0
c = 1


def speak_bouyomi(text='ゆっくり簡易化ツールが起動しました。バージョン5', voice=9, volume=-1, speed=-1, tone=-1):
    res = requests.get(
        'http://localhost:50080/Talk',
        params={
            'text': text,
            'voice': 1,
            'volume': volume,
            'speed': speed,
            'tone': tone})
    return res.status_code

# 処理


def ENTER(event):
    global d
    global yomi
    yomi = EditBox.get()
    if(yomi == "exit"):
        exit()
    if(mode == True):
        if(yomi == ''):
            return
        elif(yomi == "reset"):
            reset1()
            return()
        if(counting == 2.0):
            text_widget.configure(state='normal')
            text_widget.insert(
                counting, '---------------\n')
            text_widget.configure(state='disabled')
            count()
        speak_bouyomi(yomi)
        if(yomi != ''):
            text_widget.configure(state='normal')
            text_widget.insert(
                counting, yomi + '\n')
            text_widget.configure(state='disabled')
        count()
        text_widget.configure(state='normal')
        text_widget.insert(
            counting, '---------------\n')
        text_widget.configure(state='disabled')
        count()
    # mode2
    elif(mode == False):
        if(yomi == ''):
            return
        if(yomi == '@'):
            # print('実行します。')
            text_widget.configure(state='normal')
            text_widget.insert(
                counting, '---------------\n')
            text_widget.configure(state='disabled')
            count()
            speak_bouyomi(d)
            yomi = ''
            d = ''
        elif(yomi == "reset"):
            reset1()
            return()
        else:
            d += str(yomi)
            text_widget.configure(state='normal')
            text_widget.insert(
                counting, yomi + '\n')
            text_widget.configure(state='disabled')
        count()
        nyuuryoku = ''
    EditBox.delete(0, tkinter.END)


def reset1(event):
    global text_widget
    text_widget.configure(state='normal')
    text_widget.delete("1.0", "end")
    text_widget.configure(state='disabled')
    reset2()


def reset2():
    text_widget.configure(state='normal')
    text_widget.insert(
        '1.0', '入力履歴\n')
    text_widget.configure(state='disabled')


def HELP(event):
    messagebox.showinfo(
        "ヘルプ", "即出力モード\n即出力にチェックをつけると使える。\n即出力モードは文章を書いてENTERを押すとすぐにゆっくりがしゃべってくれるモード。\n\n@で出力モード\n@で出力モードは即出力を空白にすると使える\n@で出力モードは改行ができるモード。\n@を入力してENTERを押すとゆっくりがしゃべってくれる。")


def count():
    global counting
    global c
    counting += 1
    c += 1


def change1():
    global mode
    if bln.get() == True:
        mode = bln.get()
    if bln.get() == False:
        mode = bln.get()


def UNDO(event):
    EditBox.delete(0, tkinter.END)
    EditBox.insert(tkinter.END, yomi)


def info(event):
    messagebox.showinfo(
        "INFORMATION", "INFORMATION\nこのプログラムは「棒読みちゃん」をベースに作られています。\nゆっくり簡易化ツール\n作者 あかず")


def ENTERKEY(event):
    ENTER()


# セットアップ
root = tkinter.Tk()
root.geometry("400x500")
Static1 = tkinter.Label(text='ゆっくり簡易化ツール')
Static1.pack()
bln = tkinter.BooleanVar()
bln.set(True)
mode = bln.get()
# GUI
EditBox = tkinter.Entry(width=50)
EditBox.insert(tkinter.END, "ここにしゃべらせたい言葉を入力!")
EditBox.place(x=5, y=25)


soku = tkinter.Checkbutton(
    root, variable=bln, text='即出力', onvalue=True, offvalue=False, command=change1)
soku.place(x=250, y=60)


Button = tkinter.Button(text=u'ENTER', width=10)
Button.bind("<Button-1>", ENTER)
Button.place(x=5, y=60)

# エンターキー
root.bind('<Return>', ENTER)


Button2 = tkinter.Button(text=u'HELP', width=10)
Button2.bind("<Button-1>", HELP)
Button2.place(x=315, y=2)

Button3 = tkinter.Button(text=u'INFO', width=10)
Button3.bind("<Button-1>", info)
Button3.place(x=315, y=30)

Button3 = tkinter.Button(text=u'CLEAR', width=10)
Button3.bind("<Button-1>", reset1)
Button3.place(x=315, y=59)

Button4 = tkinter.Button(text=u'UNDO', width=10)
Button4.bind("<Button-1>", UNDO)
Button4.place(x=90, y=60)

speak_bouyomi()
root.title(u"ゆっくり簡易化ツール")

text_widget = tkinter.Text(root)
text_widget.place(x=0, y=100, height=400, width=400)
text_widget.configure(state='normal')
text_widget.insert(
    '1.0', '入力履歴\n')
text_widget.configure(state='disabled')

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

root.mainloop()
