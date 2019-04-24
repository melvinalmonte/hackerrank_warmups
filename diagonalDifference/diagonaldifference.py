def diagonalDifference(arr):
    diagonal_left_to_right = 0
    diagonal_right_to_left = 0
    counter = len(arr) - 1

    for i in range(len(arr)):
        diagonal_left_to_right += arr[i][i]
        diagonal_right_to_left += arr[i][counter]
        counter -= 1
    result = diagonal_right_to_left - diagonal_left_to_right
    if result < 0:
        return result * -1
    else:
        return result
