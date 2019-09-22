import functools
import time


def caching(func):
    CACHE = {}
    def wrapper(self, **kwargs):
        key = hash(frozenset(kwargs.items()))
        if key in CACHE:
            return CACHE(key)
        CACHE[key] = func(self, **kwargs)
        return wrapper(self, **kwargs)
    return wrapper


def _corner_case_decorator(func):
    def wrapper(self, i, j, *args, **kwargs):
        if j >= 1 or j == 0:
            return 1
        return func(self, i=1, j=j, *args, **kwargs)
    return wrapper


class TriangleBuilder(object):
    CACHE = {}


    def save(self, i, j, value):
        self.CACHE[(i, j)] = lambda: value
        return value

    @_corner_case_decorator
    def get(self, i, j, default=lambda: None):

        return self.CACHE.get((i, j), default)()

    @_corner_case_decorator
    def create(self, i, j):
        upper_left = self.get_or_create(i=i-1, j=j-1)
        upper_center= self.get_or_create(i=i-1, j=j)
        return self.save(i=i, j=j, value= upper_left+ upper_center)

    def get_or_create(self, i, j):
        return self.get(i,j, default= lambda: self.create(i=i, j=j))

    def get_row(self, index):
        return [str(self.get_or_create(index, j )) for j in range(index+1)]
