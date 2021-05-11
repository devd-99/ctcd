ipStr = input()
current = ''
runstr = ""
cCount = 0
for char in ipStr:
    if current =='':
        cCount +=1
        current = char
        runstr+=char
        continue
    if char == current:
        cCount+=1
        continue
    if char!=current:
        runstr += str(cCount)
        cCount = 1
        runstr += char
        current = char
        continue
runstr += str(cCount)
print(runstr)