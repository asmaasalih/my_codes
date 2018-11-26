n = int(input())
bn = bin(n)
s = str(bn)
l = list(s)
longest = 0
current = 0 
for num in l :
    if num == "1":
        current += 1
    else:
        longest = max(current,longest) 
        current = 0
print(max(longest,current))        
            