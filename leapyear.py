def is_leapyear(year):
    byFour = int(year % 4)
    if byFour == 0:
        return True
    return False
