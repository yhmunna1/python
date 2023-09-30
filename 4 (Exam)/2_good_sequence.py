from collections import Counter
n = int(input())

sequence = list(map(int, input().split()))

element_count = Counter(sequence)

min_removals = 0

for element, count in element_count.items():
    if count > element:
        min_removals += count - element
    elif count < element:
        min_removals += count
print(min_removals)
