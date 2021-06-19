# File containing the class that handles threading operations
from multiprocessing import current_process
from time import sleep


def process_manager(func, queue, identifier, date, age):
    while True:
        response = func(identifier, date, age)
        queue.put(response)
        if response:
            break
        sleep(2)
