s: str = input()
n: int = int(input())

s_without_prefix = s[n:]
s_without_postfix = s_without_prefix[:-n]

print(s_without_postfix)
