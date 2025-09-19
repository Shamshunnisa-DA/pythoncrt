#10.Print the first N Fibonacci numbers.
N = int(input())
a, b = 0, 1
for _ in range(0,N):
    print(a, end=' ')
    a, b = b, a + b