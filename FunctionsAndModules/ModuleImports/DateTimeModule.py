# Well we know different countries have different time zones,
# So for computer a universal time in designed, and taking this as reference each country has its time
# Each country rely on how ahead of back they are about univeresal time.
#  So Instead of working with local time zaone its better to use universal time zone
# Python standard Library provides three module to deal with time:
# time, date time, calendar

import time
# help(time)
print(time.gmtime(0))

print(time.localtime())

print(time.time())      # It returns no of seconds till 1/1/1997 00:00:00 (UTC)

# Important: It is recommended to store the date in string in formnat - 'yyyy/mm/dd'

# localtime() : it returns a tuple or we can say structure( in C language)

time_now = time.localtime()
print('Year : ', time_now[0])
print('Month : ',time_now.tm_mon)
# We can use the predefined name given to different value of the tuple instead of indices
print('Day : ', time_now.tm_mday)

# Calculating the elapsed time in a reaction rate finder game:

# To calculate elapse time there are three ways :
# using time, perf_counter, monotonic classes in time module
# import time, random
# from time import time as myTimer
#
# input('Press any key to Start\n')
# time.sleep(random.randint(1,2))
# start_timer = myTimer()
# input("Press any key to Stop ")
# end_timer = myTimer()
# print('Starting Time : {0}\nEnding time : {1}\nElapsed Time : {2}'
#        .format(time.strftime("%X",time.localtime(start_timer)), time.strftime("%X",time.localtime(end_timer)),
#         end_timer-start_timer))
#
# # O/P-->
# # Starting Time : 18:21:12
# # Ending time : 18:21:13
# # Elapsed Time : 0.7515645027160645
#
# # Above line strftime() methos changes the time which is seconds to specified format as the argument
# # To the directives or formats use documentation
# print()
# print('*'*80)
# # Using perf_counter class:
#
# import time, random
# from time import perf_counter as myTimer
#
# input('Press any key to Start\n')
# time.sleep(random.randint(1,2))
# start_timer = myTimer()
# input("Press any key to Stop ")
# end_timer = myTimer()
# print('Starting Time : {0}\nEnding time : {1}\nElapsed Time : {2}'
#       .format(time.strftime("%X",time.localtime(start_timer)), time.strftime("%X",time.localtime(end_timer)),
#               end_timer-start_timer))
#
# # O/P-->
# # Press any key to Stop
# # Starting Time : 05:30:00
# # Ending time : 05:30:00
# # Elapsed Time : 0.5441309866666667
#
# # we can see it is not showing right time, it best suited for finding elapsed time
#
# print()
# print('*'*80)
# # Using monotonic class:
#
# import time, random
# from time import monotonic as myTimer
#
# input('Press any key to Start\n')
# time.sleep(random.randint(1,2))
# start_timer = myTimer()
# input("Press any key to Stop ")
# end_timer = myTimer()
# print('Starting Time : {0}\nEnding time : {1}\nElapsed Time : {2}'
#       .format(time.strftime("%X",time.localtime(start_timer)), time.strftime("%X",time.localtime(end_timer)),
#               end_timer-start_timer))
#
# # O/P-->
# # Press any key to Stop
# # Starting Time : 00:12:29
# # Ending time : 00:12:30
# # Elapsed Time : 0.5
# # we can see it is not showing right time
#
# print()
# print('*'*80)
# # Using process_time class;
# # It returns hoe much time CPU takes to complete the process
#
# import time, random
# from time import process_time as myTimer
#
# input('Press any key to Start\n')
# time.sleep(random.randint(1,2))
# start_timer = myTimer()
# input("Press any key to Stop ")
# end_timer = myTimer()
# print('Starting Time : {0}\nEnding time : {1}\nElapsed Time : {2}'
#       .format(time.strftime("%X",time.localtime(start_timer)), time.strftime("%X",time.localtime(end_timer)),
#               end_timer-start_timer))
#
#
# # O/P-->
# # Starting Time : 05:30:00
# # Ending time : 05:30:00
# # Elapsed Time : 0.0

print()
print('*'*100)
print()

# Using 'datetime' module:

from datetime import  datetime as dt

print(dt.now())
print(dt.today())
# Both give same value but now() is more precised

# We can use an external library named 'pytz' to handle complex time and timezones
