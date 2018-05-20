n = 5
a = '1'
if n == 1:
    print(a)
else:
    for i in range(2, n + 1):
        if i == 2:
            a = '11'
        else:
            count = 1
            for j in range(len(a) - 1):
                if j == len(a) - 2 :
                    if a[j] == a[j + 1]:
                        count += 1
                        a = a + count + a[j]
                    else:

                elif a[j] == a[j + 1]:
                    count += 1
                    print(a)
                else:
                    a = a + count + a[j]
                    count = 1
                    print(a)

