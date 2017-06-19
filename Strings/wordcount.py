def wordcountFromString():
    lp = "apple banana grapes banana kiwi orange banana kiwi"
    counter = 0
    for word in lp.split():
        counter += 1
    print("Word Count is", counter)
    return

import collections


def wordcountFromArrays():
    fruits = ["apple", "banana", "grapes", "banana",
              "kiwi", "orange", "banana", "kiwi"]
    counter = collections.Counter(fruits)
    print(counter)
    return


def wordCountUsingLoopsDict():
    countfruit = []
    fruits = ["apple", "banana", "grapes", "banana",
              "kiwi", "orange", "banana", "kiwi"]
    countfruit = [fruits.count(fruit) for fruit in fruits]
    print "Fruit and count in dict", dict(zip(fruits, countfruit))
    return


def main():
    wordcountFromString()
    wordcountFromArrays()
    wordCountUsingLoopsDict()

if __name__ == "__main__":
    main()
