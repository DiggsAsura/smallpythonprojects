# Covid_v3
# Yet another crazy good update on this amazing app! xD
# A tetris friend gave me a hint i could use modulus to avoid having a double list. 
# I still can't wrap my head around how it works here but it did! Thanks G!

weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
day = input("First day you registered symptoms: ")

new_day = (weekdays.index(day) + 5) % 7

print("Your quaranteen ends on " + weekdays[new_day])
