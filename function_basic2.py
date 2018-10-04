
# Countdown
array=[]
def a(num):
    for i in range(num, -1,-1):
        array.append(i)
    print(array)
    return array

a(10)


# Print and Return 
def a(arr):
    print(arr[0])
    return arr[1]

a([1,2,3,4,5,])


# First Plus Length
def a(arr):
    sum=arr[0] + len(arr)
    print(sum)
    return sum

a([1,2,3,4,5,6])


# Values Greater than Second
def a(arr):
    count=0
    newarr=[]
    for i in range(len(arr)):
        if(arr[i]>arr[1]):
            newarr.append(arr[i])
            count = count + 1
    print(newarr)
    print(count)
    if(count == 1):
        return False
    else:
        return newarr

    
a([1,2,3,4,5,6])



# This Length, That Value
def lengthAndValue(a,b):
    arr = []
    for i in range(a):
        arr.append(b)
    print(arr)
lengthAndValue(5,8)
