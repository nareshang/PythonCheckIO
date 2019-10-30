import re
def checkio(data: str) -> bool:
    lenstr = len(data)
    if lenstr < 10:
        return False
    flag = False
    found = re.search(r"[a-z]+", data)
    if found:
        found = re.search(r"[A-Z]+", data)
        if found:            
            found = re.search(r"[0-9]+", data)
            if found:
                flag = True
    return flag

#Some hints
#Just check all conditions


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio('A1213pokl') == False, "1st example"
    assert checkio('bAse730onE4') == True, "2nd example"
    assert checkio('asasasasasasasaas') == False, "3rd example"
    assert checkio('QWERTYqwerty') == False, "4th example"
    assert checkio('123456123456') == False, "5th example"
    assert checkio('QwErTy911poqqqq') == True, "6th example"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")