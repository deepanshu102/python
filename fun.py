def inputed(mylist):
    for i in range(10):
        a=int(input("Enter {}th value".format(i+1)));
        mylist.append(a);
def chn(mylist):
    mylist=['hello','how','are',' you?'];#this would assign new references  in mylist
    print(mylist,'Id of local variable:-',id(mylist));
