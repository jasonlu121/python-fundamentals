# arr = [1,5,3,2,0,8]

# def bubbleSort(arr):
#     for j in range(len(arr)-1):    
#         for i in range(len(arr)-1-j):
#             # print('index', i, 'value',arr[i])
#             # print('comparing', arr[i], arr[i+1])
#             if(arr[i]>arr[i+1]):
#                 arr[i],arr[i+1]=arr[i+1],arr[i]
#     print(arr)
#     return(arr)        

# bubbleSort(arr)




def selectionSort(arr):
   for i in range(len(arr)-1,0,-1):
       positionOfMax=0
       for j in range(1,i+1):
           if arr[j]>arr[positionOfMax]:
               positionOfMax = j

       temp = arr[i]
       arr[i] = arr[positionOfMax]
       arr[positionOfMax] = temp

arr = [54,26,93,17,77,31,44,55,20]
selectionSort(arr)
print(arr)
