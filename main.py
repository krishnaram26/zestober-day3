# myNum = input() # takes input
# listOfNums = list(map(int, myNum)) # converts to list
# reversedList = listOfNums[::-1] # reverses the list
# print(*reversedList) # prints reversed list (without brackets)

num = int(input())

res = []
while num:
  temp = num % 10
  res.append(temp)
  num = num // 10

print(*res)
