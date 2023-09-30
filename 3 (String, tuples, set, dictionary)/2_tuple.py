def multiple():
    return 3, 4
# print(multiple())

things = 'pen', 'tripod', 'water'
print(type(things))
print(things[1])

if 'water' in things:
    print('Exists')

for item in things:
    print(item)

print(len(things))

mega = ([2, 3, 4], [6, 7, 8, 9])
mega[0][2] = 444
print(mega)