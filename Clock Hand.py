import time
startTime = time.time()
timePeriod = eval(input())
longitude = eval(input())
atLongitude = (24 / 360) * longitude
atLongitude = (round(atLongitude, 2))
# print(atLongitude)
atLongitude *= 100
hour = int(atLongitude / 100)
minute = int(atLongitude % 100)
minute *= 0.6
# print("hour", hour)
angleHour = 0.5 * (hour * 60 + minute)
angleMinute = 6 * minute
# print(angleHour)
# print(angleMinute)
angle = abs(angleMinute - angleHour)
angle = min(360 - angle, angle)
print(round(angle, 2))
# print("execution time = ", time.time() - startTime)
