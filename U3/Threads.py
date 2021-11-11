# Number of threads on interactive kernels like jupyter would likely be higher
from threading import Thread, active_count, main_thread
from time import sleep

def threadName():
    sleep(2)
    print("This is thread")

if __name__ == "__main__":
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