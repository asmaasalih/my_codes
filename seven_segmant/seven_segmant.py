
T = int(input())
for _ in range(T):
    N = input()
    tot_sticks = 0
    for num in N:
        n = int(num)
        if n == 0 or n == 6 or n == 9:
            match = 6
            tot_sticks += match
        
        elif n == 2 or n == 5 or n == 3:
            match = 5
            tot_sticks += match
            
        elif n == 8 : 
            match = 7    
            tot_sticks += match
            
        elif n == 1 :
            match = 2
            tot_sticks += match
            
        elif n == 4:
            match = 4
            tot_sticks += match
        elif n == 7 :
            match = 3
            tot_sticks += match
    if tot_sticks % 2 == 0:
        d = int(tot_sticks / 2)
        print("1"*d)
    elif tot_sticks == 3:
        print("7")
    else:
        tot_sticks = tot_sticks - 3
        d = int(tot_sticks / 2)
        print("7"+"1"*d)
        
            