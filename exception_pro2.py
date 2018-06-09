def main():
    try:
        for line in readfile("d.txt"):
            print(line.strip()); ##->strip() help to read line by line 
    except IOError as e:##->IOError 
        print('File does not Exist......!',e,"\n",IOError,"\n");
    except ValueError as e:
        print('BAD FILE NAME',e);
def readfile(filename):
    if filename.endswith('.txt'):
        fh=open(filename);
        print(fh.readlines())#
        return fh.readlines();
    else:
        raise ValueError('Filename must end with.txt');
    ######################################################
main();
