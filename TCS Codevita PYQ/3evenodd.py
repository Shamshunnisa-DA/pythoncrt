N = int(input())
li = list(map(int,input().split()))
print((list(filter(lambda x:x%2==0,li))) +(list(filter(lambda y:y%2!=0,li))))