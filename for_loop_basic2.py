# Biggie Size
# Given a list, write a function that changes all positive numbers in the list to "big"

def biggieSize(lst):
    for i in range(0,len(lst), 1):
        if lst[i] > 0:
            lst[i] = "big"
    return lst
print(biggieSize([-1,3,5,-5]))

# Count Positives Given a list of numbers, create a function to replace the last value with the number of positive values
def count_positives(lst):
    sum = 0
    for i in range(0,len(lst), 1):
        if lst[i] >= 0:
            sum += lst[i]
    lst[len(lst)-1] = sum
    return lst
print(count_positives([-1,1,1,1]))

# Create a function taht takes a list and returns the sum of all the values in the list
def sum_total(lst):
    sum = 0
    for i in range(0,len(lst), 1):
        sum += lst[i]
    return sum
print(sum_total([1,2,3,4]))
print(sum_total([6,3,-2]))

# Create a function that takes a list and returns the average of all the values
def average(lst):
    avg = 0
    for i in range(0,len(lst), 1):
        avg += lst[i]
    return avg/len(lst)
print(average([1,2,3,4]))
# Create a function that takes a list and returns the length of the list
def length(lst):
    if len(lst) == 0:
        return 0
    else:
        return len(lst)
print(length([37,2,1,-9]))
print(length([]))

# create a function that takes a list of n umbers and returns the minimum value in the list. If the list is empty, have the function return False
def minimum(lst):
    if len(lst) == 0:
        return False
    else:
        min = lst[0]
        for i in range(0, len(lst),1):
            if min > lst[i]:
                min = lst[i]
    return min
print(minimum([37,2,1,-9]))
print(minimum([]))

# Create a function that takes a list and returns the maximum value in the list. If the list is empty, have the function return false
def maximum(lst):
    if len(lst) == 0:
        return False
    else:
        max = lst[0]
        for i in range(0, len(lst),1):
            if max < lst[i]:
                max = lst[i]
    return max
print(maximum([37,2,1,-9]))
print(maximum([]))


# Ultimate Analysis, create a function that takes a list and returns a dictionary that has the sumTotal, average, minimum, maximum and length of the list.
def ultimate_analysis(lst):
    new_dict = {
        'sumTotal' : 0,
        'average' : 0,
        'minimum' : lst[0],
        'maximum' : lst[0],
        'length': len(lst)
    }
    for i in range(0,len(lst),1):
        if new_dict['minimum'] > lst[i]:
            new_dict['minimum'] = lst[i]
        if new_dict['maximum'] < lst[i]:
            new_dict['maximum'] = lst[i]
        new_dict['sumTotal'] += lst[i]
        
    new_dict['average'] = new_dict['sumTotal']/len(lst)
    return new_dict

print(ultimate_analysis([37,2,1,-9]))

# create a function that takes a list and return that lsit with values reversed. Do this without creating a second list
def reverse_list(lst):
    temp = 0
    for i in range(0, int(len(lst)/2),1):
        temp = lst[i]
        lst[i] = lst[len(lst)-1-i]
        lst[len(lst)-1-i] = temp
        
    return lst
print(reverse_list([37,2,1,-9]))