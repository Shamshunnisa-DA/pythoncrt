#14 Armstrong Number or not
N = int(input())
Number = str(N)
output = 0
for i in Number:
    output += int(i) ** len(Number)
if output == N:
    print("YES")
else:
    print("NO")

