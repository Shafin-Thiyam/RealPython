import functools
import time
import random

def do_twice(func):
    def wrapper_do_twice():
        func()
        func()
    return wrapper_do_twice

def do_twice_with_args(func):
    def wrapper_do_twice(oneargs):
        func(oneargs)
        func(oneargs)
    return wrapper_do_twice

def do_twice_with_dynamic_args(func):
    def wrapper_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)
    return wrapper_do_twice

def do_twice_with_dynamic_args_returns(func):
    @functools.wraps(func)
    def wrapper_do_twice(*args, **kwargs):
        #func(*args, **kwargs)
        return func(*args, **kwargs)
    return wrapper_do_twice

def shout(func):
    """Decorator that converts return values to uppercase."""
    @functools.wraps(func)
    def wrapper_do_shout(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.upper()
    return wrapper_do_shout


def dec2(func):
    """Decorator that converts return values to uppercase."""
    @functools.wraps(func)
    def wrapper_dec2(*args, **kwargs):
        # Do something before
        value = func(*args, **kwargs)
        return value
    return wrapper_dec2

def timer(func):
    """Print the runtime of the decorated function"""
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        # Do something before
        starttime = time.perf_counter()
        value = func(*args, **kwargs)
        endtime = time.perf_counter()
        runtime = endtime - starttime
        print(f"Finished {func.__name__!r} in {runtime:.4f} secs")
        return value
    return wrapper_timer



def debug(func):
    """Decorator that converts return values to uppercase."""
    @functools.wraps(func)
    def wrapper_debug(*args, **kwargs):
        # Do something before
        args_repr=[repr(a) for a in args]
        kargs_repr=[f"{k} = {v!r}" for k, v in kwargs.items()]
        signature = ",".join(args_repr+kargs_repr)
        print(f"calling {func.__name__} ({signature})")
        value = func(*args, **kwargs)
        print(f"{func.__name__!r} returned {value!r}")
        return value
    return wrapper_debug

def slowdown(func):
    """Decorator that converts return values to uppercase."""
    @functools.wraps(func)
    def wrapper_slowdown(*args, **kwargs):
        # Do something before
        time.sleep(3)
        return func(*args, **kwargs)
    return wrapper_slowdown

PLUGINS =dict()

def register(func):
    """Regist func as plugins."""
    PLUGINS[func.__name__] = func
    return func

def log_calls(func):
    """Decorator that logs calls to a function and its return value."""
    @functools.wraps(func)
    def wrapper_log_calls(*args, **kwargs):
        # Do something before
        args_repr=[repr(a) for a in args]
        kargs_repr=[f"{k} = {v!r}" for k, v in kwargs.items()]
        signature = ",".join(args_repr+kargs_repr)
        print(f"calling {func.__name__} ({signature})")
        value = func(*args, **kwargs)
        print(f"{func.__name__!r} returned {value!r}")
        return value
    return wrapper_log_calls
    