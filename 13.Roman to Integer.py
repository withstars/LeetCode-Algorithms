s = "MCMXCIV"
romans = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
a = []
b = []
res = 0
for i in range(len(s)-1):
    b.append(i)
    if(romans[s[i]] < romans[s[i+1]]):
        res += romans[s[i+1]] - romans[s[i]]
        a.append(i)
        a.append(i+1)
b.append(len(s)-1)
for i in b:
    if i not in a:
        res += romans[s[i]]
print(res)




