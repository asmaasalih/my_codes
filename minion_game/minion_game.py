def minion_game(string):
    # your code goes here
    vowels = ["A","E","I","O","U"]
    Stuart = []
    Kevin = []
    n = 0
    for char in string:
        if char not in vowels:
            i = 1
            while i <= len(string):
                sub = string[n:i]
                Stuart.append(sub)
                i +=1
            string = string[n+1:]        
        else:
            j = 1
            while j <= len(string):
                sub = string[0:j]
                Kevin.append(sub)
                j += 1
            string = string[n+1:]        
    res1 = len(Stuart)
    res2 = len(Kevin)
    if res1 > res2:
        print("Stuart {}".format(res1))
    elif res2 > res1:
        print("Kevin {}".format(res2))
    else:
        print("Draw") 
        
minion_game("BANANA")       