import math
import os
import random
import re
import sys

# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):
    ap_list = []
    or_list = []
    count_ap = 0  # number of apples on the house
    count_or = 0  # number of orange on the house
    for ap in apples:
        ap += a
        ap_list.append(ap)
    for ora in oranges:
        ora += b
        or_list.append(ora)
    for i in ap_list:
        if s <= i <= t :
            count_ap += 1
    for i in or_list:
        if s <=i <= t:
            count_or += 1
    print(count_ap)
    print(count_or)
if __name__ == '__main__':
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
