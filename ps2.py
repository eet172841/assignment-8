
# for all 3 rotations
k1, k2, k3 = input().split()
str = input()
# separating the characters
first = []
second = []
third = []
for i in str:
    if ord(i) >= ord('a') and ord(i) <= ord('i'):
         first.append(i)
    elif ord(i) >= ord('j') and ord(i) <= ord('r'):
         second.append(i)
    else:
         third.append(i)

#Roatating the lists

first_r = (first[-int(k1):] + first[:-int(k1)])
second_r = (second[-int(k2):] + second[:-int(k2)])
third_r = (third[-int(k3):] + third[:-int(k3)])

ctr1 = 0
ctr2 = 0
ctr3 = 0

#printing the result

for i in str:
    if ord(i) >= ord('a') and ord(i) <= ord('i'):
         print(first_r[ctr1],end = '')
         ctr1 += 1
    elif ord(i) >= ord('j') and ord(i) <= ord('r'):
         print(second_r[ctr2],end = '')
         ctr2 += 1
    else:
         print(third_r[ctr3],end = '')
         ctr3 += 1
