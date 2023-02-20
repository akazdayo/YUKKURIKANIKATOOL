import tkinter
import datetime
from tkinter import messagebox
from speaker import bouyomi
class GUIController():
    def __init__(self) -> None:
        self.mode = True
        self.d = ''
        self.counting = 2.0
        self.read = ''

    def on_press_enter(self, _):
        self.read = EditBox.get()
        if (self.read == "exit"):
            exit()
        elif (self.read == "time"):
            dt_now = datetime.datetime.now()
            times = dt_now.strftime('%Y年%m月%d日 %H時%M分%S秒')
            Speaker("速度(200)" + times, int(vol.get()))
            self.read = times
        elif (self.mode == True):
            if (self.read == ''):
                return
            elif (self.read == "reset"):
                self.reset()
                return ()
            if (self.counting == 2.0):
                text_widget.configure(state='normal')
                text_widget.insert(
                    self.counting, '---------------\n')
                text_widget.configure(state='disabled')
                self.counting += 1
            Speaker(self.read, int(vol.get()))
            if (self.read != ''):
                text_widget.configure(state='normal')
                text_widget.insert(
                    self.counting, self.read + '\n')
                text_widget.configure(state='disabled')
            self.counting += 1
            text_widget.configure(state='normal')
            text_widget.insert(
                self.counting, '---------------\n')
            text_widget.configure(state='disabled')
            self.counting += 1
        # self.mode2
        elif (self.mode == False):
            if (self.read == ''):
                return
            if (self.read == '@'):
                text_widget.configure(state='normal')
                text_widget.insert(
                    self.counting, '---------------\n')
                text_widget.configure(state='disabled')
                self.counting += 1
                Speaker(self.d, int(vol.get()))
                self.read = ''
                self.d = ''
            elif (self.read == "reset"):
                self.reset()
                return ()
            else:
                self.d += str(self.read)
                text_widget.configure(state='normal')
                text_widget.insert(
                    self.counting, self.read + '\n')
                text_widget.configure(state='disabled')
            self.counting += 1
        EditBox.delete(0, tkinter.END)

    def reset(self, _):
        text_widget.configure(state='normal')
        text_widget.delete("1.0", "end")
        text_widget.configure(state='disabled')
        text_widget.configure(state='normal')
        text_widget.insert(
            '1.0', '入力履歴\n')
        text_widget.configure(state='disabled')

    def HELP(self, _):
        messagebox.showinfo(
            "ヘルプ", "即出力モード\n即出力にチェックをつけると使える。\n即出力モードは文章を書いてENTERを押すとすぐにゆっくりがしゃべってくれるモード。\n\n@で出力モード\n@で出力モードは即出力を空白にすると使える\n@で出力モードは改行ができるモード。\n@を入力してENTERを押すとゆっくりがしゃべってくれる。")

    def change(self):
        if bln.get() == True:
            self.mode = bln.get()
        if bln.get() == False:
            self.mode = bln.get()

    def UNDO(self, _):
        EditBox.delete(0, tkinter.END)
        EditBox.insert(tkinter.END, self.read)

    def info(self, _):
        messagebox.showinfo(
            "INFORMATION", "INFORMATION\nこのプログラムは「棒読みちゃん」をベースに作られています。\nゆっくり簡易化ツール\n作者 あかず\n")


#セットアップ
GUIController = GUIController()

#話者の設定
Speaker = bouyomi.speak

root = tkinter.Tk()
root.geometry("400x500")
Static1 = tkinter.Label(text='ゆっくり簡易化ツール')
Static1.pack()
bln = tkinter.BooleanVar()
bln.set(True)

# GUI
EditBox = tkinter.Entry(width=50)
EditBox.insert(tkinter.END, "ここにしゃべらせたい言葉を入力!")
EditBox.place(x=5, y=25)

outCheckBox = tkinter.Checkbutton(
    root, variable=bln, text='即出力', onvalue=True, offvalue=False, command=GUIController.change)
outCheckBox.place(x=250, y=60)

GUIController.mode = bln.get()

vol = tkinter.DoubleVar()
vol.set(100)
sc = tkinter.Scale(
    variable=vol,
    orient=tkinter.HORIZONTAL,
    length=200,
    from_=0,
    to=100,
    command=lambda e: print('volume:%4d' % vol.get()))
sc.place(x=0, y=88)

text_widget = tkinter.Text(root)
text_widget.place(x=0, y=130, height=370, width=400)
text_widget.configure(state='normal')
text_widget.insert(
    '1.0', '入力履歴\n')
text_widget.configure(state='disabled')

Button = tkinter.Button(text=u'ENTER', width=10)
Button.bind("<Button-1>", GUIController.on_press_enter)
Button.place(x=5, y=60)

#エンターキー
root.bind('<Return>', GUIController.on_press_enter)


Button2 = tkinter.Button(text=u'HELP', width=10)
Button2.bind("<Button-1>", GUIController.HELP)
Button2.place(x=315, y=2)

Button3 = tkinter.Button(text=u'INFO', width=10)
Button3.bind("<Button-1>", GUIController.info)
Button3.place(x=315, y=30)

Button3 = tkinter.Button(text=u'CLEAR', width=10)
Button3.bind("<Button-1>", GUIController.reset)
Button3.place(x=315, y=59)

Button4 = tkinter.Button(text=u'UNDO', width=10)
Button4.bind("<Button-1>", GUIController.UNDO)
Button4.place(x=90, y=60)


Speaker(text="ゆっくり簡易化ツールが起動しました。ベータ7.5")
root.title(u"ゆっくり簡易化ツール")

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

root.mainloop()