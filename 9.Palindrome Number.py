def isPalindrome( x):
    """
    :type x: int
    :rtype: bool
    """
    tmp = x
    if x<0:
        return False
    else:
        rev = 0
        while x != 0:
            rev = rev * 10 + x %10
            x //= 10
        if tmp == rev:
            return True
        else:
            return False

if __name__ == '__main__':
    print(isPalindrome(-121))