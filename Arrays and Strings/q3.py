from queue import Queue
#write algo to replace all spaces in a string with %20. Extra space will be given at the end of the string
#use queue to maintain a list of characters you have to add. if i>n, discard spaces
ipString = input("enter ip: ")
charArray = []
for _ in ipString:
    charArray.append(_)
actualSize = int(input("enter actual size: "))
q = Queue()
i=0
while i < len(charArray):
    print(i)

    if q.empty():
        if charArray[i] == ' ':
            if(charArray[i+1]==' ' and i+1 < actualSize):
                q.put(charArray[i+1])
            elif(charArray[i+1]!=' '):
                q.put(charArray[i+1])

            if(charArray[i+2]==' ' and i+2 < actualSize):
                q.put(charArray[i+2])
            elif(charArray[i+2]!=' '):
                q.put(charArray[i+2])

            charArray[i] = '%'
            charArray[i+1] = '2'
            charArray[i+2] = '0'
            i+=3
        else:
            i+=1
            
    else:
        temp = q.get()
        if temp != ' ':
            if(charArray[i]==' ' and i<actualSize):
                q.put(charArray[i])
            elif(charArray[i]!=' '):
                q.put(charArray[i])

            charArray[i] = temp
            i+=1

        elif temp == ' ':
            if(charArray[i]==' ' and i<actualSize):
                q.put(charArray[i])
            elif(charArray[i]!=' '):
                q.put(charArray[i])
            charArray[i] = '%'

            if(charArray[i+1]==' ' and i+1 <actualSize):
                q.put(charArray[i+1])
            elif(charArray[i+1]!=' '):
                q.put(charArray[i+1])
            charArray[i+1] = '2'

            if(charArray[i+2]==' ' and i+2 <actualSize):
                q.put(charArray[i+2])
            elif(charArray[i+2]!=' '):
                q.put(charArray[i+2])
            charArray[i+2] = '0'

            i+=3

finalstr = ""
for _ in charArray:
    finalstr += _

print(finalstr)







