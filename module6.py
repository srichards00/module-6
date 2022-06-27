# module 6
# 1
import sys
from datetime import datetime
from datetime import time
from datetime import date
from datetime import timedelta
def main():
    dt = datetime.now()
    utc = datetime.utcnow()
    time_string = dt.strftime("%X")
for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) == 6:
        _date, _time, store, item, cost, payment = data
        print("{dt}\t{time_string}\t{store}\t{item}\t{cost}\t{payment}")
main()

# Q2
print(datetime.now() + timedelta(days = 1))
print(datetime.now() - timedelta(seconds = 60))
print(datetime.now() + timedelta(days = 730))

#Q3
d = timedelta(minutes = 13, hours = 10, days = 100)
print(d)

# Q4
datetime_object = datetime.now()
def main(a,b,c):
    print("Date: ", datetime_object)
    print("Feet: ", a)
    print("Inches: ", b)
a = input("Input measurement in Feet: ")
b = input("Input measurement in Inches: ")
c = datetime_object
main(a, b, c)
