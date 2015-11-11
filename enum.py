from enum import Enum,unique

Month=Enum('Month',('Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'))

for name,member in Month.__members__.items():
    print(name,'=>',member,',',member.value)

@unique
class Weekday(Enum):
    Sun=0
    Mon=1
    Tue=2
    Wed=3
    Thu=4
    Fri=5
    Sat=6

day1=Weekday.Fri
print(day1)
print(day1.value)
print(Weekday(1))
print(Weekday.Mon)
print(Weekday['Mon'])
print(day1==Weekday.Fri)
