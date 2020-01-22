def max_num_in_list( list ):
    max = list[ 0 ]
    min=list[0]
    for a in list:
        if a > max:
            max = a
    for a in list:
        if a < min:
            min = a
    return max-min

print(max_num_in_list([10,15,20,2,10,6]))
print(max_num_in_list([-3,4,-9,-1,-2,15]))
