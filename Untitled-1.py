from tkinter import *

root = Tk()

e=Entry(root, bg='green',borderwidth=5)
e.pack()

def teachername():
    mylabel=Label(root,text="Enter the no. of Teacher")
    mylabel.pack()
    a=int(e.get())
    print(a)
    data=[]
    for i in range(a):
        mylabels=Label(root,text="Name of Teacher")
        mylabels.pack()
        name=Entry(root)
        name.pack()
        data[i]=data.append(name.get())
    

myButton = Button(root,text="Enter The no. of teacher" , command=teachername ,fg="blue",bg="green")
myButton.pack()


def time():
    d=Entry(root)
    d.pack()
    


second=Button(root,text='Enter The Subject Time',command=time,fg='black',bg='white')
second.pack()



root.mainloop()
