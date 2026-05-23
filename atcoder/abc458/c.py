s: str = input()


indiceToCount = [{i: 0} for i, char in enumerate(s) if char == "C"]
i = 0
for d in indiceToCount:
    for indice, count in d.items():
        headToIndice = indice
        indiceToTail = len(s) - indice - 1
        indiceToCount[i][indice] = min(headToIndice, indiceToTail) + 1
        i += 1

ans_count = 0
for d in indiceToCount:
    for _, count in d.items():
        ans_count += count

print(ans_count)
