def swap_case(s):
    n_s = ""
    for char in s:
        if char.islower():
            char = char.upper()
            n_s += char
        elif char.isupper():
            char = char.lower()
            n_s += char
        else:
            n_s += char
    return n_s                    
                                                           
    return

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)