'''
from tkinter import * # add tkinter module

window = Tk() # create root window
label = Label(window, text="Hello tkinter") # create label widget
label.pack() # put label widget on window

window.mainloop() # window wait for user move

from tkinter import *
window = Tk()

button = Button(window, text="클릭하세요!", bg="yellow", fg="blue", width=80, height=2)

button.pack()
window.mainloop()

from tkinter import *
window = Tk()

entry = Entry(window, fg="black", bg="yellow", width=80)

entry.pack()
window.mainloop()

from tkinter import *

window = Tk()

Label(window, text='박스 #1', bg='red', fg='white').pack()
Label(window, text='박스 #2', bg='green', fg='white').pack()
Label(window, text='박스 #3', bg='blue', fg='white').pack()

window.mainloop()

from tkinter import *

window = Tk()

Label(window, text='박스 #1', bg='red', fg='white').pack(side=LEFT)
Label(window, text='박스 #2', bg='green', fg='white').pack(side=LEFT)
Label(window, text='박스 #3', bg='blue', fg='white').pack(side=LEFT)

window.mainloop()

from tkinter import *

window = Tk()

b1 = Button(window, text="박스 #1", bg='red', fg='white')
b2 = Button(window, text="박스 #2", bg='green', fg='white')
b3 = Button(window, text="박스 #3", bg='orange', fg='white')
b4 = Button(window, text="박스 #4", bg='pink', fg='white')

b1.grid(row=0, column=0) 
b2.grid(row=0, column=1) 
b3.grid(row=1, column=0) 
b4.grid(row=1, column=1) 

window.mainloop()

from tkinter import *

window = Tk()

b1 = Button(window, text="박스 #1", bg='red', fg='white')
b1.place(x=0, y=0)
b2 = Button(window, text="박스 #2", bg='green', fg='white')
b2.place(x=20, y=30)
b3 = Button(window, text="박스 #3", bg='orange', fg='white')
b3.place(x=40, y=60)

window.mainloop()

from tkinter import *

window = Tk()
f = Frame(window)

b1 = Button(f, text='박스 #1', bg='red', fg='white')
b2 = Button(f, text='박스 #2', bg='green', fg='black')
b3 = Button(f, text='박스 #3', bg='orange', fg='white')
b1.pack(side=LEFT)
b2.pack(side=LEFT)
b3.pack(side=LEFT)

l = Label(window, text='이 레이블은 버튼들 위에 배치된다.')

l.pack()
f.pack()

window.mainloop()

'''

