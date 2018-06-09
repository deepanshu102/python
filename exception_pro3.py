
try:
    f=open('d.txt');##->By default its open file in the read-mode 
    a=1/0
    for line in f:
        print(line.strip()); ##->strip() help to read line by line
    f.close
except IOError as e:##->IOError 
    print('File does not Exist......!',e,"\n",IOError,"\n");
except ZeroDivisionError as e:
    print("Divide by Zero ",e);
finally:
    print("Bye CLEANING UP FILE");
    f.close();
