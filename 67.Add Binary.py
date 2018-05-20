a = "10110"
b = "1011"
aLen = len(a)
bLen = len(b)
aTen = 0
bTen = 0
for i in range(aLen):
    mi=aLen-i-1
    aTen += int(a[i]) * (2**mi)
for i in range(bLen):
    mi=bLen-i-1
    bTen += int(b[i]) * (2**mi)
c = aTen + bTen
res =c
result = ""
while res!=0:
    mo = res % 2
    res =res // 2
    result = str(mo) + result
print(result)


