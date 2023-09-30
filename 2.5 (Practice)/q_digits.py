def print_reverse(n):
    reversed_n = ' '.join(n[::-1])
    print(reversed_n)

t = int(input())
for _ in range(t):
    n= input()
    print_reverse(n)