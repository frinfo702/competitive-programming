import bisect
from typing import List


class Solution:
    def darts(self, a: List[int], m: int):
        two_sum = []
        for ai in a:
            for aj in a:
                two_sum.append(ai + aj)

        two_sum.sort()
        answer = 0

        for x in two_sum:
            if m - x < 0:
                continue
            # bisect_right: targetより大きい値が初めて現れる位置
            # -1をするとm-x以下の値のうち最大の値のindex
            # leftはtarget以上の値が初めて現れる位置なのでズレる(target==m-xの場合)
            max_index = bisect.bisect_right(two_sum, m - x) - 1
            if max_index >= 0:
                candidate = x + two_sum[max_index]
                answer = max(candidate, answer)

        return answer


s = Solution()
assert s.darts([3, 14, 15, 9], 50) == 48
