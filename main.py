'''
Leila Lopez Marks
9/24/2020
Python Trip Planner Assignment
'''
'''
#Make a greeting
print("Welcome to Vacation Planner")
customers_name=input("What's your name?")
destination=input("Nice to meet you "+ customers_name+ " where are you travelling to?")
print("Great! "+ destination + " Sounds like a great trip!")
print("******")

number_of_days = int(input("How many days are you going to spend?"))
integer_number_of_days= int(number_of_days)
budget = int(input('How much are you willing to spend?'))
currency = input('What is the three letter currency symbol for your travel destination?')
conversion_rate = float(input('How many MXC are there in 1 USD?'))
hours = number_of_days*24
minutes = hours*60

# Part 2 - Travel time and budget
print(f'If you are traveling for {number_of_days} days that is the same as{hours} hours or {minutes} minutes')

daily_budget = budget/number_of_days
print(f'If you are going to spend {budget} {currency} that means per day you can spend {daily_budget} {currency}')

# If time difference + 12 is <= 24
midnight = 0
noon = 12
time_difference = int(input('What is the time difference, in hours, between your home and your destination?' ))
adjusted_midnight = time_difference + midnight
adjusted_noon = time_difference + noon
# if(time_difference <= 12 and time_difference >= 0):

if(time_difference < 0):
   adjusted_midnight = 24+time_difference

print(f'That means when it is midnight at home it will be {adjusted_midnight}  in the previous day in your travel destination')
print(f'And when it is noon at home it will be {adjusted_noon} in your travel destination')
'''
def time_change():
    time_difference = int(input("What is the time difference, in hours, between your home and your destination? If the time is behind, use a negative symbole in front of the amount of hours. "))
        #our_time_input = 12
    noon = 12
    midnight=0
     # so the time difference could be + or -
     # convert the string to a int
    int_time_difference = int(time_difference)

     # calculate from noon
    difference_hrs_noon = noon + int_time_difference
    difference_hrs_midnight=midnight+int_time_difference
    print(difference_hrs_noon,"Difference hours noon",difference_hrs_midnight,"Difference hours midnight")
    # these two condisions are on different days
    # use % to get how many hours over into the next day could be + or -
    # use % to get how many hours over into the next day could be + or -
    adjusted_noon=difference_hrs_noon%24
    adjusted_midnight=difference_hrs_midnight%24
    print(adjusted_noon,"This is adjusted noon")
    print(adjusted_midnight,"This is adjusted midnight")
    if difference_hrs_noon <= 24 and difference_hrs_noon >=0:
        print("Destination time is ", difference_hrs_noon, ":00 from noon 12:00")
    if difference_hrs_noon > 24:
        print(f"Destination time is  {adjusted_noon}:00 hrs(s) on the next day from noon 12:00")
    if difference_hrs_noon <0:
        print(f"Destination time is  {adjusted_noon}:00 hrs on the previous day from noon 12:00")


    if difference_hrs_midnight <= 24 and difference_hrs_midnight >=0:
        print("Destination time is ", difference_hrs_midnight, ":00 from midnight 0:00")
    if difference_hrs_midnight > 24:
        print(f"Destination time is  {adjusted_midnight}:00 hrs(s) on the next day from midnight 0:00")
    if difference_hrs_midnight <0:
        print(f"Destination time is  {adjusted_midnight}:00 hrs on the previous day from midnight 0:00")

time_change()




