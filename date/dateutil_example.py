from dateutil import parser

str1 = '2019-08-28T14:34:25.518993Z'
str2 = '2020-04-09T03:31:37.846Z'

date1 = parser.isoparse(str1)
print(date1)
print(type(date1))
date2 = parser.parse(str2)
print(date2)
print(type(date2))