def simpleanagrams():
    str1 = "cinema"
    str2 = "iceman"
    if (list(str2)).sort() == (list(str1)).sort():
        print "%s and %s are anagrams" % (str1, str2)
    else:
        print "%s and % s are not anagrams" % (str1, str2)
    return


def anagramsUsingSets():
    str1 = "cinema"
    str2 = "iceman"
    if set(list(str1)).difference(set(list(str1))) == set():
        print "%s and %s are anagrams" % (str1, str2)
    else:
        print "%s and % s are not anagrams" % (str1, str2)
    return


def main():
    simpleanagrams()
    anagramsUsingSets()


if __name__ == "__main__":
    main()
