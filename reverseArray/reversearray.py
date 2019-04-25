# Using Extended Slice
def reverse_array_slice(a):
    return a[::-1]


# Appending a second array
def reverse_array_second_array(a):
    counter = len(a) - 1
    tempArr = []
    for i in range(len(a)):
        tempArr.append(a[counter])
        counter -= 1
    return tempArr
