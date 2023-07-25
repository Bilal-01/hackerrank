
def dayOfProgrammer(year):
    month = 0
    day = 0
    if(year < 1918):
        if(year % 4 == 0):
            month='09'
            day = '12'
        else:
            month = '09'
            day = '13'
    if(year > 1918):
        if(year%400 == 0 or (year%4==0 and year%100 != 0)):
            month = '09'
            day = '12'
        else:
            month = '09'
            day = '13'
    if(year == 1918):
        month = '09'
        day = '25'

    return (day + '.' + month + '.' + str(year))


year = 1918
print(dayOfProgrammer(year))
