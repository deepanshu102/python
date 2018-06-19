n=int(input("Enter a Number"));

for j in range(1,n):
    str1="0";
    sum1=0;
    for i in range(1,j):
        str1=str1+"+"+str(i);
        sum1=sum1+i;
    print(str1,"=",sum1)
