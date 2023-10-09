# To understand if statement
weight = int(input("Please enter your weight "))
KoL = input("Please type K for Kgs and L for Pounds")

if (KoL=='K' or KoL=='k') : 
    print("your weight is "+ str(weight) + "kgs")
    print("And in Pounds " + str(weight // 0.45) + "Lbs")
else:
    print("your weight is " + str(weight) + "Lbs")
    print("And in Kgs " + str(int(weight * 0.45)) + "Kgs")