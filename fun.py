def fac(n):
    if(n<=0):
        return 1;
    else:
        return n*fac(n-1);
def odd_even(n):
    if(n%2==0):
        print(n,"Even Number");
    else:
        print(n,"Odd Number");
