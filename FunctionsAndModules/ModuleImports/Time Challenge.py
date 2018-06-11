
# About get_clock_info()
# time.get_clock_info(name)
# Get information on the specified clock as a namespace object.
# Supported clock names and the corresponding functions to read their value are:
#
# 'clock': time.clock()
# 'monotonic': time.monotonic()
# 'perf_counter': time.perf_counter()
# 'process_time': time.process_time()
# 'time': time.time()

# The result has the following attributes:

# adjustable: True if the clock can be changed automatically (e.g. by a NTP daemon)
#             or manually by the system administrator, False otherwise
# implementation: The name of the underlying C function used to get the clock value.
#                  Refer to Clock ID Constants for possible values.
# monotonic: True if the clock cannot go backward, False otherwise
# resolution: The resolution of the clock in seconds (float)

from time import time as my_timer
from time import perf_counter, monotonic, process_time
import time

print('Time Clock INFORMATION\n')

print('Time : '+ time.strftime('%X',time.localtime(my_timer()))+ "\n")
description = time.get_clock_info('time')
print('Adjustable : {0}\n' 
      'Implementation : {1}\n' 
      'Monotonic : {2}\n'
      'Resolution : {3}\n'
      .format(description.adjustable, description.implementation, description.monotonic, description.resolution))


print('Perf_counter Clock INFORMATION\n')

print('Time : '+ time.strftime('%X',time.localtime(perf_counter()))+ "\n")
description = time.get_clock_info('perf_counter')
print('Adjustable : {0}\n'
      'Implementation : {1}\n'
      'Monotonic : {2}\n'
      'Resolution : {3}\n'
      .format(description.adjustable, description.implementation, description.monotonic, description.resolution))

print('Monotonic Clock INFORMATION\n')

print('Time : '+ time.strftime('%X',time.localtime(monotonic()))+ "\n")
description = time.get_clock_info('monotonic')
print('Adjustable : {0}\n'
      'Implementation : {1}\n'
      'Monotonic : {2}\n'
      'Resolution : {3}\n'
      .format(description.adjustable, description.implementation, description.monotonic, description.resolution))


print('Process Time Clock INFORMATION\n')

print('Time : '+ time.strftime('%X',time.localtime(process_time()))+ "\n")
description = time.get_clock_info('process_time')
print('Adjustable : {0}\n'
      'Implementation : {1}\n'
      'Monotonic : {2}\n'
      'Resolution : {3}\n'
      .format(description.adjustable, description.implementation, description.monotonic, description.resolution))


