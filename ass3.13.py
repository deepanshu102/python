n=int(input("enter the number"));
for j in range(0,n-1):
    for i in range(0,n-1):
        if(i==j):
            print("1\t");
        else:
            print("0\t");
    print("\n");
