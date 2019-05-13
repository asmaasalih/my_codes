#You are given ى words.
#Some words may repeat.
#For each word, output its number of occurrences.
#The output order should correspond with the input order of appearance of the word.
#See the sample input/output for clarification.
#Note: Each input line ends with a "\n" character.

from collections import Counter
n =int(input())    
arr = []
for _ in range(n):
    word = input()
    arr.append(word)
nw = len(Counter(arr).keys())
print(nw)
orders=Counter(arr).values()
for i in orders:
    print(i,end=" ")
