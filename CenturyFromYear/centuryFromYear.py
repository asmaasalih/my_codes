def century(year):
    
    # Finish this :)
    if year in range(1 ,101):
        return 1
    elif year % 100 == 0 :
        return int(year/100)
    else:
        return int((year/100)+1)
    



    