from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        回転ソート配列では、任意の点で二つに分けたときそのうち片方は必ずソートされた配列になっている。
        これを利用して、ソートされた範囲のみを見るようにして、その部分に二分探索を適用する(三項比較の部分)
        """

        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            # 左スライスがソートされている時
            if nums[0] <= nums[mid]:
                if nums[0] <= target <= nums[mid]:
                    right = mid  # midは条件を満たす候補なので含める
                else:
                    left = mid + 1  # midは条件を満たさない候補なので含めない
            # 右スライスがソートされている場合
            else:
                if nums[mid] < target <= nums[-1]:
                    left = mid + 1  # midは条件を満たさない候補なので含めない
                else:
                    right = mid  # midは条件を満たす候補なので含める

        return left if nums[left] == target else -1
