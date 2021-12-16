temp = input("Insert the temperature you would like to convert: ")
if "c" in temp.lower():
    new_temp = (float(temp[:-1]) * 9 / 5) + 32
    print(str(new_temp) + "F")
elif "f" in temp.lower():
    new_temp = (float(temp[:-1]) - 32) * 5 / 9
    print(str(new_temp) + "C")