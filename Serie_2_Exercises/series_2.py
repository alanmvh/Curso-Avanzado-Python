
# Exercise 1

# Creation of list
list1 = []

# For loop to append 100 elements in the list using the value of the counter as cell value
for i in range(1,101):
    # Appends the element i to list[i] position
    list1.append(i)

# Creating list2 using generated lists where (xi) is the element is the element contained inside list1
list2 = [xi ** 2 for xi in list1]

# Generating list with map function
# map - executes for each item a function 
# lambda - Anonymous function that is executed online, no declaration needed
list3 = list(map(lambda i:i**2,list1))

# Exercise 2

# Generating list from number 3-57 (1:1)
list_ex3 = [i for i in range(3,58)]

# List of cubed numbers of list_ex3 which are multiple of 3 - generated lists
list_ex3_cubed = [i ** 3 for i in list_ex3 if i % 3 == 0]

# List of cubed numbers of list_ex3 which are multiple of 3 - using filter function
list_ex3_cubed2 = list(map(lambda a: a ** 3, filter(lambda b:b % 3 == 0, list_ex3)))

# Excercise 3

# Generate a list with numbers 4-48(inclusive)
e4_list = [i for i in range(4,49)]

# Sum of all list elements if multiples of 4 = Output: 312 -> Generated lists
sum_generated_list = sum([i for i in e4_list if i % 4 == 0])

# Sum of all list elements if multiples of 4 = Output: 312 -> using Filter function
sum_filter = sum(list( filter(lambda b:b%4==0, e4_list)))

# Sum of all list elements if multiples of 4 = Output: 312 -> using reduce
from functools import reduce
sum_reduce = reduce(lambda a,b: a+b if (b%4==0) else a, e4_list)

# Time it section
import timeit

time_generated_list = timeit.repeat(
    # Code that we want to measure
    stmt="sum_generated_list = sum([i for i in e4_list if i % 4 == 0])",
    # Setup details that need to be executed before stmt
    setup="e4_list = [i for i in range(4,49)]",
    # Times stmt will be executed as per the number is given
    number=1,
    repeat=5
)

time_filter_function = timeit.repeat(
    # Code that we want to measure
    stmt="sum_filter = sum(list(filter(lambda b:b%4==0, e4_list)))",
    # Setup details that need to be executed before stmt
    setup="e4_list = [i for i in range(4,49)]",
    # Times stmt will be executed as per the number is given
    number=1,
    repeat=5
)

# list generated in stmt due to import error if 'from functools import reduce' not executed in setup
time_functools = timeit.repeat(
    # Code that we want to measure
    stmt="sum_reduce = reduce(lambda a,b: a+b if (b%4==0) else a, [i for i in range(4,49)])",
    # Setup details that need to be executed before stmt
    setup= "from functools import reduce",
    # Times stmt will be executed as per the number is given
    number=1,
    repeat=5
)

# Prints generated list execution time in miliseconds
print(f"Time for generated list: {(sum(time_generated_list))/(len(time_generated_list))/1e-6}")
# Prints filter function execution time in miliseconds
print(f"Time for filter function: {(sum(time_filter_function))/(len(time_filter_function))/1e-6}")
# Prints functools-reduce time in miliseconds
print(f"Time functools.reduce: {(sum(time_functools))/(len(time_functools))/1e-6}")