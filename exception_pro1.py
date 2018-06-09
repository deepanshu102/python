'''
_________________________
EXCEPTION HANDLING
_________________________

SYNTAX:-
            try:
                    try-block
            except Exception1:
                    it's act as an catch block 
            except Exception2:
                    another catch
            else://its optional
'''
################################
try:
    f=open('d.txt');##->By default its open file in the read-mode 
    for line in f:
        print(line.strip()); ##->strip() help to read line by line
    f.close();
#################################################
except IOError as e:##->IOError 
    print('File does not Exist......!',e,"\n",IOError,"\n");
##################################################
