myList = [23,43,56,12,34,96,45,54,56,76]

length = len(myList)

i = 0
max = 0
while i < 10 :
    if myList[i] > max:
        max = myList[i]
    i += 1
print ("Maximum number is : ", max)