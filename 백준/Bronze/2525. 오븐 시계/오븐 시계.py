hour, minute = input().split()

my_time = int(input())

my_hour = int(hour)
my_minute = int(minute)

result = my_time // 60
remain = my_time % 60

if  my_minute + remain >= 60:
    if my_hour + result >= 23:
        print(my_hour + result + 1 - 24, my_minute + remain - 60)
    else:
        print(my_hour + result + 1, my_minute + remain - 60)
else:
    if my_hour + result >= 24:
        print(my_hour + result -24, my_minute + remain)
    else:
        print(my_hour + result, my_minute + remain)