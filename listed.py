seq=('spam','Spam','SPAM!','HELLO');
l=list(seq)##TUple to list
print(l[2]) ##access one element at specific index
print(len(l))## find the length of the list
print(l[0:len(l):2]) ## invoke 2 from 0(start) and ending(len(l)
l.append(1980);## insert the list 
l.insert(1,'SpAm'); #insert at specific location
print(l);
l=l+list(seq); ## concate 2 list
print(l);
del l[1]; ## delete the one item of the list
l[1]='DRunken'
print(l);
