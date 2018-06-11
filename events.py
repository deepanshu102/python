from tkinter import *
root=Tk()
#root.title("Events");
def leftClick(event):
	print("LEFT");
def middleClick(event):
	print("Middle");
def rightClick(event):
	print("Right");
	
frame=Frame(root,width=200,height=200)
#Event is something the user does to widget,function that gets called
frame.bind("<Button-1>",leftClick);#button-1 is deined for leftclick
frame.bind("<Button-2>",middleClick);
frame.bind("<Button-3>",rightClick);
frame.pack();
root.mainloop()
