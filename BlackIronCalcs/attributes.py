#!/usr/bin/python3

from enum import Enum

class Attributes(Enum):
    HP = 0
    MP = 1
    STRENGTH = 2
    ENDURANCE = 3
    AGILITY = 4
    MAGIC = 5
    INTELLIGENCE = 6
    DEXTERITY = 7
    LUCK = 8


class AttributeList(object):

    def __init__(self, attrs):
        assert(isinstance(attrs, dict))
        for (key, value) in attrs.items():
            assert(isinstance(key, Attributes))
            assert(isinstance(value, int))
        self.attrs = attrs

    def __len__(self):
        return len(self.attrs)

    def __getitem__(self, attr):
        return self.attrs[attr]

    def __setitem(self, attr, value):
        assert(isinstance(attr, Attributes))
        assert(isinstance(value, int))
        self.attrs[attr] = value

    def __contains__(self, attr):
        return attr in self.attrs

    def __add__(self, other):
        assert(isinstance(other, AttributeList))
        new_attrs = {}
        for attr in Attributes:
            if (attr in self) and (attr in other):
                new_attrs[attr] = self[attr] + other[attr]
            elif (attr in self):
                new_attrs[attr] = self[attr]
            elif (attr in other):
                new_attrs[attr] = other[attr]
        return AttributeList(new_attrs)


