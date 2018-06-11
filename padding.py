import tkinter as tk
root=tk.Tk()
logo=tk.PhotoImage(file="jims.JPG")
w1=tk.Label(root,image=logo).pack(side="right");
exp="""asdfjksdl;akgj;sdfjgvfsdkl;jiotrmvgodfjoasdgfsdahfkasdfsdkajhflaksdjhfkasdhfasdklfjasdkf\jklsdgafklghasdfkjlasdghflkasd"""
w2=tk.Label(root,justify=tk.LEFT,padx=10,text=exp).pack(side="left")
root.mainloop()