usa=["atlanta","new york","chicago","baltimore"]
uk=["landon","bristol","cambridge"]
india=["mumbai","delhi","banglore"]

##############################
## pro1                 ###
############################
city=input("Enter the City name:- ");

for k in usa:
    if(k==city):
        print('usa')
for k in uk:
    if(k==city):
        print('UK');
for k in india:
    if(k==city):
        print("India");
###########################
##      problem 2       ##
#########################
city=input("Enter 1 city name:- ");
city1=input("enter 2nd city name:-");
if(city in uk and city1 in uk):
    print("UK");
elif(city in india and city1 in india):
    print("INDIA");
elif city in usa and city1 in usa:
    print("USA");

