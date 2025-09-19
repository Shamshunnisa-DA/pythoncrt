#11. Check if a number is prime or not.
N = int(input())
fact = 0
for i in range(1,N+1):
    if N%i==0:
        fact+=1
res = "YES" if fact==2 else "NO"
print(res)