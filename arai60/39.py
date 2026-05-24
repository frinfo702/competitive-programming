from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        def backtrace(start_idx: int, current_nums: List[int], current_sum: int):
            if current_sum == target:
                result.append(current_nums)
                return
            elif current_sum > target:
                return

            for i in range(start_idx, len(candidates)):
                backtrace(
                    i, current_nums + [candidates[i]], current_sum + candidates[i]
                )

        backtrace(0, [], 0)
        return result
