l =[1,2,3,4,5]
l1 = [4,5,7,8,9]
new_l = []
for i in l:
  if i%2 != 0:
    new_l.append(i)
for j in l1 :
  if j%2 == 0:
    new_l.append(j)


print(new_l)
