import random

# Generate 5 random floating-point numbers
numbers = [random.uniform(0, 10) for _ in range(5)]

# Calculate minimum and maximum
minimum = min(numbers)
maximum = max(numbers)

# Display the results
print("Random numbers:", numbers)
print("Minimum value:", minimum)
print("Maximum value:", maximum)
