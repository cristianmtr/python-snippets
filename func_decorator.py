def decorate(decorator):
    print 'decorator is {}'.format(decorator)
    def wrapper(func):
        print 'func name is {}'.format(func.__name__)
        def actual_decorator(name):
            print 'argument name for func is {}'.format(name)
            return "{0}{1}{0}".format(decorator, func(name))
        return actual_decorator
    return wrapper

@decorate("<p>")
def get_text(name):
    return "Hello {0}".format(name)

print get_text("John")
