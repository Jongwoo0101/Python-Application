'''

import tkinter
root = tkinter.Tk()
root.mainloop()

import tkinter
root = tkinter.Tk()
root.title('첫 번째 윈도우')
root.geometry('800x600')
root.mainloop()

import tkinter
root = tkinter.Tk()
root.title('첫 번째 라벨')
root.geometry('800x600')
label = tkinter.Label(root, text='라벨 문자열', font=('System', 24))
label.place(x=200, y=100)
root.mainloop()

import tkinter

def click_btn():
    button['text'] = '클릭했습니다'
    
root = tkinter.Tk()
root.title('첫 번째 버튼')
root.geometry('800x600')
button = tkinter.Button(root, text='클릭하십시오', font=("Times New Roman", 24), command=click_btn)
button.place(x=200, y=100)
root.mainloop()

'''

import tkinter

root = tkinter.Tk()
root.title('첫 번째 캔버스')
canvas = tkinter.Canvas(root, width=400, height=600, bg='skyblue')
canvas.pack()
root.mainloop()