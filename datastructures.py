"""
data structures is a way of managing data in memory
in python 1.list
          2.tuple
          3.dictionary
"""
#
my_numbers=[1,2,3,4,5,6,7,8]#listofnumbers
my_floats=[10.1,10.2,10.3,10.4,10.5]#listoffloats
my_pets=["dog","cat","rat","rabbit"]#listofstrings
my_bool=[True,True,False,False,True,False]#listofstrings
mixed_types=[1,"hello",False,10.8]#mixedt data ypes
lists_of_lists=[[1,2,3,4],[10,"10",True],[10.5]]

#list indexing
print("get number7",my_numbers[-2])
print("get number7",my_numbers[-6])

#list slicing
print("+slicing",my_numbers[1:5])
print("+slicing",my_numbers[-7:-3])

#reverse my numbers list
print(my_numbers[::-3])

#list of list
my_bool=lists_of_lists
print(my_bool[1],[2])
print(lists_of_lists[1][2])






