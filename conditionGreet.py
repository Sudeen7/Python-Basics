"""
    greets morning, afternoon, evening or night based on input time (h,m,s)
"""
print("--Enter the time--")
h = int(input("Enter Hours: "))
m = int(input("Enter Minutes: "))
s = int(input("Enter Seconds: "))
if (h > 24 or m > 59 or s > 59):
    print("!!-Invalid Input-!!")
    if (h > 24):
        print('Hours cannot exceed 24')
    if (m > 60):
        print('Minutes cannot exceed 60')
    if (s > 60):
        print('Seconds cannot exceed 60')
elif (h >= 00 and h < 12):
    print('Good Morning')
elif (h >= 12 and h < 17):
    print('Good Afternoon')
elif (h >= 17 and h < 19):
    print('Good Evening')
elif (h >= 19 and h < 12):
    print('Good Night')
