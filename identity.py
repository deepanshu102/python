#its a identity operators i.e. is,is not

''' multi line comment 
in which 2 variable and check that its under  variable value are similar
'''
a=20
b=20
if(a is b):
        print('a,b have same identity')
else:
        print('a,b are different')
b=10
if(a is not b):
        print("a,b have different identity")
else:
        print("a,b have same identity")

