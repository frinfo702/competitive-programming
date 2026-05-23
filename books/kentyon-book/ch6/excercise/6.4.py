from typing import List


class Solution:
    def possible(self, d: int, a: List[int], m: int) -> bool:
        count = 1  # 最初の小屋は必ず選ぶから
        prev = a[0]
        for i in range(1, len(a)):
            if a[i] - prev >= d:
                count += 1
                prev = a[i]
            if count == m:
                return True

        return False

    def agressive_cows(self, a: List[int], m: int) -> int:
        left = 0
        right = a[-1] - a[0]

        while right > left:
            mid = (right + left + 1) // 2  # 区間更新を保証して無限ループを避ける
            if self.possible(mid, a, m):
                left = mid
            else:
                right = mid - 1  # midは条件を満たさないのでmid-1以下を探す

        return left
