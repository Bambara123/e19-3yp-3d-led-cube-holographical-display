myArray = [1,4,3,1,3,5,2,3,1,2,1,4,5,3,5,8,1,3,6]

new  = []

for x in range(len(myArray)):
    for y in range(x,len(myArray)):
        if myArray[x] + myArray[y] == 6:
            new.append([x,y])

print()
        

