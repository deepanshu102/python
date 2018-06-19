'''
#->write a program to find the sum of Digit in a Number
'''
a=int(1234);
i=0
sum1=0
while(a>0):
    sum1=sum1+(a%10);
    a/=10;
    i=i+1
print("Sum is :",sum1);
print("Number of digit",i)
