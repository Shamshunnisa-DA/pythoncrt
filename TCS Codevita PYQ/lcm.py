A = int(input())
B = int(input())
def gcd(A,B):
    return A if B == 0 else gcd(B,A%B)
def lcm(A,B):
    return (A*B)//gcd(A,B)
print(lcm(A,B))