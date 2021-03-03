import time
def calculate_time(func):
    def wrapper():
        currrent_time = time.time()
        func()
        new_time = time.time()
        x = new_time - current_time
        print(f'Total time {x}')
    return wrapper
