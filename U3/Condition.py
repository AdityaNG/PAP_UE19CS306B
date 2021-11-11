from threading import Thread, Condition
from time import  sleep
from random import choice, random

queue = []
maxNum = 5
condition = Condition()

RED = "\033[91m"
GREEN = "\033[92m"
RESET = "\033[0m"
C1 = "\033[93m"
C2 = "\033[94m"
C3 = "\033[95m"

class Producer(Thread):
    def run(self):
        nums = range(5)
        global queue
        while True:
            num = choice(nums)
            condition.acquire()
            if len(queue) == maxNum: 
                print(f"{C1}Producer: {RED}Queue Full{RESET}")
                condition.wait() # Wait for Consumer to notify after it has consumed something and made room for new products in the queue
            queue.append(num)
            print(f"{C1}Producer: {C3}Produced {num}{RESET}")
            condition.notify() # Notify the consumer that a new product has been produced
            condition.release()
            sleep(random())

class Consumer(Thread):
    def run(self):
        global queue
        while True:
            condition.acquire()
            if not queue: 
                print(f"{C2}Consumer: {RED}Queue Empty{RESET}")
                condition.wait() # Wait for Producer to add something the queue
            num = queue.pop(0)
            print(f"{C2}Consumer: {GREEN}Consumed {num}{RESET}")
            condition.notify() # Notify the producer to add something to the queue
            condition.release()
            sleep(random())

Producer().start()
Consumer().start()               