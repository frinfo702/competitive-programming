from typing import List


class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        min_capacity = max(weights)
        max_capacity = sum(weights)

        def canCompleteWithin(weights: List[int], days: int, capacity: int) -> bool:
            """O(N), given with N of the length of weights"""
            required_days = 1
            current_weight = 0

            for w in weights:
                if current_weight >= capacity:
                    required_days += 1
                    current_weight = w
                    continue
                current_weight += w

            return required_days <= days

        left = min_capacity
        right = max_capacity
        while left < right:
            mid = (left + right + 1) // 2
            if canCompleteWithin(weights, days, mid):
                right = mid  # midで運べるならmid自身を残す
            else:
                left = mid + 1  # midで運べないならそれよりは大きい必要がある

        return left
