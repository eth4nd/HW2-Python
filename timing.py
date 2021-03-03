import time
def calculate_time(func):
    def wrapper():
        x  = time.time()
        func()
        new_time = time.time()
        x = new_time - x
        print(f'Total time {x}')
    return wrapper

@my_decorator
def time_sleep():
    func_sleep()
