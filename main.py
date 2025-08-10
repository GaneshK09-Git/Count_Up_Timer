#count-up timer


import time

def count(end, start=0): #Default arguments should be placed at last and no default should be placed before default arguments.
    for x in range(start, end+1):
        print(x)
        time.sleep(1)
    print("Done!")

count(20, 9) #(a,b) the countdown starts from b and ends at a 
