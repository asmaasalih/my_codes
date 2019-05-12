import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    #
    # Write your code here.
    #
    hour = int(s[:2])
    state = s[8:]
    if hour < 12 and state == "AM":
        new_string = s[:8]
    elif hour < 12 and state == "PM":
        hour += 12
        new_string = str(hour) + s[2:8]
    elif hour == 12 and state == "AM":
        hour = 0
        new_string = "00" + s[2:8]
    elif hour == 12 and state == "PM":
        new_string = s[:8]
    return new_string

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
