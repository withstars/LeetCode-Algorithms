s = "0P"
a = []
for i in range(len(s)):
    tmp = ord(s[i])
    if tmp>=97 and tmp<=122 :
        a.append(s[i])
    elif tmp>=65 and tmp<=90:
        a.append(chr(tmp+32))
    elif tmp >= 48 and tmp <= 57:
        a.append(s[i])
aLen = len(a)
flag = True
for i in range(aLen//2):
    if(a[i] != a[aLen-i-1]):
        flag = False
        break
print(flag)




