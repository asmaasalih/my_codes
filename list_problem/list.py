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

if __name__ == '__main__':
    N = int(input())
    l = []
    for command in range(N):
        x = input().split(" ")
        command = x[0]
        if command == "append":
            l.append(int(x[1]))

        elif command == "insert":
            l.insert(int(x[1]),int(x[2]))
            
        elif command == "pop":
            l.pop()

        elif command == "sort":
            l.sort()    
            
        elif command == "remove":
            l.remove(int(x[1]))
            
        elif command == "reverse":
            l = l[::-1]
        
        elif command == "print":
            print(l)
            

