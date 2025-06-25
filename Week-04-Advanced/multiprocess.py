import multiprocessing

def square(n):
    return n**2
numbers = [3,4,5]

with multiprocessing.Pool(processes=3) as pool:
    results = pool.map(square, numbers)

print(results)    