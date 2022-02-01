# Tested positive on corona today. Thought I could try use python to write a simple
# program to return which day i'm out of quaranteen. It's actually a bit more annoying then 
# I first thought. Was thinking in lines of just returning (day) + 5 (6 days of quaranteen)
# But the closest I got when using a list is for it to return an integer. I could not figure
# how to get it to return the actual value. Ex. Symptoms on Sunday, but it would return 11 for when
# im out of quarnteen, not Friday. 
# For now, pivot, and just make a longass if statement. 

# weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

registered_symptoms = input("Day you first got symptoms: ")

if registered_symptoms == "Monday":
	print("Quaranteen ends on Saturday")
elif registered_symptoms == "Tuesday":
	print("Quaranteen ends on Sunday")
elif registered_symptoms == "Wednesday":
	print("Quaranteen ends on Monday")
elif registered_symptoms == "Thursday":
	print("Quaranteen ends on Tuesday")
elif registered_symptoms == "Friday":
	print("Quaranteen ends on Wednesday")
elif registered_symptoms == "Saturday":
	print("Quaranteen ends on Thursday")
elif registered_symptoms == "Sunday":
	print("Quaranteen ends on Friday")
			

# Fucking ugly code
# But it's something



	
