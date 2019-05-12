#Problem
"""Consider a list (list = []).
 You can perform the following commands:

insert i e: Insert integer  at position .
print: Print the list.
remove e: Delete the first occurrence of integer .
append e: Insert integer  at the end of the list.
sort: Sort the list.
pop: Pop the last element from the list.
reverse: Reverse the list.
Initialize your list and read in the value of  followed by  lines of commands where each command will be of the  types listed above.
Iterate through each command in order and perform the corresponding operation on your list."""

#Output Format
#For each command of type print, print the list on a new line.

nested_list = [['Harsh', 20], ['Beria', 20], ['Varun', 19], ['Kakunami', 19], ['Vikas', 21]]
score_list = []
for i in nested_list:
    score_list.append(i[1])
print(score_list)
mini = min(score_list)
print(mini)
score_list = sorted(score_list)
nun_mini = score_list.count(mini)
print(nun_mini)
score_list = score_list[nun_mini:]
print(score_list)  
    
print(score_list)        
second_lowest = min(score_list)
print(second_lowest)
second_lowest_list = []
for i in range(len(nested_list)):
    if nested_list[i][1] == second_lowest:
        second_lowest_list.append(nested_list[i][0])
print("second lowest list: " ,second_lowest_list)
sorted_list = sorted(second_lowest_list)
print(sorted_list)
for name in sorted_list:
    print(name)

