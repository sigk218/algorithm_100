import sys
sys.stdin = open('input.txt', 'r')

import datetime

x, y = map(int, input().split())
d = datetime.datetime(2007, x, y)
day = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
print(day[d.weekday()])