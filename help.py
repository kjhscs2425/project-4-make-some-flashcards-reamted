import math
#a is negitive 
#b is positive




def qudratic():
    a = 1
    b = 2
    for i in range(10):
        
  
        x = (a+b)/2
        
        x = float(x)
        
        quadratic_1 = math.pow(x, 4)-3*(math.pow(x, 3))+4

        if -0.001 < quadratic_1 and quadratic_1 < 0.001: 
            print("Found it!")
            print(x)
            break
        else:
            print(x)
            if quadratic_1 > 0:
                a = x
                
            else:
                b = x
            
   
        print(a)
        print(b)

def poly(x):
    return math.pow(x, 4)-3*(math.pow(x, 3))+4
    #return math.pow(x, 5) -3*(math.pow(x, 3)) + 1
    

def general_purpose(a, b):
    if poly(a) > 0 and poly(b) < 0:
        neg = b
        pos = a 
    elif poly(a) < 0 and poly(b) > 0:
        neg = a
        pos = b
    else:
        print("there is no root in this interval, google intermidiate value theorem") 
        return
    for i in range(100):
        mid = (neg+pos)/2
        value = poly(mid)
        print(neg, pos, mid)
        if -0.001 < value and value < 0.001:
            print(f"the root here is {mid}")
            break
        else:
            if value > 0:
                pos = mid
            else:
                neg = mid
        
general_purpose(1,2)
