num_class_held =int(input("enter classes held:"))
num_class_attended =int(input("enter number of classes attended:"))
percentage_attended = (num_class_attended/num_class_held)*100
medical_cause="yes"
no_cause="no"

medical_input = input("enter if you had a medical issue yes or no:")

print("attended number of classes",percentage_attended,"%")
if   num_class_attended >=75:
    print("let student sit for exam")
else:
    print("student barred from exam")
 
 





