def time_converter(time):
    newtime = None
    timemode = None

    listtime = time.split(':')
    itime = int(listtime[0])
    if itime >= 12:
        if itime > 12:
            itime = itime - 12
        newtime = str(itime)
        timemode = ' p.m.'
    else:
        if itime == 0:
            itime = 12
        newtime = str(itime)
        timemode = ' a.m.'
    newtime = newtime + ':' + listtime[1] + timemode    

    return newtime

if __name__ == '__main__':
    print("Example:")
    print(time_converter('12:30'))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert time_converter('12:30') == '12:30 p.m.'
    assert time_converter('09:00') == '9:00 a.m.'
    assert time_converter('23:15') == '11:15 p.m.'
    print("Coding complete? Click 'Check' to earn cool rewards!")