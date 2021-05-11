#given a string, write a program to check whether its a permutation of a palindrome

def findIfPermutationOfPalindrome(ipString):
    ct = 0
    hmap = {}
    for _ in ipString:
        if(_!=' '):
            if(_ not in hmap):
                hmap[_] = 1
            else:
                hmap[_] = (hmap[_] + 1) %2

    for k,v in hmap.items():
        if(v==1):
            ct+=1
        if(ct>1):
            return -1
    if(ct==1 or ct==0):
        return 1


ipString = input()
print(findIfPermutationOfPalindrome(ipString))
