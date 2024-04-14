def do_twice(func):
    def wrapper_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)
    return wrapper_do_twice

    

@do_twice
def say_whee():
    print("Wheeeee!")

#say_whee()

do_twice(say_whee())