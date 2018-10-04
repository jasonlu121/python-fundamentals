def coins(num):
    ccoins=[]
    if(num>=25 & num > 0):
        ccoins.append(int(num/25))
        num -= int(num/25)*25
    else:
        ccoins.append(0)
    if(num>=10 & num > 0):
        ccoins.append(int(num/10))
        num -= int(num/10)*10
    else:
        ccoins.append(0)

    if(num>=5 & num > 0):
        ccoins.append(int(num/5))
        num -= int(num/5)*5
    else:
        ccoins.append(0)

    if(num>=1 & num > 0):
        ccoins.append(int(num/1))
        num -= int(num/1)
    else:
        ccoins.append(0)
print(ccoins)
return ccoins

coins(87)
    
        




#     if(change>=25):
#         coins['quarters']=int(change/25)
#         newchange = (change%25)
#     elif(change>=10 or newchange>=10):
#         coins['dimes']=int(newchange/10)
#         newchange = (newchange%10)
#     elif(change>=5 or newchange>=5):
#         coins['nickels']=int(newchange/5)
#         newchange = (newchange%5)
#     else:
#         coins['nickels']=newchange
    
#     print(newchange)
#     print(coins)


# coinchange(87)




def coinchange(change):
    coins = [25,10,5,1]
    change = { }
    for 
