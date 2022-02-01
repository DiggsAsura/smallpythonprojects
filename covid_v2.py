# Covid_v2
# OK, v2 of this crazy good app (irony). I wanted to avoid that longass if statement
# Next version should be able to take a list with just the 7 days. 

weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

day = input("Day first registered symptoms: ")
new_day = int(weekdays.index(day) + 5)

print("Your quaranteen ends on: " + weekdays[new_day])





		
