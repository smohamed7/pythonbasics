def max_num_in_list( list ):
    max = list[ 0 ]
    for a in list:
        if a > max:
            max = a
    return max
print(max_num_in_list([4, 5, 1, 3]))
print(max_num_in_list([300, 200, 600, 150]))
print(max_num_in_list([1000, 1001, 857, 1]))