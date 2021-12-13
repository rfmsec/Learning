total = int(input("Enter three digits (each digit for one pig): "))

num1 = total // 100
num2 = total % 100 // 10
num3 = total % 100 % 10
total = num1 + num2 + num3
divison_equal = total % 3 == 0

print(total)
print(total // 3)
print(total % 3)
print(divison_equal)
