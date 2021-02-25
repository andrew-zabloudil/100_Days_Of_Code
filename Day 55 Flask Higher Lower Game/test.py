def logging_decorator(function):
    def wrapper(*args, **kwargs):
        print(f"\nCalled {function.__name__}")
        print(f"Arguments given: {args}")
        print(f"Kw Args given: {kwargs}\n")
        function(*args, **kwargs)
    return wrapper


@logging_decorator
def test_function(text):
    print(text)


@logging_decorator
def test_function_2(text, number):
    print(text)
    print(number)


@logging_decorator
def test_function_3(text="Hello", number=12):
    print(text)
    print(number)


test_function("Test")
test_function_2("Test", 12)
test_function_3(text="Test", number=24)
