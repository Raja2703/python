import tkinter
from tkinter import Entry, Label,Button
tk=tkinter.Tk()

def card_validity():
    card_no=entry.get()
    arr=[]
    for i in range(0,16):
        if(i%2==0):
            a=0
            no=int(card_no[i])*2
            if(no>9):
                a+=no%10
                a+=no//10
                arr.append(a)
            else:
                arr.append(no)
        else:
            arr.append(int(card_no[i]))
 
    sum=0
    for i in range(0,16):
        sum=sum+arr[i]

    if(str(sum)[-1]=='0'):
        Label(tk,text='Valid').pack()
    else:
        Label(tk,text='Invalid').pack()

tk.geometry('500x500')
tk.title('Card Validity')
Label(tk,text='Enter Card no:').pack()
entry=Entry(tk)
entry.pack()
btn=Button(tk,text="Submit",command=card_validity)
btn.pack()

tk.mainloop()

#4408041234567893

#4408041234567893

#3530111333300000
