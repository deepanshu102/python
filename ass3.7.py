a=int(input("enter the value"));
b=int(input("Enter the Second value"));
c=int(input("Enter the Third Value"));
li=[]
li.append(a)
li.append(b)
li.append(c);
print(li[0]);
#print(len(li));
for i in range(len(li)):
    for j in range(len(li)):
        for k in range(len(li)):
            print(li[i],li[j],li[k]);

