# hard
number = ["1", "2", "3", "4", "5"]
print(number)  # ['1', '2', '3', '4', '5']
for i in range(len(number)):
    number[i] = int(number[i])
print(number)  # [1, 2, 3, 4, 5]

numberLst = ["1", "2", "3", "4", "5"]
print(number)  
newNumberLst =list(map(int,number))
print(newNumberLst)  

map()
