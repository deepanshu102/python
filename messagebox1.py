from tkinter import *
import tkinter.messagebox
root=Tk()
'''#######################################
#enter the title of using show info
->alert is title
->authentication stream error is the message
#######################################'''
e=tkinter.messagebox.showinfo('Alert','Authentication stream error');

'''#########################################
##
pop message box
###########################################
'''
a=tkinter.messagebox.askquestion('Question1','Do you like to try again');
if a=='yes':
	print("HELELE");
else:
	print("GRWETR");
root.mainloop();