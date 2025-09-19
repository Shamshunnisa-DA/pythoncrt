#return the length of the word which is big from given sentence
Str = list(input().split())
print(Str)
print(len(max(Str, key = len)))