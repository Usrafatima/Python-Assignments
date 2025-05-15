def get_first_element(lst):
 
    print(lst[0])


n = int(input("How many elements would you like to add to the list? "))
lst = []

for _ in range(n):
    element = input("Enter an element: ")
    lst.append(element)


get_first_element(lst)
