# from dateutil import parser
from datetime import datetime

str1 = '2019-08-28T14:34:25.518993Z'
str2 = '2020-04-09T03:31:37.846Z'

# date1 = parser.isoparse(str1)
# print(date1)
# print(type(date1))
# date2 = parser.parse(str2)
# print(date2)
# print(type(date2))

print('-'*50)
print(f'ISO: {datetime.now().isoformat()}')


print('-'*50)
print('- Parse date string with datetime:')
str3 = '2021-07-07 14:36:30.979024'
print(f'IN : {str3}')
date_time_obj = datetime.strptime(str3, '%Y-%m-%d %H:%M:%S.%f')
print(f'OUT: {date_time_obj.isoformat()}')
