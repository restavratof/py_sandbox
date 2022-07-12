import csv
import pprint
from collections import Counter
from collections import defaultdict

# -------------------------------------------------------------------------
print('-'*50)
print('-'*3, 'Counter')
str1 = 'qwueitjihqgnjsf;gnjrmypoukjo[aueigrvfybnjtykjh[iowjaesrotjy[iore'
c = Counter(str1)
print(c)

# -------------------------------------------------------------------------
print('-'*50)
print('-'*3, 'defaultdict')
d = defaultdict(list)
d['spam'].append(42)
d['blah'].append(12)
d['spam'].append(10)

print(d)

# -------------------------------------------------------------------------
print('#'*80)
print('#'*3, 'FOOD INSPECTION')

file_name = 'Food_Inspections.csv'
# file_name = 'restaurant-and-food-inspections-1.csv'
rest_food_insp_file = f'/home/dfashchanka/PycharmProjects/_workdata/{file_name}'
food = list(csv.DictReader(open(rest_food_insp_file)))
print(f'rows number: {len(food)}')
pp = pprint.PrettyPrinter(indent=4)
pp.pprint(food[0])

print('-'*30)
print('-', 'Results:')
results = {row['Results'] for row in food}
pp.pprint(results)


print('-'*30)
print('-', 'Number of failed results:')
fail = [row for row in food if row['Results'] == 'Fail']
pp.pprint(len(fail))

print('-'*30)
print('-', 'First failed:')
pp.pprint(fail[0])

# print('-'*30)
# print('-','Inspection Types:')
# insp_types = { row['Inspection Type'] for row in food }
# pp.pprint(insp_types)

# Complaint
print('-'*30)
print('-', 'compliant:')
compliant = [row for row in food if (row['Inspection Type'] == 'Complaint' and row['Results'] == 'Fail')]
pp.pprint(len(compliant))

print('-'*30)
print('-', 'Worst places:')
fail = [{**row, 'DBA Name': row['DBA Name'].replace("'", '').upper()} for row in fail]
worst = Counter(row['DBA Name'] for row in fail)
pp.pprint(worst.most_common(5))

print('-'*30)
print('-', 'Worst street:')
bad = Counter(row['Address'] for row in fail)
pp.pprint(bad.most_common(5))

print('-'*30)
print('-', 'Worst by year:')
by_year = defaultdict(Counter)
for row in fail:
    by_year[row['Inspection Date'][-4:]][row['Address']] += 1
pp.pprint(by_year['2020'].most_common(5))

print('-'*30)
print('-', 'Worst street:')
bad = Counter(row['Address'] for row in fail)
pp.pprint(bad.most_common(5))
