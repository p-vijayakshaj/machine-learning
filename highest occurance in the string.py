list1 = input("enter a string")
dictionary ={}
for i in list1:
  if i.isalpha(): # only if we want input pf alphabets
   if i in dictionary:
     dictionary[i] = dictionary[i]+1
   else:
    dictionary[i] =1

high_occurance = max(dictionary,key = dictionary.get)

print("highest occured letter is :",high_occurance)
