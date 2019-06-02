#! /usr/local/bin/python3

import bisect


def grade(score, breakpoints=None, grades='FDCBA'):
    if breakpoints is None:
        breakpoints = [60, 70, 80, 90]
    i = bisect.bisect(breakpoints, score)
    return grades[i]


def main():
    grades = [grade(score) for score in [33, 99, 77, 70, 89, 90, 100]]
    print(grades)
    # ['F', 'A', 'C', 'C', 'B', 'A', 'A']


if __name__ == "__main__":
    main()
