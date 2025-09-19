#17
A = int(input())
B = int(input())
# li = []
# for i in range(1,max(A,B)+1):
#     if A%i==0 and B%i==0:
#         li.append(i)
# print(max(li))
def gcd(A,B):
    return A if B == 0 else gcd(B,A%B)
print(gcd(A,B))