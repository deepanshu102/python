def printme(str,grup='anonymous'): #Default argument based function
    print(str,' ',grup);
############################################
##      Exercise key(keyword argument)  ####
###########################################
def printkey(str,age):
    if(age<30):
        print("MY NAME IS ",str,'and my age is ',age,'year old');
    elif(age>=30):
        print(age,' is  greater than 30');
    return (str,age);
###############################################################







printkey("Deepanshu",21);##Positional agrument
printkey(age=31,str='deepanshu') ## notes pass agrouments values are suffle ->keyword argument
printme("abc");
printme('Deepanshu');
printme('deep','Root user');
