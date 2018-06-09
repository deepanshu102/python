from random import *

for i in range(10):
    print(randint(1,10));
    print(random());
    print(uniform(1,10));
    print(randrange(1,10,2));
    print(choice('abcdefghj'));
    items=['10','20','40'];
    print(shuffle(items))
    print(items);
    print('\n',sample([1,2,3,4,5],2));
