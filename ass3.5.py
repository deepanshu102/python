sum=0;
for i in range(5):
    a=int(input("enter the mark of subject"));
    sum+=a;
if(sum/5>90):
    print("GRADE: A");
elif(sum/5>70 and sum/5<=90):
    print("GRADE: B");
elif(sum/5>60 and sum/5<=70):
    print("GRADE : C");
else:
    print("GRADE: D");
