# * This program asks the user to input 10 ﬂoats, store them in a list and finds and prints out
# * the total of all the numbers, the index of the maximum, the index of the minimum,
# * the average of the numbers and round off to 2 decimal places and the median number.

# Adding features to output messages

GREEN = '\033[92m'
WHITE = '\033[0m'
BOLD = '\033[1m'

import math

# Creating list to store float numbers

float_list = []

# Populating list with user's float numbers

for i in range(10):

    float_list.append(float(input(f"Please insert float #{BOLD}{GREEN}{i+1}{WHITE}: ")))

# Finding the total of all the numbers and printing the result

total = sum(float_list)
print(f"\nThe total of all the numbers is {round(total, 2)}")

# Finding the index of the maximum and printing the result

maximum = max(float_list)
print(f"\nThe index of the maximum float is {float_list.index(maximum)}")

# Finding the index of the minimum and printing the result

minimum = min(float_list)
print(f"\nThe index of the minimum float is {float_list.index(minimum)}")

# Calculating the average of the numbers and rounding off to 2 decimal places

average = total / 10
print(f"\nThe average of the numbers is {round(average, 2)}")

# Finding the median number and printing the result
# Following example from https://www.w3schools.com/python/ref_stat_median.asp#:~:text=median()%20method%20calculates%20the,in%20a%20set%20of%20data.

import statistics
print(f"\nThe median number is {statistics.median(float_list)}")
