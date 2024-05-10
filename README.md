# Performance Testing

## Program 1: Timers

### Description

A simple and effective way to measure the performance of a program is to use timers. In this program, you will use the `time` module to measure the time it takes to execute a two implementations of a program.

When using a sample size we usually refer to the number of samples in the format `n=1`, `n=10`, etc.

### Instructions

1. Open the timers.py file.
2. Read through the file and do your best to interpret the code.
3. Run the program several times and observe the output.
4. Change the NUMBER_OF_TESTS constant to 1000 and run the program again.

Answer the following questions:

- For both your n=1 and n=1000 scenarios:
   - What is the percentage difference in the average time between the two implementations? You may use the following formula to calculate the percentage difference: `((original_time - new_time) / new_time) * 100`.
   - Express this difference verbally, e.g. "Implementation x is 10% faster/slower than Implementation x."
- Is there greater variation in the average time with the smaller or larger number of tests?
- What does this tell you about how sample size affects the reliability of performance measurements?

Submit your answers in a text file named "timers_analysis.txt".

## Program 2: Performance Profiling

Performance profiling is a technique used to measure certain aspects of a program's performance such as the time spent in specific function calls, or the amount of memory it uses. In this program, you will use the `cProfile` module to profile the performance of a program.

### Instructions

1. Open the profiling.py file.
2. Read through the file and do your best to interpret the code.
3. Install the numpy package using the pip package manager. You can do this by entering the following command in the terminal: `pip install numpy`
4. Execute the code. Observe the following in the output for the rows where the line number is 20 and 26:
   1. ncalls: the number of times the function was called.
   2. tottime: the total time spent in the function over the life of the program.

Answer the following questions regarding other_function1 and other_function2:

- Which function takes longer to execute a single time? See the comments on lines 21 and 28.
- How much time did the program spend in each function over the life of the program?
- Based on this data, which of the two functions should we focus on optimizing (trying to reduce execution time of the function call), and why?

Submit your answers in a text file named "profiling_analysis.txt".
