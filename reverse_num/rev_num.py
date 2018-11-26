def reverse_number(n):
    s = str(n)
    l = []
    for i in s:
        l.append(i)
    lr = l[::-1]    
    if "-" in lr:
        lr.remove("-")
        ns = "".join(lr)
        num_rev = - int(ns)
        return num_rev
    else:
        ns = "".join(lr)
        num_rev = int(ns)
        return num_rev
print reverse_number(-123)        