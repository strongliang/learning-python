def isPalindrome(str):
    if len(str) == 1:
        return True
    elif len(str) == 2 and str[0] == str[-1]:
        return True
        
    elif str[0] != str[-1]:
        return False
    else:
        print str[1:-1]
        return isPalindrome(str[1:-1])
        
print isPalindrome("abba")