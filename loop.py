name="Harrison";
guess=input("So I am thinking of person name.try to guess it: ");
pos=0;
while guess !=name and pos<len(name):
        print("Nope,'That's nott it!Hint:letter");
        print(pos+1,"is",name[pos]+".");
        guess=input("Guess again");
        pos=pos+1
if pos==len(name) and name!=guess:
    print("TOO BAD,YOU COULD NOT GET IT.THE name was ",name+".")
else:
    print("\nGreat you got it in",pos+1,"guesses!");
