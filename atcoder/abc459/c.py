n, q = map(int, input().split())
queries = [input().split() for _ in range(q)]

blocks = [0] * n


def isLoadedAll(blocks: list[int]) -> bool:
    for block in blocks:
        if block == 0:
            return False
    return True


seen = set()
for i in range(q):
    query = queries[i]
    query_head = query[0]
    num_in_query = int(query[1])
    if query_head == "1":
        blocks[num_in_query - 1] += 1
        if num_in_query not in seen:
            seen.add(num_in_query)
        if len(seen) == n:
            blocks = [block - 1 for block in blocks]
            seen.clear()

    elif query_head == "2":
        count = 0
        for block in blocks:
            if block >= num_in_query:
                count += 1
        print(count)
