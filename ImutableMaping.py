from collections.abc import Mapping

class ImmutableMap(Mapping):
    def __init__(self, *args, **kwargs):
        self._data = dict(*args, **kwargs)

    def __getitem__(self, key):
        return self._data[key]

    def __iter__(self):
        return iter(self._data)

    def __len__(self):
        return len(self._data)

    def __contains__(self, key):
        return key in self._data

    def __repr__(self):
        return f'ImmutableMap({repr(self._data)})'

    
    def keys(self):
        return self._data.keys()

    def values(self):
        return self._data.values()

    def items(self):
        return self._data.items()

    
    def __setitem__(self, key, value):
        raise TypeError("ImmutableMap object does not support item assignment")

    def __delitem__(self, key):
        raise TypeError("ImmutableMap object does not support item deletion")



if __name__ == "__main__":
    
    data = {'a': 3, 'b': 15, 'c': 6}
    imap = ImmutableMap(data)

    try:
        imap['d'] = 4
    except TypeError as e:
        print(f"Expected exception: {e}")

    try:
        del imap['a']  
    except TypeError as e:
        print(f"Expected exception: {e}")

    
    assert len(imap) == 3
    assert set(imap.keys()) == {'a', 'b', 'c'}
    assert set(imap.values()) == {3,15,6}
    assert set(imap.items()) == {('a', 3), ('b', 15), ('c', 6)}


    for key, value in imap.items():
        print(f"{key}: {value}")
