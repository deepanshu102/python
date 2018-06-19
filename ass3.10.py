def pal(num):
    rev=int(0);
    temp=num;
    while(temp>0):
        rev=rev*10+temp%10;
        temp=temp/10;
    if(rev==num):
        return True
    else:
        return False;
a=int(12334);
if(pal(a)):
    print("palindrome");
else:
    print("Not palindrome");
