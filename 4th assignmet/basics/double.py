def double_until_100():
    
    curr_value = int(input("Enter a number: "))


    while curr_value < 100:
        curr_value = curr_value * 2
        print(curr_value, end=" ")


double_until_100()
