#15. Check if two strings are anagrams of each other.
S1 = input().lower()
S2 = input().lower()
count = 0
if len(S1) == len(S2):
    for i in S1:
        if i in S2 :
            count += 1
res = "YES" if count == len(S1) else "NO"
print(res)