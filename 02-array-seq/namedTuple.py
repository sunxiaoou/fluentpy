#! /usr/local/bin/python3

from collections import namedtuple


def main():
    City = namedtuple('City', 'name country population coordinates')
    tokyo = City('Tokyo', 'JP', 36.933, (35.689722, 139.691667))
    print(tokyo)
    # tokyoCity(name='Tokyo', country='JP', population=36.933, coordinates=(35.689722,139.691667))
    print(tokyo.population)
    # 36.93
    print(tokyo.coordinates)
    # (35.689722, 139.691667)
    print(tokyo[1])
    # 'JP'

    print(City._fields)
    # ('name', 'country', 'population', 'coordinates')

    LatLong = namedtuple('LatLong', 'lat long')
    delhi_data = ('Delhi NCR', 'IN', 21.935, LatLong(28.613889, 77.208889))
    delhi = City._make(delhi_data)
    print(delhi._asdict())
    # OrderedDict([('name', 'Delhi NCR'), ('country', 'IN'), ('population',21.935),
    #  ('coordinates', LatLong(lat=28.613889, long=77.208889))])
    for key, value in delhi._asdict().items():
        print(key + ':', value)


if __name__ == "__main__":
    main()
