# #introducing function to calculate factorial using for loop
# n=int(input("please enter a positive integer\n"))
# def factorial_iterative(n):
#     result = 1
#     for i in range(1, n + 1):
#         result *= i
#     return result
# print(f"The factorial is {factorial_iterative(n)}")


#introducing function to calculate factorial using while loop
n=int(input("please enter a positive integer\n"))
def factorial_iterative(n):
    result = 1
    i=1
    while i < n+1 :
        result *= i
        i+=1
    return result
print(f"The factorial is {factorial_iterative(n)}")