# Countdown - Create a function that accepts a number as an input. Return a new list that counts down by one, from the number (as the 0th element) down to 0 (as the last element).

def countdown(num):
    arr = []
    for i in range(num, -1,-1):
        arr.append(i)
    return arr

print(countdown(17))

# input => 5
# output 5,4,3,2,1

#Print and Return - Create a function that will receive a list with two numbers. Print the first value and return the second.

def printAndReturn (small_list):
    print(small_list[0])
    return small_list[1]

#First Plus Length - Create a function that accepts a list and returns the sum of the first value in the list plus the list's length. Example: first_plus_length([1,2,3,4,5]) should return 6 (first value: 1 + length: 5)

def firstPlusLength(medium_list):
    x = medium_list[0] + len(medium_list)
    return x

# Values Greater than Second - Write a function that accepts a list and creates a new list containing only the values from the original list that are greater than its 2nd value. Print how many values this is and then return the new list. If the list has less than 2 elements, have the function return False
#Example: values_greater_than_second([5,2,3,2,1,4]) should print 3 and return [5,3,4]
#Example: values_greater_than_second([3]) should return False

def greaterThanSecond(large_list):
    newList = []
    if len(large_list) < 2:
        return False
    for i in range(0, len(large_list)):
        if large_list[i] > large_list[1]:
            newList.append(large_list[i])
    print(len(newList))
    return newList


#This Length, That Value - Write a function that accepts two integers as parameters: size and value. The function should create and return a list whose length is equal to the given size, and whose values are all the given value.
#Example: length_and_value(4,7) should return [7,7,7,7]
#Example: length_and_value(6,2) should return [2,2,2,2,2,2]

def thisAndThat(length, value):
    newList = []
    for i in range(length):
        newList.append(value)
    return newList


