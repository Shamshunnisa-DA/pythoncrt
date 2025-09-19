#Rearrange integers so that even numbers come first, then odd numbers. Order must be preserved in both groups.
# Input Format:
# First line: integer N
# Second line: N space-separated integers
N = int(input())
li = list(map(int(input()).split()))
even = list(filter(lambda x:x%2==0,li))
print(even)
odd = list(filter(lambda y:y%2!=0,li))
print(odd)