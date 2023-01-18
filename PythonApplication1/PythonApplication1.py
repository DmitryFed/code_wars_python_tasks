
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

