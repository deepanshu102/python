def enter(li,n):
	i=0
	while i<n:
		a=int(input("Enter integer Value only"));
		li.append(a);
		i+=1;
def average(li):
    sum=0
    for i in li:
        sum+=i;
    return sum/len(li);
li=[];
n=int(input("HOW MANY VALUES YOU WANT TO INSERTED"));
enter(li,n);
print("AVERAGE IS ",average(li));
