
from time import time
from functools import wraps
from inspect import isfunction, isclass

def profile(obj):
    def profile_func(func):
        @wraps(func)
        def function(*args, **kwargs):
            print(f'`{func.__qualname__}` started')
            timer = time()
            result = func(*args, **kwargs)
            print('`%s` finished in %f'% (func.__qualname__, time() - timer))
            return result
        return function

    def profile_class(klass):
        for attr_name in klass.__dict__:
            attr = getattr(klass, attr_name)
            if callable(attr):
                setattr(klass, attr_name, profile_func(attr))
        return klass

    if isfunction(obj):
        return profile_func(obj)
    elif isclass(obj):
        return profile_class(obj)

@profile
def foo():
    pass

@profile
class Bar:
    def __init__(self):
        pass

if __name__ == "__main__":
    foo()
    Bar()