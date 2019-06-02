#! /usr/local/bin/python3


def main():
    fruits = ['grape', 'raspberry', 'apple', 'banana']
    print(sorted(fruits))
    # ['apple', 'banana', 'grape', 'raspberry']
    print(sorted(fruits, reverse=True))
    # ['raspberry', 'grape', 'banana', 'apple']
    print(sorted(fruits, key=len))
    # ['grape', 'apple', 'banana', 'raspberry']
    print(sorted(fruits, key=len, reverse=True))
    # ['raspberry', 'banana', 'grape', 'apple']
    fruits = ['grape', 'raspberry', 'apple', 'banana']
    print(fruits.sort())
    # None
    print(fruits)
    # ['apple', 'banana', 'grape', 'raspberry']


if __name__ == "__main__":
    main()
