from collections import namedtuple

''' Different between sort() and sorting()'''

''' Sorted is a Python built-in Function That Works on any iterable, it returns the modified Iterable but doesn't change the original '''

''' Sort() is a method that Works only on a list , it returns None and modify the original list '''

''' They both have a key parameter that used to sort based on what the key function returns '''

''' They both have a reverse parameter you can set it to True or False '''

a_list = [1, 2, 15, 47, 85, 4, 0, -8, 11, 110, 6, 2]


print(sorted(a_list))
a_list.sort(reverse=True)
print(a_list)


Student = namedtuple('Student', 'id name age')

s_list = [Student(1, 'alan', 24), Student(2, 'creg', 30), Student(4, 'sam', 15)]

''' Let sort those student by age '''
print('Sort by age')
print(sorted(s_list, key=lambda x : x.age))

''' Let Sort them by name'''
print('Sort by name')
s_list.sort(key=lambda x : x.name)

print(s_list)

''' x, y and z coordinates let say '''

l_listes = [ [-1, 0, 4], [-5, 1, 10], [5, 5, -7], [0, 0, 0] ]

''' Sort by Z '''

print('Sort By Z coordinate')
l_listes.sort(key = lambda x : x[2])

print(l_listes)

print('Sort a dict')
''' it will Sort based on key and returns a list of sorted keys '''
m_dict = {1: 'D', 0: 'B', 2: 'B', 4: 'E', 5: 'A'}
print(sorted(m_dict))

print('Sorted by Value')
for item in sorted(m_dict, key=lambda x : m_dict[x]):
	print('{0}:{1}'.format(item, m_dict[item]), end=' ')
print()