def palindrome():
    lp = "kayak"
    if (lp == lp[::-1]):
        print "%s is a palindrome" % lp
    else:
        print "%s is not a palindrome" % lp
    return


def palindromeUsingLoop():
    lp = "kayakakaakkay"
    index = 0
    while index < len(lp)/2:
        if lp[index] != lp[-index-1]:
            print "%s is not a palindrome" % lp
            break
        index = index+1
    else:
        print "%s is a palindrome" % lp
    return


def main():
    palindrome()
    palindromeUsingLoop()

if __name__ == "__main__":
    main()
