import time


def execution_time(function):
    def wrapper_function():
        begin = time.time()
        function()
        end = time.time()
        print(f"{function.__name__} executed in {end - begin} seconds.")
    return wrapper_function


@execution_time
def fast_function():
    for i in range(10000000):
        i * i


@execution_time
def slow_function():
    for i in range(100000000):
        i * i


fast_function()
slow_function()
