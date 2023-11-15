import pprint
import myCats


# cats = [{'name': 'Zophie', 'desc': 'chubby'}, {'name': 'Pooka', 'desc': 'fluffy'}]
# print(pprint.pformat(cats))

# file_obj = open('myCats.py', 'w')
# file_obj.write('cats =' + pprint.pformat(cats) + '\n')

print(myCats.cats)
print(myCats.cats[0])
print(myCats.cats[0]['name'])