# n = int(input())
# n=list(str(n))
# x = n.count('3') + n.count('7')
# print(x)
# 
n = int(input()).strip()
print(sum(1 for i in str(n) if i in ['3','7']))