s = input()


def isNumber(char: str) -> bool:
    try:
        char_int = int(char)
        if char_int in {1, 2, 3, 4, 5, 6, 7, 8, 9, 0}:
            return True
    except ValueError:
        pass

    return False


result = []

for char in s:
    if isNumber(char):
        result.append(char)

ans = "".join(result)
print(ans)
