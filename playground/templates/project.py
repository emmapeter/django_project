import random

# Number of lists to generate
x = int(input("Enter the limit for Fibonacci Series: "))
num_lists = x

# Number of random numbers in each list
num_numbers_in_list = 5

# List to store the generated lists
generated_lists = []

# Generate the lists
for _ in range(num_lists):
    random_list = [random.randint(1, 100) for _ in range(num_numbers_in_list)]
    generated_lists.append(random_list)

# Print the generated lists
for i, random_list in enumerate(generated_lists, 1):
    print(f"Fibonacci Series {i}: {random_list}")



# Resuit 
import random

#number of random number in five
y =  2

# Number of random numbers in each list
num_numbers_in_list = 5

# List to store the generated lists
generated_lists_five = []

# Generate the list_five
for _ in range(2):
    random_list_five = [random.randint(1, 99) for _ in range(num_numbers_in_list)]
    generated_lists_five.append(random_list_five)

# Print the generated lists
for i, random_list_five in enumerate(generated_lists_five, 1):
    random.shuffle(random_list)

    print(f"Resiut -->>>> {i}: {random_list}")
