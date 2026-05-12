import bisect
from typing import List


class Solution:
    def snuke_festival(self, A: List[int], B: List[int], C: List[int]):
        A.sort()
        C.sort()

        N = len(A)
        ans = 0

        # O(NlogN)
        for bj in B:
            count_a = bisect.bisect_left(A, bj)  # a_i < b_jの個数
            count_c = N - bisect.bisect_right(C, bj)  # b_j < c_kの個数
            ans += count_a * count_c

        return ans
