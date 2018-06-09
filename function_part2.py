from functions import *
a=int(input("\n1.)Find area of Triangle \n2.)Find area of Rectangle\n Enter your choice :- "));
if(a==1):
    a=int(input("enter one integer base of the triangle"));
    b=int(input("enter one integer height of the triangle"));
    print(tri(a,b));
elif(a==2):
    a=int(input("enter one integer length of the rectangle"));
    b=int(input("enter one integer breath of the rectangle"));
    rect(a,b);

else:
    print("invalid choice");tri(a,b);
