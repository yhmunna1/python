# Lambda:

# Type-1:
# def doubled(x):
#     return x*2

# Type-2:
doubled = lambda num : num *2

result = doubled(44)
print(result)


numbers = [12, 56, 98, 78, 56, 12, 6, 98]
# doubled_nums = map(doubled, numbers)
doubled_nums = map(lambda x: x*2, numbers)

print(numbers)
print(list(doubled_nums))


# Find the actress who is under 40
actors = [
    {'name': 'sabana', 'age': 65},
    {'name': 'makela', 'age': 25},
    {'name': 'khaleka', 'age': 30},
    {'name': 'daleka', 'age': 35},
    {'name': 'haleka', 'age': 40},
]

juniors = filter(lambda actor : actor['age'] <40, actors)
print(list(juniors))