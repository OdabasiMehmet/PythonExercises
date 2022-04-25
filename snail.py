array = [[1,2,3],
         [4,5,6],
         [7,8,9]]
#snail(array) #=> [1,2,3,6,9,8,7,4,5]


snail=[]
for i in array[0]:
    snail.append(i)
snail.append(array[1][2])
for i in array[2][::-1]:       
    snail.append(i)
for i in array[1][:2]:       
    snail.append(i)
print(snail)