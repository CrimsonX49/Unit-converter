def c_to_f (a):
    return a * 9/5 + 32

def f_to_c (a):
    return a - 32 * 5/9 

def cen_to_inc (a):
    return a / 2.54

def inc_to_cen (a):
    return a * 2.54

print("Welcome to my standard unit converter! With no spaces included, please select an option: ")
print("1. Convert Celsius to Fahrenheit")
print("2. Convert Fahrenheit to Celsius")
print("3. Convert Centimeters to Inches")
print("4. Convert Inches to Centimeters")
 
while True:
    user_choice = input("Enter your option choice: 1, 2, 3, or 4")
    if user_choice == "1":
        try: 
            float1 = float(input("Enter the Celsius you'd like to convert: "))
        except ValueError:
            print("Please enter a valid number!")
            continue
    elif user_choice == "2":
        try:
            float2 = float(input("Enter the Fahrenheit you'd like to convert: "))
        except ValueError:
            print("Please enter a valid number!")
            continue
    elif user_choice == "3":
        try:
            float3 = float(input("Enter the Centimeters you'd like to convert: "))
        except ValueError:
            print("Please enter a valid number!")
            continue 
    elif user_choice == "4":
        try: 
            float4 = float(input("Enter the Inches you'd like to convert: "))
        except ValueError:
            print("Please enter a valid number!")
            continue
    else:
        print("Please enter a valid choice!")
        continue
        
    if user_choice == "1": 
        print(c_to_f(float1), "°", "F", sep="")
    if user_choice == "2":
        print(f_to_c(float2), "°", "C", sep="")    
    if user_choice == "3":
        print(cen_to_inc(float3), "Inches")
    if user_choice == "4":
        print(inc_to_cen(float4), "Centimeters")
        
    while True:
        next_conversion = input("Convert more units? Y/N?")
        if next_conversion == "Y" or next_conversion == "y":
            break
        else:
            print("Thank you for using my unit converter. :)")
            continue
            


 