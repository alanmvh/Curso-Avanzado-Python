
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

# Exercise 4

# import of numpy module
import numpy as np
# numpy.linspace(start, stop, num=X)
# Output: [-2.  -1.6 -1.2 -0.8 -0.4  0.   0.4  0.8  1.2  1.6  2. ]
np_values = np.linspace(-2, 2, num=11)

#  Exercise 5

cero_matrix = np.zeros((6,8))

# Modify the index row 4, column 5 with value 3
cero_matrix[3][4] = 3

# Modify index  in row 3, column 4 with value 6
cero_matrix[2][3] = 6

# Matrix output:
# [[0. 0. 0. 0. 0. 0. 0. 0.]
#  [0. 0. 0. 0. 0. 0. 0. 0.]
#  [0. 0. 0. 6. 0. 0. 0. 0.]
#  [0. 0. 0. 0. 3. 0. 0. 0.]
#  [0. 0. 0. 0. 0. 0. 0. 0.]
#  [0. 0. 0. 0. 0. 0. 0. 0.]]

# Get row 3 and calculate the avg of their values
# Range: [0. 0. 0. 6. 0. 0. 0. 0.]
# Avg = 0.75
avg = cero_matrix[2, :].mean()

# Get column 5 and obtain the avg value of the array
# Output = 0.5
avg_2 = cero_matrix[:, 4].mean()

# Get transposed matrix and obtain row 4 - Calculate the avg of the values
# Output : 1.0
t_1 = cero_matrix.T[3, :].mean()

# Get transposed matrix and obtain column 4 - Calculate the avg of the values
# Output = 0.375
t_2 = cero_matrix.T[:, 3].mean()


# Exercise 6
# Create a vector x in a linealspace -10 - +10 with `11` numbers
# Output = [-10.  -8.  -6.  -4.  -2.   0.   2.   4.   6.   8.  10.]
v_x = np.linspace(-10, 10, num=11)
# Create vector y in a lineal space from `-10` - `+10` with 21 numbers
# Output = [-10.  -9.  -8.  -7.  -6.  -5.  -4.  -3.  -2.  -1.   0.   1.   2.   3.   4.   5.   6.   7.   8.   9.  10.]
v_y = np.linspace(-10, 10, num=21)
# Create a matrix `z` with `11x21` ceros
# Output:
# [[0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
#  [0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
#  [0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
#  [0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
#  [0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
#  [0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
#  [0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
#  [0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
#  [0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
#  [0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
#  [0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]]
Z = np.zeros((11,21))

#Loops through indices 0 to 11 (exclusive) for an i, inside the iterator loops through indices 0 to 21 (exclusive) for a j.
for i in range(len(v_x)):
    for j in range(len(v_y)):
        # Inside both iterators get the xi of array x at index i (i.e. x[i]).
        print(f"Index i: {i} Value:{v_x[i]}")
        # Inside both iterators get the yj of the array y at index j (i.e. y[j]).
        print(f"Index j: {j} Value:{v_y[j]}")
        
        # Calculate Z[i][j] = np.exp(-(xi ** 2 + yj ** 2)).
        Z[i][j] = np.exp(-(v_x[i] ** 2 + v_y[j] ** 2))

