a = int(input("Please enter a number:"))
b = int(input("Please enter the other number:"))

a1 = str(a)
b1 = str(b)

common_list = ""

for digit in a1:
    if digit in b1 and digit not in common_list:
        common_list += digit
        print(f"{digit} is common in both the numbers.")
        


