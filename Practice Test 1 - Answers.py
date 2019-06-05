"""Valerie's"""

import math

#Q4
def collapse_values(data):
    for key in data : 
        values = data[key]
        sum = 0 
        for element in values :
            sum += element
        data[key] = sum

#Q5
def factorial(n):
    total = 1 
    while n > 0 :
        total *= n 
        n -= 1
    return total

#Q6
def fibonacci(n):    
    if n == 0: 
        return 0
    elif n == 1: 
        return 1
    else: 
        return fibonacci(n-1)+fibonacci(n-2)

#Q7
def get_largest_value(a_dict):
    maximum = 0 
    for key in a_dict:
        if a_dict[key] > maximum :
            maximum = a_dict[key]
    return maximum

#Q9
def print_prime(upper_bound):
    print_string = ""
    for num in range(2, upper_bound + 1):
        if all(num%i!=0 for i in range(2,num)):
            print_string += str(num) + " "
    print(print_string)

#Q10
def rate(n):
    sums = 0
    i = 1
    ops = 0 
    while i < n:
        j = 0
        while j < n:
            sums = i * j + sums
            ops += 1 
            j = j + 1
        i = i * 2
    print("No of operations", ops)

#Q11
def sum_of_factors(num):
    sum = 0 
    for i in range (1, num + 1):
        if num % i == 0 :
            sum += i
    return sum

#Q12
def word_frequencies(string):
    string = string.lower()
    my_dict1 = {}
    my_dict2 = {}
    for word in string.split() :
        if word in my_dict1 :
            my_dict1[word] += 1 
        else:
            my_dict1[word] = 1 
    for element in my_dict1:
        value = my_dict1[element]
        if value in my_dict2 :
            my_dict2[value].append(element)
        else:
            my_dict2[value] = [element]
    for key in my_dict2 :
        my_dict2[key] = sorted(my_dict2[key])
    for i in sorted(my_dict2, reverse = True):
        print(i, my_dict2[i], end = "\n")

#Q13
def sort_second_element(sublists):
    l = len(sublists)
    for i in range(0, l):
        for j in range(0, l - i - 1):
            if (sublists[j][1] > sublists[j + 1][1]):
                temp = sublists[j]
                sublists[j] = sublists[j + 1]
                sublists[j + 1] = temp
    return sublists

#Q14 - Q16
class RegularPolygon:
    def __init__(self, n = 3, side = 1, x = 0, y = 0):
        self.__n = n 
        self.__side = side
        self.__x = x
        self.__y = y

    def get_n(self):
        return self.__n

    def get_side(self):
        return self.__side

    def getX(self):
        return self.__x
    
    def getY(self):
        return self.__y
    
    def get_perimeter(self):
        return self.__n * self.__side

    def get_area(self):
        return ((self.__side ** 2 * self.__n) / (4 * math.tan(math.pi / self.__n)))
    
