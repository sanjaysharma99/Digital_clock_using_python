from tkinter import *
import time

app=Tk()
app.title('Clock')
app.config(bg='#00FFB1')

hl=Label(app,bg='#000000',fg='#EB00FF',font='Robot 16 bold')
hs=Label(app,text=':',bg='#000000',fg='#EB00FF',font='Robot 16 bold')
ml=Label(app,bg='#000000',fg='#EB00FF',font='Robot 16 bold')
ms=Label(app,text=':',bg='#000000',fg='#EB00FF',font='Robot 16 bold')
ql=Label(app,bg='#000000',fg='#EB00FF',font='Robot 16 bold')

hl.grid(row=1,column=1,padx=5,pady=5)
hs.grid(row=1,column=2,padx=5,pady=5)
ml.grid(row=1,column=3,padx=5,pady=5)
ms.grid(row=1,column=4,padx=5,pady=5)
ql.grid(row=1,column=5,padx=5,pady=5)

while True:
    seconds=time.time()
    c_time=time.localtime(seconds)

    if c_time.tm_hour<10:
        hl.config(text=f'0{c_time.tm_hour}')
        hl.update()
    else:
        hl.config(text=c_time.tm_hour)

    if c_time.tm_min<10:
        ml.config(text=f'0{c_time.tm_min}')
        ml.update()
    else:
        ml.config(text=c_time.tm_min)

    if c_time.tm_sec<10:
        ql.config(text=f'0{c_time.tm_sec}')
        ql.update()
    else:
        ql.config(text=c_time.tm_sec)
        ql.update()

app.mainloop()