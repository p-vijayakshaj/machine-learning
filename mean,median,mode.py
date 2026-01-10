import random
list1  = []
n = 25
sum =0
for i in range(n):
  list1.append(random.randint(1,10))
  sum= sum + list1[i]
  mean = sum/ n

new_list = sorted(list1)
dictionary = {}
for i in list1:
  if i in dictionary:
    dictionary[i] = dictionary[i] +1
  else:
    dictionary[i] =1
mode = max(dictionary,key = dictionary.get)

if n % 2 != 0:          # odd number of elements
    median = new_list[n // 2]
else:                   # even number of elements
    median = (new_list[n // 2 - 1] + new_list[n // 2]) / 2
print(list1)
print(new_list)
print("mean",mean)
print("mode",mode)
print("median",median)
