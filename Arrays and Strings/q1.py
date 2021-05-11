# o(s)
def checkUnique(s):
    a={}
    for _ in s:
        if _ in a:
            return -1
        else:
            a[_] = 1

    return 1

# o(s log(s))
def checkUniqueWithoutHashMap(s):
    sortedString = sorted(s.lower())
    for i in range(len(sortedString)-1):
        if sortedString[i]==sortedString[i+1]:
            return -1
    return 1


# implement algo to find out whether all chars in a string are unique firstly anyhow secondly without extra data structures
s= input()
print(checkUnique(s))
print(checkUniqueWithoutHashMap(s))