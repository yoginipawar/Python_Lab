#Convert the below list into a numpy array then display the array then display the first and last index and then multiply each element by 2 and display the result.
#Input: my_list = [1, 2, 3, 4, 5]

import numpy as np

# Create the list
my_list = [1, 2, 3, 4, 5]

# Convert the list to a NumPy array
my_array = np.array(my_list)

# Display the array
print("Array:", my_array)

# Get the first and last indices
first_index = my_array[0]  # Access the first element using index 0
last_index = my_array[-1]  # Access the last element using negative indexing

# Display the first and last indices
print("First index:", first_index)
print("Last index:", last_index)

# Multiply each element by 2
doubled_array = my_array * 2

# Display the doubled array
print("Doubled array:", doubled_array)

#OUTPUT
Array: [1 2 3 4 5]
First index: 1
Last index: 5
Doubled array: [ 2  4  6  8 10]
