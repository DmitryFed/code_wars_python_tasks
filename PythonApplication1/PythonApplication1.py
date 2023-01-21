
#
def queue_time(customers, n):
   l = [0]*n
   
   for i in range(len(customers)):

      min_value =  min(l)

      indexofmin = l.index(min_value)

      l[indexofmin] += customers[i];  

   return max(l)


def solution(s):
  
    result = [];
    for i in range(0,len(s),2):
        
        result.append(s[i:i+2])

    if len(s)%2 != 0:
       result[len(result)-1] +="_"

    return result

def create_phone_number(n):
	return "({}{}{}) {}{}{}-{}{}{}{}".format(*n)

def likes(names):
    n = len(names)
    return {
        0: 'no one likes this',
        1: '{} likes this', 
        2: '{} and {} like this', 
        3: '{}, {} and {} like this', 
        4: '{}, {} and {others} others like this'
    }[min(4, n)].format(*names[:3], others=n-2)
 
# url: https://www.codewars.com/kata/55bf01e5a717a0d57e0000ec/train
# example: 123 -> 1*2*3 -> 6 (return 1)
# example: 999 -> 9*9*9 -> 729-> 7*2*9 ->126 -> 1*2*6 -> 12 -> 1*2 ->2 (return 4)
def persistence(n):
    mutable_number = 1 
    counter = 0 
    if n < 10: return 0
    while n > 0:
       mutable_number*=n%10
       n//=10 
       if n == 0:
          n = mutable_number
          mutable_number = 1 
          if n < 10: break
          counter += 1       
    return counter 

print(persistence(10))

