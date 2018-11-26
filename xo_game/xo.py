def xo(s):
	sl = s.lower(s)
    l = list(sl)     #to make it case_insinstive
    x = l.count("x")
    o = l.count("o")
    if (x == o):
        return True
    else: 
        return False
print xo("xoSNodoxoGxxEbotpxoQfxxxoooxoxxxrxxxoZWoxvoxxkoohoUxooAoxxooxCmooyJxL")        
