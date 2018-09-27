###### this is the second .py file ###########

####### write your code here ##########
import string
k1, k2, k3 = input().split()
str = input()
#print (k1,k2,k3)

first = []

for i in str:
    if ord(i) >= ord('a') and ord(i) <= ord('i'):
         first.append(i)

print (first)

# for c in range(ord('a'), ord('i')+1):
#     for i in range(len(str)):
#         if print (chr(c))
