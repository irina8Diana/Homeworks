# Tema: Declaram o lista ce contine nr. si vrem sa-i facem suma elementelor din lista prin 4 metode.
# sa gasim duplicatele dintr-o lista. Sa afisam elemente care se gasesc de mai multe ori
# avem o lista cu nr si sa obtinem cel mai mare nr par
list1 = [1,2,3,4,2,2,1]
suma = 0
for i in list1:
    suma = suma + i
print(suma)

print ("The sum of my_list is", sum(list1))

s=[i for i in list1]
print(sum(s))

total=0
el = 0
while (el < len(list1)):
    total = total + list1[el]
    el+=1
print(total )

res = {}
#find duplicates
for i in list1:
    res[i] = list1.count(i)
print (res)