def animals_legs(a,b,c):
    legs =(2,4)
    total_legs=a*legs[0]+b*legs[1]+c*legs[1]
    return total_legs

ch = int(input("Enter number of chickens:"))
cow = int(input("Enter number of cows:"))
pigs = int(input("Enter number of pigs:"))

print("total legs ",animals_legs(ch,cow,pigs))

