def store(dic,n):
    i=0
    while i<n:
        a=input("Enter the name of the person :- ");
        b=int(input("Enter the age of "));
        dic[a]=b;
        #print(dic);
        i=i+1;
def find_age(dic,name):
    return dic[name]
dic={};
n=int(input("Enter how many members in your family"));
store(dic,n);
n=input("Enter the name of the person");
print("Age of ",n," is ",find_age(dic,n))
for k in dic:
    print(k,'\t',dic[k])
