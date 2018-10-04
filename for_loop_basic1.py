
# Basic
for i in range(151):
    print(i)

# # Multiples of Five
for i in range(5, 1000001):
    if(i%5==0):
        print(i)

# # Counting, the Dojo Way
for i in range(0, 101):
    if(i%10==0):
        print('Coding Dojo')
    elif(i%5==0):
        print('Coding')
    else:
        print(i)
        
# # Whoa. That Sucker's Huge
sum = 0
for i in range(0,500001):
    if(i%3==0):
        sum += i
print(sum)



# # Countdown by Fours
for i in range(2018,0,-4):
    print(i)

# # Flexible Countdown
lownum=2
highnum=9
mult=3
for i in range(lownum,highnum+1):
    if(i%mult==0):
        print(i)



list = [3,5,1,2]
for i in list:
    print(i)
# 3,5,1,2

list = [3,5,1,2]
for i in range(list):
    print(i)


list = [3,5,1,2]
for i in range(len(list)):
    print(i)
# 0,1,2,3