strs = ["flower","flow","flight"]
length = len(strs)
if length ==0:
    print("")
res = ""
flag = 0
strMinLength = len(strs[0])
for i in range(length):
    if (len(strs[i]) < strMinLength):
        strMinLength = len(strs[i])
for j in range(strMinLength):
    tmp = strs[0][j]
    for x in range(length):
        if tmp != strs[x][j]:
            flag =1
            break
    if flag == 1:
        break
    res += tmp
print(res)
