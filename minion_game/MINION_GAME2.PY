def minion_game(s):
    # your code goes here
    stuart = 0
    kevin = 0
    for i in range(len(s)):
        if s[i] in "AEOUI":
            kevin += (len(s) - i)
        else:
            stuart += (len(s)- i)
    if stuart > kevin:
        print("Stuart {}".format(stuart))
    elif stuart == kevin:
        print("Draw")
    else:
        print("Kevin {}".format(kevin))

minion_game("BANANA")