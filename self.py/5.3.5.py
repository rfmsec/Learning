def distance(num1, num2, num3):
    if abs(num1 - num2) == 1 or abs(num1 - num3) == 1:
        if abs(num2 -num1) >= 2 or abs(num3 - num1) >= 2:
            return True
    return False

print(distance(1, 2, 10))