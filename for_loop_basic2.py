# Biggie Size 
def posbig(arr):
    for i in range(len(arr)):
        if(arr[i]>0):
            arr[i]='pos'
    print(arr)    
posbig([-1,2,5,-6,-9])

# Count Positives
def lastposval(arr):
    count = 0
    for i in range(len(arr)):
        if(arr[i]>0):
            count = count +1
    arr[len(arr)-1] = count
    print(arr)
    return arr
lastposval([1,-3,5,6,1,3])    

# SumTotal
def sumallvals(arr):
    sum= 0
    for i in range (len(arr)):
        sum = sum + arr[i]
    print(sum)
    return sum

sumallvals([1,2,3,4,5])

# Length 
def length(arr):
    print(len(arr))


# Minimum 
def minimum(arr):
    print(min(arr))

    # or

def minimum(arr):
    min=arr[0]
    for i in range(len(arr)):
        if(arr[i]<min):
            min=arr[i]
    print(min)
    
# Maximum 
def maximum(arr):
    print(min(arr))

    # or

def maximum(arr):
    max=arr[0]
    for i in range(len(arr)):
        if(arr[i]<max):
            max=arr[i]
    print(max)

# UltimateAnalyze 
def arrtodict(arr):
    totalsum=sum(arr)
    avg= sum(arr)/len(arr)
    minimum = min(arr)
    maximum = max(arr)
    length=len(arr)
    dictionary={totalsum, avg, minimum, maximum, length}
    print(dictionary)

arrtodict([1,2,3,4])


# ReverseArr
def ReverseArr(arr):
    arr.reverse()
    print(arr)

    # or



# def ReverseArr(arr):
#     temp=0
#     for i in range(0,(int(len(arr)/2))):
#         temp=arr[i]
#         arr[i]= arr[(len(arr)-1)]
#         arr[(len(arr)-1)]=temp
#     print(arr)
#     return arr

# ReverseArr([1,2,3,4,5,6])
