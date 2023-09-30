s = input()
current_sub = ""
count = 0
substrings = []

for char in s:
    current_sub += char

    if current_sub.count('L') == current_sub.count('R'):
        count += 1
        substrings.append(current_sub)
        current_sub = ""

print(count)
for substring in substrings:
    print(substring)
