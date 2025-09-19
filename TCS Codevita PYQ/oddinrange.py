#13. Print all odd numbers in a given range.
L= int(input())
R= int(input())
for i in range(L,R+1):
    if i%2!=0:
        print(i,end=' ')