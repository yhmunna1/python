n = int(input())
numbers = list(map(int, input().split()))
max_operations = 0

while all(num % 2 == 0 for num in numbers):
    numbers = [num // 2 for num in numbers]
    max_operations += 1

print(max_operations)
