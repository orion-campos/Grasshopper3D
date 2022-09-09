numbers = [2, 5, 3, 2, 2]

newList = []
sumN = 0
for n in range(len(numbers)):
 sumN += numbers[n]
 newList.append(sumN)
print(newList)

new_list = []
for i in range(len(numbers)):
 new_list.append(numbers[i] + sum(numbers[:i]))
print(new_list)

output = [numbers[i]+sum(numbers[:i]) for i in range(len(numbers))]
print(output)

new_list = []
for i in range(len(numbers)):
 new_list.append(numbers[i] + numbers[i-1])
print(new_list)

new_list = []
for i in range(len(numbers)):
 if i > 0:
    new_list.append(numbers[i] + numbers[i-1])
 else:
    new_list.append(numbers[i])
print(new_list)
 
output = [numbers[i]+numbers[i-1] if i > 0 else numbers[i] for i in range(len(numbers))]
print(output)
