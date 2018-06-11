from tkinter import *
root=Tk();
root.title("Login");
lo={'A':'1234','abc':"123"}
def log():
	v=lo[entry_1.get()];
	if(v==entry_2.get()):
		label2=Label(root,text="Sucessfully login in");
		label2.grid(row=4,column=1);
	else:
		label2=Label(root,text="INVALID USER ID AND PASSWORD");
		label2.grid(row=4,column=1);
	print(var.get())
		
label_1=Label(root,text="Name");
label_2=Label(root,text="Password");
entry_1=Entry(root);
entry_2=Entry(root);
var=IntVar()
label_1.grid(row=0,sticky=E);
label_2.grid(row=1,sticky=E)# sticky helps to move Directions N,W,E,S,Center
entry_1.grid(row=0,column=1)
entry_2.grid(row=1,column=1)

c=Checkbutton(root,text="Keep me Logged in",variable=var,command=log);
c.grid(columnspan=2)

root.mainloop()
