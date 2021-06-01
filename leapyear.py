def is_leapyear(year):
    byFour = int(year % 4)
    if byFour == 0:
        by100 = int(year % 100)
        if by100 == 0:
            return False
        else:
            return True
    else:
        return False
