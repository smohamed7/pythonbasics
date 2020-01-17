tasklist =[23,"jane",["lesson 23",560,{"currency":"KES"}],987,(76,"john")]

print(tasklist)
#1.Determinig of variable intasklist an inbuilt function

x= type(tasklist)

print(tasklist)

#print KES

print(tasklist[2][2]["currency"])

#print 560

print(tasklist[2][1])

#length of task
print(len(tasklist))

#change 987 to 789 without using an inbuilt method

num =987
num =str(num)

print(num[::-1])

#change the name of john to jane

name = "jane"
print(name.replace("john","jane"))



