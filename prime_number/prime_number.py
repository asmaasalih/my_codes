'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
N = int(input())
L = [x for x in range(2,N+1)]
def prime(num):
    lm = []
    if num == 2:
        return True
    else:    
        for n in range(2,num):
            m = num % n
            lm.append(m)
        if 0 in lm:
            return False
        else:
            return True
    

for n in L:
    if prime(n):
        print(n, end=" ")
        

        
