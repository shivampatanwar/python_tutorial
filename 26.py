import time

times = time.strftime('%H:%M:%S')
print(times)
hours = time.strftime('%H')
print(hours)
# minuts = time.strftime('%M')
# print(minuts)
# seconds = time.strftime('%S')
# print(seconds)
# print(seconds)


if '0' < hours < '12':
    print('Good Morning')

elif '12' < hours < '16':
    print('Good Afternoon')

else:
    print('Good Evening')

#
# if hours < '12':
#     print('Good Morning')
#
# elif hours < '16':
#     print('Good Afternoon')
#
# else:
#     print('Good Evening')
