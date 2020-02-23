import os

data_dir = 'DIRECTORY TO CHECK'

#--------------------------------------------
# SOLUTION FROM FORUM
for root, dirs, files in os.walk(data_dir):
    level = root.replace(data_dir, '').count(os.sep)
    indent = ' ' * 4 * (level)
    print('{}{}/'.format(indent, os.path.basename(root)))
    subindent = ' ' * 4 * (level + 1)
    for f in files:
        print('{}{}'.format(subindent, f))

print('---------------------------------------------------')
# MY SOLUTION WITH STORING TREE IN DICTIONARY
# And get files only in 2nd directory layer
mydict = {}

if os.path.isdir(data_dir):
    for subdir, dirs, files in os.walk(data_dir):
        # print('SUBDIR:{}   DIRS:{}    FILES:{}'.format(subdir, dirs, files))
        if subdir == data_dir:
            print("|{}".format(subdir))
            categories = dirs

        elif subdir.count('/') == 1:
            parent = subdir.split('/')[0]
            group = subdir.split('/')[1]
            print("|---{}".format(group))
            mydict[group] = {}

        elif subdir.count('/') == 2:
            section = subdir.split('/')[2]
            print("    |---{}".format(section))
            print("        |---{}".format(files))

            group = subdir.split('/')[1]
            print('SECT:{}'.format(section))
            mydict[group][section] = {}
            for f in files:
                topic = f.split('.')[0]
                print('f:{}'.format(topic))
                mydict[group][section][topic] = {}

    print('---------------------------------------------------')
    print('CATEGORIES:{}'.format(categories))
    print('MYDICT    :{}'.format(mydict))

