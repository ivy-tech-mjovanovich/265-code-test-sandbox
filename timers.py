'''
In this example, the program first sorts the data list using the built-in sorted function. 
Then, it attempts a premature optimization by implementing a more complex quicksort algorithm. 
The performance (time taken) of both approaches is measured, demonstrating that the premature 
optimization did not provide a significant benefit and may have even resulted in slower performance.
The program turned out to be prematurely optimized.
'''
import time
import random

NUMBER_OF_TESTS = 1


# Python has a built-in function to sort lists that is optimized for performance
def builtin_sort(arr):
    return sorted(arr)


# The quicksort algorithm is sometimes used as an optimization for sorting large datasets,
# but it is not always the best choice.
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)


# Initialize variables to store the total time taken for each approach
total_time_original = 0
total_time_optimized = 0

# Run the algorithm NUMBER_OF_TESTS times to get an average time span
for _ in range(NUMBER_OF_TESTS):

    # Generate a random dataset of 1000 elements for each test
    data = [random.randint(1, 1000) for _ in range(1000)]

    # Time the built-in sort function
    start_time = time.time()
    sorted_original = builtin_sort(data)
    end_time = time.time()
    total_time_original += (end_time - start_time)

    # Time the quicksort function
    start_time = time.time()
    sorted_optimized = quicksort(data)
    end_time = time.time()
    total_time_optimized += (end_time - start_time)

# Calculate the average time taken for each approach
average_time_original = total_time_original / NUMBER_OF_TESTS
print(f"Original sort: {average_time_original:.4f}ms")

average_time_optimized = total_time_optimized / NUMBER_OF_TESTS
print(f"Optimized sort: {average_time_optimized:.4f}ms")
