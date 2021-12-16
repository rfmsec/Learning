import calendar


days = ["Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday", "Sunday"]

date = input("Enter a date: ").split('/')
day = calendar.weekday(int(date[2]), int(date[1]), int(date[0]))
print(days[day])
