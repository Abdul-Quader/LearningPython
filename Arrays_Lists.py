# Demo Arrays

# employees = ["Mohammed", "Abdul", "Quader", "Qureshi"]
# print(employees[2])
# print(employees[1:3])

# # Arrays or list methods

# print(len(employees))

# #Access list items individually

# for item in employees:
#     print(item)


# #printing number range
# for item in range(1,5):
#     print(item)

# #printing number range alternatively
# for item in range(1,5,2):
#     print(item)


#Accepting values into the list and displaying the contents
array=[]
for item in range(1,6) :
    element=input(f"Enter element {item}: ")
    array.append(element)
print(array)
