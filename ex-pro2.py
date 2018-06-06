'''
enter value less than 45 
if the 43 

print lager

if more than 35 and less than 43 

print mediumm
if more than 25 and less than 35


print small

if more than 15 and less than 25 

print ex-small
if less than 15 then print not elegible
'''
a=int(input('Enter one value less than or equal to 45:- '));
if a>43 and a<=45:
	print('\nLarge');
elif a>35 and a<=43:
    print('\nMedium');
elif a>25 and a<=35:
	print('\nSmall');
elif a>15 and a<=25:
	print('\nExtra small');

elif a<=15:
	print('\nNot eligible')
else:
	print('\nEntered value is greater than 45');
