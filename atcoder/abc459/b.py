n = int(input())
ss = input().split()
result_list = []
for term in ss:
    head = term[0]
    if head in {"a", "b", "c"}:
        result_list.append("2")
    elif head in {"d", "e", "f"}:
        result_list.append("3")
    elif head in {"g", "h", "i"}:
        result_list.append("4")
    elif head in {"j", "k", "l"}:
        result_list.append("5")
    elif head in {"m", "n", "o"}:
        result_list.append("6")
    elif head in {"p", "q", "r", "s"}:
        result_list.append("7")
    elif head in {"t", "u", "v"}:
        result_list.append("8")
    elif head in {"w", "x", "y", "z"}:
        result_list.append("9")

result = "".join(result_list)
print(result)
