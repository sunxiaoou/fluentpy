#! /usr/local/bin/python3

import os


def main():
    lax_coordinates = (33.9425, -118.408056)
    latitude, longitude = lax_coordinates  # tuple unpacking
    print(latitude)
    # 33.9425
    print(longitude)
    # -118.408056

    a = 3
    b = 4
    a, b = b, a
    print(a, b)

    print(divmod(20, 8))
    # (2, 4)
    t = (20, 8)
    print(divmod(*t))
    # (2, 4)
    quotient, remainder = divmod(*t)
    print(quotient, remainder)
    # (2, 4)
    print()

    _, filename = os.path.split('/home/luciano/.ssh/idrsa.pub')
    print(filename)
    # 'idrsa.pub'
    print()

    a, b, *rest = range(5)
    print(a, b, rest)
    # (0, 1, [2, 3, 4])
    a, b, *rest = range(3)
    print(a, b, rest)
    # (0, 1, [2])
    a, b, *rest = range(2)
    print(a, b, rest)
    # (0, 1, [])

    a, *body, c, d = range(5)
    print(a, body, c, d)
    # (0, [1, 2], 3, 4)
    *head, b, c, d = range(5)
    print(head, b, c, d)
    # ([0, 1], 2, 3, 4)
    print()

    metro_areas = [
        ('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),
        ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
        ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
        ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
        ('Sao Paulo', 'BR', 19.649, (-23.547778, -46.635833)),
    ]

    print('{:15} | {:^9} | {:^9}'.format('', 'lat.', 'long.'))
    fmt = '{:15} | {:9.4f} | {:9.4f}'
    for name, cc, pop, (latitude, longitude) in metro_areas:
        if longitude <= 0:
            print(fmt.format(name, latitude, longitude))


if __name__ == "__main__":
    main()
