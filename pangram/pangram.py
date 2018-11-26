# Complete the pangrams function below.
def pangrams(s):
    lowerCase = s.lower()
    ch = "abcdefghijklmnopqrstuvwxyz"
    l = []
    for char in ch:
        if char in lowerCase:
            l.append(1)
        else:
            l.append(0)
    if 0 in l:
        return "not pangram"
    else:
        return "pangram"
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = pangrams(s)

    fptr.write(result + '\n')

    fptr.close()
