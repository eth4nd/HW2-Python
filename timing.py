import time
def calculate_time(func):
    """
    A decorator that calculates the time to run a function.
    """
    def wrapper():
        """
        Wraps the function to extend behavior of wrapped function.
        """
        x  = time.time()
        func()
        new_time = time.time()
        x = new_time - x
        print(f'Total time {x}')
    return wrapper

@calculate_time
def time_sleep():
    """
    Suspends execution for a specified number of seconds. 
    """
    time.sleep(2)
