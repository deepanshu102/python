def rect():
    print(a*b);
def triangle():
    print((a*b)/2);
a=int(input("\n1.)Find area of Triangle \n2.)Find area of Rectangle\n Enter your choice :- "));
if(a==1):
    a=int(input("enter one integer base of the triangle"));
    b=int(input("enter one integer height of the triangle"));
    triangle();
elif(a==2):
    a=int(input("enter one integer length of the rectangle"));
    b=int(input("enter one integer breath of the rectangle"));
    rect();

else:
    print("invalid choice");
