x = -321
y = abs(x)
res = 0
while y != 0:
    tmp = y % 10
    res = res * 10 + tmp
    y //= 10
resres = (res if x>=0 else -res)
if resres > (2**31 -1) or resres < (-2**31):
    print(0)
else:
    print(resres)


