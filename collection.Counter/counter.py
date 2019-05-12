#Raghu is a shoe shop owner. His shop has x number of shoes. 
#He has a list containing the size of each shoe he has in his shop. 
#There are n number of customers who are willing to pay  amount of money only if they get the shoe of their desired size.
#Your task is to compute how much money Raghu earned.

from collections import Counter
Ns = int(input())
shose = Counter(list(map(int,input().split())))
Nc = int(input())
total_money = 0
for i  in range(Nc):
    size ,cost = map(int,input().split())  
    if shose[size]:
        total_money += cost
        shose[size] -= 1

print(total_money)         
