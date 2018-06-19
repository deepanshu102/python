def count(num):
    i=int(0)
    print(num);
    while(num>0):
        num=num/10;
        i=i+int(1);
    return i;
a=int(input("Enter the number"));
print("Number of the digit",count(a));
