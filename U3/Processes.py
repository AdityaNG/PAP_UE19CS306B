from multiprocessing import Process

def cube(num):
    print(f"Cube of the given number if {num ** 3}")

def square(num):
    print(f"Square of the given number if {num ** 2}")

if __name__ == "__main__":
    p1 = Process(target = cube, args = (10,))
    p2 = Process(target = square, args = (2,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("Both processes finished")