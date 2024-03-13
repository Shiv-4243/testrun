import time
timestamp = time.strftime('%H : %M : %S')
print(timestamp)
hour = int(time.strftime('%H')) #convert to int to manupulate
print(hour)

min = int(time.strftime('%M')) #convert to int to manupulate
print(min)

sec = int(time.strftime('%S')) #convert to int to manupulate
print(sec)

if hour >= 12:
    print(' good afternoon ')
else:
    print('good morning')