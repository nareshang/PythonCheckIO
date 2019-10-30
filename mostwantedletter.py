from collections import Counter
import re

def checkio(text: str) -> str:
    alphastr = re.findall("[a-zA-Z]+", text)
    charlist = [ch for word in alphastr for ch in word.lower()]
    countchar = Counter(charlist)
    mostcommon = countchar.most_common()    
    wantedchar = None
    
    l = len(mostcommon)    
    if (l == 0):
        return wantedchar

    if (l == 1):
        wantedchar = mostcommon[0][0]
    elif (l > 1) and (mostcommon[0][1] == mostcommon[1][1]):
        commonkeys = [k for k,v in mostcommon if v == mostcommon[0][1]]
        sortedkeys = sorted(commonkeys)
        wantedchar = sortedkeys[0]
    else:
        wantedchar = mostcommon[0][0]
    
    return wantedchar

if __name__ == '__main__':
    print("Example:")
    print(checkio("Hello World!"))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("Hello World!") == "l", "Hello test"
    assert checkio("How do you do?") == "o", "O is most wanted"
    assert checkio("One") == "e", "All letter only once."
    assert checkio("Oops!") == "o", "Don't forget about lower case."
    assert checkio("AAaooo!!!!") == "a", "Only letters."
    assert checkio("abe") == "a", "The First."
    print("Start the long test")
    assert checkio("a" * 9000 + "b" * 1000) == "a", "Long."
    print("The local tests are done.")