from tkinter import *
root=Tk();
#Frame is rectangular area that can contain 
top=Frame(root)
top.pack();
bottomFrame=Frame(root);
bottomFrame.pack(side=BOTTOM)
b1=Button(top,text="Button 1",fg="red");
b2=Button(top,text="Button 2",fg="blue");
b3=Button(top,text="Button 3",fg="green");
b4=Button(bottomFrame,text="Button 4",fg="red");

#These buttons will be on top
b1.pack(side=LEFT);
b2.pack(side=LEFT);
b3.pack(side=LEFT);

#Button 4 is on the Bottom
b4.pack(side=BOTTOM)
root.mainloop()
