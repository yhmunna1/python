numbers = [12, 56, 98, 78, 56, 12, 6, 98]


# {key: value, key: value, key: value}
person = {'name': 'Kala Chan', 'address': 'Kalipur', 'age': 23, 'job': 'bekar'}
print(person)
print(person['name'])
print(person.keys())
print(person.values())

# Add new
person['language'] = 'python'
print(person)

# Change name:
person['name'] = 'Lal chan'
print(person)

# Delete age:
del person['age']
print(person)


# Special dictionary loop
for key, value in person.items():
    print(key, value)