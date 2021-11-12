from threading import Thread, active_count, main_thread, current_thread
from os import getpid
from time import sleep

def threadName():
    sleep(2)
    print(f"This is thread: {current_thread().name}")


if __name__ == "__main__":
    print("ID of process running main program:", getpid()) 

    th = Thread(target = threadName, name = "th")
    th.start()

    print("Current thread count = ", active_count())
    print(f"Thread {th.getName()} is {th.is_alive()}")
    print()

    th.join()

    print()
    print(f"Thread {th.getName()} is {th.is_alive()}")
    print("Current thread count = ", active_count())
    print()

    print(f"Main thread's name = {main_thread().name}")
    print(f"Current thread's name in main = {current_thread().name}")