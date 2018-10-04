import unittest

def reverseList(list):
    for i in range(int(len(list)/2)):
        temp=list[i]
        list[i]=list[len(list)-1-i]
        list[len(list)-1-i]=temp
    return list

def isPalindrome(str):
    for i in range(int(len(str)/2)):
        if(str[i] != str[len(str)-1-i]):
            return False
        else:
            return True

def coins(change):
    ccoins=[]
    if(num>=25):
        ccoins.append(int(num/25))
        num -= int(num/25)*25
    else:
        ccoins.append(0)
    if(num>=10):
        ccoins.append(int(num/10))
        num -= int(num/10)*10
    else:
        ccoins.append(0)

    if(num>=5):
        ccoins.append(int(num/5))
        num -= int(num/5)*5
    else:
        ccoins.append(0)

    if(num>=1):
        ccoins.append(int(num/1))
        num -= int(num/1)
    else:
        ccoins.append(0)
    print(ccoins)
    return ccoins

    
        

# def factorial():

# def Fib():



class reverseListTest(unittest.TestCase):
    def test1(self):
        return self.assertEqual(reverseList([1,3,5]), [5,3,1])
    def test2(self):
        return self.assertEqual(reverseList([2,4,-3]), [-3,4,2])
class isPalindromeTest(unittest.TestCase):
    def test1(self):
       return self.assertEqual(isPalindrome("racecar"), True)
    def test2(self):
       return self.assertEqual(isPalindrome("rabbit"), False)
if __name__ == "__main__":
    unittest.main()
