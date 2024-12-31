import time

# we retrieve the user's credits from the txt file
file = open("user_credits.txt", "r")
content = file.read()

if content == '':
    user_credits = 0
else:
    user_credits = int(content)

file.close()

def timer(seconds):
    credits = 0
    initial_seconds = seconds
    while seconds:
        # divmod attribute the first variable the quotient and the second the remainder
        hrs, secs = divmod(seconds, 3600)
        mins, secs = divmod(secs, 60)
        # formatting of the timer
        time_format = '{:02}:{:02}:{:02}'.format(hrs, mins, secs)
        print(time_format, end='\r')
        time.sleep(1)
        seconds -= 1
        elapsed_seconds = initial_seconds - seconds
        # every minute, the user earn a credit
        if elapsed_seconds % 60 == 0:
            credits += 1
            # print(f'Credits: {credits}')

    print('00:00:00')
    # print(f'Total Credits Earned: {credits}')
    return credits

seconds = int(input("Enter the time in seconds: "))
user_credits += timer(seconds)

# we add the credits to the txt file
with open("user_credits.txt", "w") as file:
    file.write(str(user_credits))