from wrapper_module import my_decorator


@my_decorator
def just_some_function():
    print "Wheee!"

just_some_function()
