a=int(input("enter One Integer value\n"))
b=int(input("Enter Second Integer value\n"))
c=int(input("1.)Using 3rd variable\n2.)Without using 3rd variable\nEnter your choice:-"));
print("\nCurrent values \na="+str(a)+"\tb="+str(b))
if(c==1):
    c=a;
    a=b;
    b=c;
elif(c==2):
    a=a+b;
    b=a-b;
    a=a-b;
print("\nAfter Swaping \n a={}\t b={}".format(a,b))
        


