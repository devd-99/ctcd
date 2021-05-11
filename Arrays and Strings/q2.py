#implement an algo to find out whether one provided string is a permutation of another
#EXTRA: Implement an n log(n) sorting algo

def checkPermutation(s1, s2):
    s1 = sorted(s1.lower())
    s2 = sorted(s2.lower())
    if s1 == s2:
        return 1
    else:
        return -1



s1 = input()
s2 = input()
print(checkPermutation(s1, s2))