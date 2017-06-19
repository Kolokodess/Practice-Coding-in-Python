def stringmanipulations():
    lp = " Lorem Ipsum is a dummy text of printing      industry since 1950's "
    print lp
    print("Character at index 0 of String", lp[0])
    print("Character at index 1 of String", lp[1])
    print("Reversed String", lp[::-1])
    print("Starting 0 to position 5 excluded", lp[:5])
    print("Starting 5 to end included", lp[5:])
    print("Characters from 3rd last included to the end", lp[-3:])
    print("Length of String", len(lp))
    print(
        "Alternate Characters in the String from start to the end, jump 2 strings start to end",
        lp[::2])
    print(
        "Alternate Characters in the Reverse String from end to the start",
        lp[::-2])
    print("Fruit 5 times", 'Fruit'*5)
    print("Append Fruit 5 times to the Character at substring of Lp Starting from 0 to 5th character",
          'Fruit'+lp[:6])
    return


def main():
    stringmanipulations()

if __name__ == "__main__":
    main()