# Matrix X Output:
# [1.38389653e-87 2.47001036e-79 5.96629836e-72 1.95039330e-65
#   8.62880116e-60 5.16642063e-55 4.18639400e-51 4.59093847e-48
#   6.81355682e-46 1.36853947e-44 3.72007598e-44 1.36853947e-44
#   6.81355682e-46 4.59093847e-48 4.18639400e-51 5.16642063e-55
#   8.62880116e-60 1.95039330e-65 5.96629836e-72 2.47001036e-79
#   1.38389653e-87]
#  [5.96629836e-72 1.06487866e-63 2.57220937e-56 8.40859712e-50
#   3.72007598e-44 2.22736356e-39 1.80485139e-35 1.97925988e-32
#   2.93748211e-30 5.90009054e-29 1.60381089e-28 5.90009054e-29
#   2.93748211e-30 1.97925988e-32 1.80485139e-35 2.22736356e-39
#   3.72007598e-44 8.40859712e-50 2.57220937e-56 1.06487866e-63
#   5.96629836e-72]
#  [8.62880116e-60 1.54008828e-51 3.72007598e-44 1.21609930e-37
#   5.38018616e-32 3.22134029e-27 2.61027907e-23 2.86251858e-20
#   4.24835426e-18 8.53304763e-17 2.31952283e-16 8.53304763e-17
#   4.24835426e-18 2.86251858e-20 2.61027907e-23 3.22134029e-27
#   5.38018616e-32 1.21609930e-37 3.72007598e-44 1.54008828e-51
#   8.62880116e-60]
#  [4.18639400e-51 7.47197234e-43 1.80485139e-35 5.90009054e-29
#   2.61027907e-23 1.56288219e-18 1.26641655e-14 1.38879439e-11
#   2.06115362e-09 4.13993772e-08 1.12535175e-07 4.13993772e-08
#   2.06115362e-09 1.38879439e-11 1.26641655e-14 1.56288219e-18
#   2.61027907e-23 5.90009054e-29 1.80485139e-35 7.47197234e-43
#   4.18639400e-51]
#  [6.81355682e-46 1.21609930e-37 2.93748211e-30 9.60268005e-24
#   4.24835426e-18 2.54366565e-13 2.06115362e-09 2.26032941e-06
#   3.35462628e-04 6.73794700e-03 1.83156389e-02 6.73794700e-03
#   3.35462628e-04 2.26032941e-06 2.06115362e-09 2.54366565e-13
#   4.24835426e-18 9.60268005e-24 2.93748211e-30 1.21609930e-37
#   6.81355682e-46]
#  [3.72007598e-44 6.63967720e-36 1.60381089e-28 5.24288566e-22
#   2.31952283e-16 1.38879439e-11 1.12535175e-07 1.23409804e-04
#   1.83156389e-02 3.67879441e-01 1.00000000e+00 3.67879441e-01
#   1.83156389e-02 1.23409804e-04 1.12535175e-07 1.38879439e-11
#   2.31952283e-16 5.24288566e-22 1.60381089e-28 6.63967720e-36
#   3.72007598e-44]
#  [6.81355682e-46 1.21609930e-37 2.93748211e-30 9.60268005e-24
#   4.24835426e-18 2.54366565e-13 2.06115362e-09 2.26032941e-06
#   3.35462628e-04 6.73794700e-03 1.83156389e-02 6.73794700e-03
#   3.35462628e-04 2.26032941e-06 2.06115362e-09 2.54366565e-13
#   4.24835426e-18 9.60268005e-24 2.93748211e-30 1.21609930e-37
#   6.81355682e-46]
#  [4.18639400e-51 7.47197234e-43 1.80485139e-35 5.90009054e-29
#   2.61027907e-23 1.56288219e-18 1.26641655e-14 1.38879439e-11
#   2.06115362e-09 4.13993772e-08 1.12535175e-07 4.13993772e-08
#   2.06115362e-09 1.38879439e-11 1.26641655e-14 1.56288219e-18
#   2.61027907e-23 5.90009054e-29 1.80485139e-35 7.47197234e-43
#   4.18639400e-51]
#  [8.62880116e-60 1.54008828e-51 3.72007598e-44 1.21609930e-37
#   5.38018616e-32 3.22134029e-27 2.61027907e-23 2.86251858e-20
#   4.24835426e-18 8.53304763e-17 2.31952283e-16 8.53304763e-17
#   4.24835426e-18 2.86251858e-20 2.61027907e-23 3.22134029e-27
#   5.38018616e-32 1.21609930e-37 3.72007598e-44 1.54008828e-51
#   8.62880116e-60]
#  [5.96629836e-72 1.06487866e-63 2.57220937e-56 8.40859712e-50
#   3.72007598e-44 2.22736356e-39 1.80485139e-35 1.97925988e-32
#   2.93748211e-30 5.90009054e-29 1.60381089e-28 5.90009054e-29
#   2.93748211e-30 1.97925988e-32 1.80485139e-35 2.22736356e-39
#   3.72007598e-44 8.40859712e-50 2.57220937e-56 1.06487866e-63
#   5.96629836e-72]
#  [1.38389653e-87 2.47001036e-79 5.96629836e-72 1.95039330e-65
#   8.62880116e-60 5.16642063e-55 4.18639400e-51 4.59093847e-48
#   6.81355682e-46 1.36853947e-44 3.72007598e-44 1.36853947e-44
#   6.81355682e-46 4.59093847e-48 4.18639400e-51 5.16642063e-55
#   8.62880116e-60 1.95039330e-65 5.96629836e-72 2.47001036e-79
#   1.38389653e-87]]

# Calculate the projected matrices of X and Y to graph in 3 dimensions with:
Y, X = np.meshgrid(v_y, v_x)

# Create a graph with X, Y and Z
import matplotlib.pyplot as plt

ax = plt.figure().add_subplot(projection='3d')

ax.plot_surface(X, Y, Z)

# # How does it look like this graph with 101 and 201 numbers instead 11 and 21
v_x2 = np.linspace(-10, 10, num=101)
v_y2 = np.linspace(-10, 10, num=201)
Z2 = np.zeros((101,201))

#Loops through indices 0 to 11 (exclusive) for an i, inside the iterator loops through indices 0 to 21 (exclusive) for a j.
for i in range(len(v_x2)):
    for j in range(len(v_y2)):
        # Inside both iterators get the xi of array x at index i (i.e. x[i]).
        print(f"Index i: {i} Value:{v_x2[i]}")
        # Inside both iterators get the yj of the array y at index j (i.e. y[j]).
        print(f"Index j: {j} Value:{v_y2[j]}")
        
        # Calculate Z[i][j] = np.exp(-(xi ** 2 + yj ** 2)).
        Z2[i][j] = np.exp(-(v_x2[i] ** 2 + v_y2[j] ** 2))
Y2, X2 = np.meshgrid(v_y2, v_x2)

ax2 = plt.figure().add_subplot(projection='3d')
ax2.plot_surface(X2, Y2, Z2)

plt.show()