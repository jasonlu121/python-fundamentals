# def random(min,max):
#     for 
# print(random.random()*50) # returns a float between 0.000 to 50.000

# randInt() returns a random integer between 0 to 100
import random
def rand():
    print (int(random.random()*100))
    return int(random.random()*100)
rand()

# randInt(max=50) returns a random integer between 0 to 50
import random
def rand():
    print (int(random.random()*50))
    return int(random.random()*50)
rand()


# randInt(min=50) returns a random integer between 50 to 100
import random
def rand():
    x =(int(random.random()*100))
    if( x > 50):
        print(x)
        return x
    else:
        rand()
rand()

# or

import random
def rand():
    x =(int(random.random()*50)+50)
    print(x)
    return x
rand()

# randInt(min=50, max=500) returns a random integer between 50 and 500

import random
def rand():
    x =(int(random.random()*500))
    if( x > 50):
        print(x)
        return x
    else:
        rand()
rand()

#or

import random
def rand():
    x =(int(random.random()*450)+50)
    print(x)
    return x
rand()