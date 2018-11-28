N = int(input())
Array = list(map(int,input().split()))
Answer = 1
for num in Array:
    Answer = (Answer * num) % (7 + 10**9)
print(Answer)    