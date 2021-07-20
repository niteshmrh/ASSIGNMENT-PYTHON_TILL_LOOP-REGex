"""
Q.3 Write a program to calculate BMI of a person after inputting the weight in
kgs and height in meters and then print the nutritional status as per the given
table
"""
def Nutritional():
    a=float(input("Enter height in kg= "))
    b=float(input("Enter weight in m= "))
    c= b/a**0.5
    if (c < 18.5):
        print("Underweight ")
    elif (c>=18.5 or c<=24.9):
        print("Normal ")
    elif (c>=25 or c<=29.9):
        print("overweight")
    elif (c>=30):
        print("Obesed")
    else:
        print("enter valid values")

#Driver Code
Nutritional()
