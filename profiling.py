'''
In this example we use a profiler to analyze the performance of the program as a whole.
We want to identify where the program is spending most of its time.
'''
import cProfile
import numpy as np
import time


def call_functions(arr):
    for val in arr:
        if val < 10:
            function1()
        else:
            function2()
    return None


# Simulate doing some work.
def function1():
    # It takes .2ms to complete this function
    time.sleep(0.002)
    return None


# Simulate doing some work.
def function2():
    # It takes .3ms to complete this function
    time.sleep(0.003)
    return None


# Simulate a real dataset for the application
data = np.random.gamma(2.0, 2.0, 10000)
data = np.clip(data, None, 20)

## ###############################################################
## Run the test
## ###############################################################

# Profile the function call
cProfile.run("call_functions(data)")
