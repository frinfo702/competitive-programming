from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        def backtrack(start_idx, path):
            result.append(path.copy())  # ポインタではなくオブジェクトを渡すため

            for i in range(start_idx, len(nums)):
                backtrack(i + 1, path + [nums[i]])

        backtrack(0, [])
        return result
