def strStr (haystack, needle):
    if haystack == "" or needle == "":
        return -1
    hLen = len(haystack)
    nLen = len(needle)
    a = hLen - nLen + 1
    flag = True
    index = -1
    for i in range(a):
        if haystack[i] != needle[0]:
            continue
        else:
            tmp = i
            for j in range(nLen-1):
                i += 1
                if needle[j+1] != haystack[i]:
                    flag = False
                    break
            if flag == True:
                index = tmp
                return index
        if flag == True:
            break
    return index
if __name__ == '__main__':
    print(strStr("hfaeello","ae"))
