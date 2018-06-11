from tkinter import *
root=Tk()
root.title("Foregound");
one=Label(root,text="One",bg="red",fg="white")
one.pack()
two=Label(root,text="Two",bg="green",fg="black");
two.pack(fill=X)#fill=X-makes the widget AS WIDE AS THE PARENT
three=Label(root,text="Three",bg="blue",fg="white")
three.pack(side=LEFT,fill=Y)
root.mainloop()