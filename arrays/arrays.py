# 1. Write a function to add integer values of an array

li = [1,2,3,4,5,6,7]


def add_integer(a):
    li.append(a)


print('--2')

# 2.Write a function to calculate the average value of an array of integers


def average(a):
    return sum(li)/len(li)


print('--3')
# 3.Write a program to find the index of an array element


def index_of_list(a):
    return li.index(a)


print('--4')

# 4. Write a function to test if array contains a specific value


def contain(a):
    return a in li


print('--5')

# 5. Write a function to remove a specific element from an array


def remove(a):
    li.remove(a)


print('--6')

# 6.Write a function to copy an array to another array


def copy(a):
    x = li[::]


print('--7')

# 7.Write a function to insert an element at a specific position in the array


def insert(value,pos):
    li.insert(value,pos)


print('--8')

# 8.Write a function to find the minimum and maximum value of an array


def maximum_minimum(a):
    if a == 'maximum':
        return max(li)
    else:
        return min(li)


print('--9')

# 9.Write a function to reverse an array of integer values


def reverse(a):
    return li[::-1]


print('--10')

# 10.Write a function to find the duplicate values of an array


def duplicates(a):
    duplicates=[]
    for i in li:
        if i not in duplicates:
            duplicates.append(i)
        else:
            print(i,end=' ')


print('--11')

# 11. Write a program to find the common values between two arrays


def common_values(a,b):
    common_val = []
    for i in a:
        for j in b:
            if i==j:
                if i not in common_val:
                    common_val.append(i)
    return common_values


print('--12')

# 12.Write a method to remove duplicate elements from an array


def remove_duplicates(a):
    return list(dict.fromkeys(a))


print('--13')

# 13. Write a method to find the second largest number in an array


def second_largest(a):
    a.sort()
    return a[-2]


print('--14')

# 14.Write a method to find number of even number and odd numbers in an array


def even_odd(a):
    for i in a:
        if a%2 == 0:
            print('even')
        else:
            print('odd')


print('--15')

# 15.Write a function to get the difference of largest and smallest value


def difference_bw_large_and_small(a):
    a.sort()
    return a[-1]-a[0]


print('--16')

# 16.Write a method to verify if the array contains two specified elements(12,23)


def contains(a,b):
    if a in li:
        if b in li:
            return True
    return False


print('--17')

# 17.Write a program to remove the duplicate elements and return the new array


def remove(a):
    new_list = []
    for i in a:
        if i not in new_list:
            new_list.append(i)
    return new_list


print('--18')

# 18. Write a function to find the missing number of sorted array of 1 to 100


def missing_number(a):
    li = []
    for i in range(1,10):
        li.append(i)
    for j in li:
        if j not in sorted(a):
            print(j)






















