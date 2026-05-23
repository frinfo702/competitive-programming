x: int = int(input())
q: int = int(input())

nums = []
nums.append(x)

pairs = [input().split() for _ in range(q)]

for i, (a, b) in enumerate(pairs):
    nums.append(a)
    nums.append(b)

    sorted_index_to_origin_index = {}
    for i, num in enumerate(nums):
        sorted_index_to_origin_index[i] = i

    sorted_index_to_origin_index
    n = len(nums)
    median_index = n // 2
    nums
