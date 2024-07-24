import random

# Create list of 100 random integers between 0-9
random_hundred = [random.randint(0, 9) for _ in range(100)]

# Create a dictionary object that stores the count of the number of times each of the numbers between  0 and 9 appear in the list
count_dictionary = {}
for x in random_hundred:
    if x in count_dictionary:
        count_dictionary[x] += 1
    else:
        count_dictionary[x] = 1
# Print dictionary information
print("Count of values:")
for x in range(10):
    if x in count_dictionary:
        print(f"{x}: {count_dictionary[x]}")
    else:
        print(f"{x}: 0")

# Create set of unique numbers from the list
unique_set = set(random_hundred)

# Print the length of the unique set
print(f"Length of set: {len(unique_set)}")