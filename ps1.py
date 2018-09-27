
row, col = input().split()
#print (row,col)
s = []
for i in range(int(row)):
    str = input()
    s.append(str)

count = 0
num = 1
flag = 0

maxlist = []

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

# if flag == 1:
#     maxlist.append(count*4 + 1)

max1 = 0
max2 = 0

for i in range(len(maxlist)):
    if maxlist[i] >= max1:
        max2 = max1
        max1 = maxlist[i]

print (max1, max2)


#print (s)
