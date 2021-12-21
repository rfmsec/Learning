def last_early(my_str):
    my_str = my_str.lower()
    total_letters = len(my_str)
    last_letter = my_str[-1]
    first_index = my_str.index(last_letter)
    print((total_letters -1) > first_index)

last_early("happy birthday")
last_early("best of luck")
last_early("Wow")
last_early("X")