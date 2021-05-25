# def hourToSec(hour):
#     sec = hour * 3600
#     print(f'{hour} hour is {sec} seconds')
#
#
# hour = float(input("Enter the hour: "))
# hourToSec(hour)

def secToHour(sec):
    hour = sec / 3600
    print(f'{sec} seconds is equal to {hour} hours')


sec = float(input("Enter the second: "))
secToHour(sec)

