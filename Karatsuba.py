import time

def karatsuba(x, y):
    # Base case for recursion
    if x < 10 or y < 10:
        return x * y

    # Calculate the size of the numbers
    n = max(len(str(x)), len(str(y)))
    m = n // 2

    # Split the numbers into halves
    high1, low1 = divmod(x, 10**m)
    high2, low2 = divmod(y, 10**m)

    # 3 recursive calls made to numbers approximately half the size
    z0 = karatsuba(low1, low2)
    z1 = karatsuba((low1 + high1), (low2 + high2))
    z2 = karatsuba(high1, high2)

    return (z2 * 10**(2*m)) + ((z1 - z2 - z0) * 10**m) + z0

# Input large integers
a = int(input("Enter the first large integer: "))
b = int(input("Enter the second large integer: "))

# Standard multiplication
start_time_standard = time.time()
standard_result = a * b
end_time_standard = time.time()
time_standard = end_time_standard - start_time_standard

# Karatsuba multiplication
start_time_karatsuba = time.time()
karatsuba_result = karatsuba(a, b)
end_time_karatsuba = time.time()
time_karatsuba = end_time_karatsuba - start_time_karatsuba

# Compare results and print if they are the same
print("Karatsuba result:", karatsuba_result)
print("Standard multiplication result:", standard_result)
print("Are both results the same? ", karatsuba_result == standard_result)

# Print the time taken by each method
print(f"Time taken by standard multiplication: {time_standard:.10f} seconds")
print(f"Time taken by Karatsuba multiplication: {time_karatsuba:.10f} seconds")
 