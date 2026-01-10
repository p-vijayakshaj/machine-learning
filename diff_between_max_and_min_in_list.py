list1 = list(map(float,input("enter more than 3 numbers").split()))

if len(list1) < 3:
  print("range determination is not possible")
else: 
 maxi = list1[0]
 mini =list1[0] 
 for i in range(len(list1)):
   if list1[i] > maxi:
     maxi = list1[i]

 for j in range(len(list1)):
   if list1[j] < mini:
    mini = list1[j]
 diff = maxi - mini
 print("difference between the maximun and minimum in the list is",diff)
