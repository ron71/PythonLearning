# to install pytz module :
# In cmd : 'pip3 install pytz'

import pytz
import datetime
# this module is generally used for creating 'tzinfo' object via time timezone object
# by providing country name

country = 'Chile/Continental'
tzOfUS = pytz.timezone(country)
localTimeOfUs = datetime.datetime.now(tz=tzOfUS)
print('Local Time of {} : {}'.format(country, localTimeOfUs))
print('UTC Time : {}'.format(datetime.datetime.utcnow()))
# utcnow() returns current utc time i.e. (local time - 5:30)

# Its hard to find the country name compatible with timezone method.
# Therefore this module has a list of all the acceptable country names for time zone
# We can print the list by using list name : 'all_timezone'
print('*'*100)
for t in pytz.all_timezones:
    print(t)

print("*"*100)

# We can also use country code for getting the timezone of the country
# This module has a built in dictionary for the country codes.

for code in pytz.country_names:
    print("{} : {}".format(code, pytz.country_names[code]))
# How ever it is nor recommended to use country codes as many country have more than on timezone timezone
print("*"*100)
print()

# we can print whole list of ountry and there different timezone names

for code in sorted(pytz.country_names):
    print("{} : {} : {}".format(code, pytz.country_names.get(code), pytz.country_timezones.get(code)))
# NOTE : We used get() method so that if any country donot has time zone it will return None, for ex.'BV: Bouvet Island'

print()
print('line No : 41\t'* 100)
print()

# well we can print time of each timezone :
for code in sorted(pytz.country_names):
    print('{} : {}'.format(code, pytz.country_names[code]), end=':')
    if code in pytz.country_timezones:
        for zone in sorted(pytz.country_timezones[code]):
            countryTimeZone = pytz.timezone(zone)
            localTime = datetime.datetime.now(countryTimeZone)
            print('\t\t{} : {}'.format(countryTimeZone, localTime))
    else:
        print('\t\tNo Time Zone Found')