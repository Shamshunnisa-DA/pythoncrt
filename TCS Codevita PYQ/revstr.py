Str = input().split()
print(list(map(lambda i:Str[-i-1],range(len(Str)))))