from typing import List


class Solution:
    def coordinate_compression(self, A: List[int]):
        value_and_index = []
        for index, original_index in enumerate(A):
            value_and_index.append((original_index, index))

        value_and_index.sort(key=lambda x: x[0])

        rank = [0] * len(a)
        for i, (_, idx) in enumerate(value_and_index):
            rank[idx] = i

        return rank


s = Solution()
a = [12, 43, 7, 15, 9]
ans = s.coordinate_compression(a)
assert ans == [2, 4, 0, 3, 1]
