phoneBook = {
    'Savannah' : '476', 
    'Rahul' : '1324'
}

print(phoneBook.get('Rahul'))

info = {}
info['name'] = 'Sandy'
info['occupation'] = 'Hacker'

print(info.get('name'))

info.pop('name')
print(info)
print(info.get('occupation'))