from multiprocessing import Process, Array, Value

resultLocal = [] # Local to the current Process

def squareList(a, result, squareSum):
    for i, num  in enumerate(a):
        result[i] = num ** 2
        resultLocal.append(result[i])
    squareSum.value = sum(result)
    
    print("In Process P1")
    print(f"Shared Variable: {result[:]}")
    print(f"Local Variable: {resultLocal}")
    print("Sum of squares = ", squareSum.value)

if __name__ == "__main__":
    a = range(1, 6)
    result = Array('i', 5) # Shared between multiple Processes (ctypes object in shared memory)
    squareSum = Value('i') # Shared between multiple Processes (ctypes object in shared memory)
    p1 = Process(target = squareList, args = (a, result, squareSum), name = "P1")
    p1.start()
    p1.join()
    print("\nIn Main Process")
    print(f"Shared Variable: {result[:]}")
    print(f"Local Variable: {resultLocal}")
    print("Sum of squares = ", squareSum.value)