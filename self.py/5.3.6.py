def filter_teens(a = 13, b = 13, c = 13):
    a, b, c = fix_age(a), fix_age(b), fix_age(c)
    print(a + b + c)

def fix_age(age):
    if age < 13 or age == 15 or age == 16:
        return age
    elif age >= 13 and age <= 19:
        return 0

filter_teens()
filter_teens(1, 2, 3)
filter_teens(2, 13, 1)
filter_teens(2, 1, 15)
