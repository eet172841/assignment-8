# scan row and col
row, col = input().split()
# scan the input
s = []
for i in range(int(row)):
    str = input()
    s.append(str)
# var to store various counts
count = 0
num = 1
flag = 0

maxlist = []
# scan the string and check for valid plus
for i in range(int(row)):
    for j in range(int(col)):
        flag = 0
        if s[i][j] == 'S':
            flag = 1
            num = 1
            count = 0
            while i - num >= 0 and i + num < int(row) and j - num >= 0 and j + num < int(col) and s[i-num][j] == 'S' and s[i][j-num] == 'S' and s[i+num][j] == 'S' and s[i][j+num] == 'S':
                    count += 1
                    num += 1
        if flag == 1:
            maxlist.append(count*4 + 1)
# max1 and max2 for 2 largest
max1 = 0
max2 = 0
# find two largest

if (len(maxlist) == 0):
    print("0 0")
else:
    for i in range(len(maxlist)):
        if maxlist[i] >= max1:
            max2 = max1
            max1 = maxlist[i]
    print (max1, max2)
#
#
# zeros = []
#
# for i in range(int(row)):
#     for j in range(int(col)):
#         zeros = [0] * col
#
# limit = 0
#
# if (len(maxlist) == 0):
#     print("0 0")
# else:
#     for i in range(len(maxlist)):
#         if maxlist[i] > max1:
#             max1 = maxlist[i]
#     limit = range[i]
#     x = index[i][0]
#     y = index[i][1]
#     zeros[x][y] = 1
#     while limit > 0:
#          zeros[x+limit][y] = 1
#          zeros[x][y+limit] = 1
#          zeros[x-limit][y] = 1
#          zeros[x][y-limit] = 1
#          limit -= 1
#
#
# #print (index)
