if __name__ == '__main__':
    N = int(input())
    nested_list = []
    for _ in range(N):
        name = input()
        score = float(input())
        nested_list.append([name,score])
    score_list = []
    for i in nested_list:
        score_list.append(i[1])
    mini = min(score_list)
    score_list = sorted(score_list)
    nun_mini = score_list.count(mini)
    score_list = score_list[nun_mini:]

    second_lowest = min(score_list)
    second_lowest_list = []
    for i in range(len(nested_list)):
        if nested_list[i][1] == second_lowest:
            second_lowest_list.append(nested_list[i][0])
    sorted_list = sorted(second_lowest_list)
    for name in sorted_list:
        print(name)        
