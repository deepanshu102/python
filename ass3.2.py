def reverse(n):
    reverse=0
    while(n>0):
        reverse=reverse*10+n%10;
        n/=10;
    return reverse;
n=int(12456);
print(reverse(n));
