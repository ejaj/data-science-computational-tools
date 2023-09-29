import numba
import time

# Define a function to compute the sum using numba
@numba.jit
def compute_sum_n(n):
    result = 0.0
    for i in range(1, n + 1):
        result += 1.0 / (i * i)
    return result

# Set the number of times to run the calculation
num_iterations = 2000

# Set the value of n
n = 10000

# Measure the execution time
start_time = time.time()

# Run the calculation num_iterations times
for _ in range(num_iterations):
    result = compute_sum_n(n)

# Calculate the average result
average_result = result / num_iterations

# Print the average result
print(f"Average Result for n = {n}: {average_result:.4f}")

# Print the execution time
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution Time: {execution_time:.4f} seconds")
