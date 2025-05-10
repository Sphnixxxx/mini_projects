#asking input
weight= float(input("enter a weight: "))
#asking whether it is in kg or pound:
unit=input("enter its unit(k/l): ")

if unit == "k":
    weight= weight * 2.204
    print(f"your weight in kilogram is:  {weight}lbs")
elif unit=="l":
    weight=weight/2.204
    print(f"your weight in pound is : {weight}kg")
else:
    print("invalid: try again!!")    
    
