#! /usr/local/bin/python3

# install numpy on MacOS / IntelliJ:
# $ pip3 install numpy
# IntelliJ -> Project Structure -> SDKs / Packages (+) -> Search / InstallPackage "numpy"

import numpy

from time import perf_counter as pc


def basic_operate():
    a = numpy.arange(12)
    print(a)
    # array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11])
    print(type(a))
    # <class 'numpy.ndarray'
    print(a.shape)
    # (12,)
    a.shape = 3, 4
    print(a)
    # array([[ 0,  1,  2,  3],
    #        [ 4,  5,  6,  7],
    #        [ 8,  9, 10, 11]])
    print(a[2])
    # array([ 8,  9, 10, 11])
    print(a[2, 1])
    # 9
    print(a[:, 1])
    # array([1, 5, 9])
    print(a.transpose())
    # array([[ 0,  4,  8],
    #        [ 1,  5,  9],
    #        [ 2,  6, 10],
    #        [ 3,  7, 11]])


def operate():
    floats = numpy.loadtxt('ndarray.txt')
    print(floats[-3:])
    # array([ 3016362.69195522,   535281.10514262,  4566560.44373946])
    floats *= .5
    print(floats[-3:])
    # array([ 1508181.34597761,   267640.55257131,  2283280.22186973])
    t0 = pc()
    floats /= 3
    print(pc() - t0)
    # 0.03690556302899495
    numpy.save('ndarray', floats)
    floats2 = numpy.load('ndarray.npy', 'r+')
    floats2 *= 6
    print(floats2[-3:])
    # memmap([ 3016362.69195522,   535281.10514262,  4566560.44373946])


def main():
    basic_operate()
    print()
    operate()


if __name__ == "__main__":
    main()
