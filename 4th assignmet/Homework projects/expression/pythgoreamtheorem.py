import math

def main():
    
    AB = float(input("Enter the length of AB: "))
    AC = float(input("Enter the length of AC: "))
    
  
    BC = math.sqrt(AB ** 2 + AC ** 2)
    
   
    print(f"The length of BC (the hypotenuse) is: {BC}")

main()
