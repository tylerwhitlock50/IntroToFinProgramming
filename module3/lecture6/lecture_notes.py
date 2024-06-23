li = []
li.append('Senatus')
li.append('Populusque')
li.append('Romanus')
print(li)

li.insert(1, 'Roman')

print(li)
print(li[1])

di = {}
di['t'] = 'Tyler'
di['g'] = 'Glen'
di['w'] = 'Whitlock'

print(di)

li1 = ['t', 'g', 'w']
for i in li1:
    print(di[i])

print(di.keys())
print(di.values())
print(di.items())

val = di.pop('t')
print(di, 'Popped value:', val)

print(di.get('t', 'Not found'))
del(di['g'])

print(di.get('t', 'Not found'))

import string # build a dictionary that maps letters to numbers
letters = list(string.ascii_lowercase)
numbers = list(range(1, 27))
letter_number_dict = dict(zip(letters, numbers))
print(letter_number_dict)

for key, value in letter_number_dict.items():
    print(key, value)

letter_number_dict['aa'] = letter_number_dict.get('aa', 'not found')
print(letter_number_dict.get('aa'))