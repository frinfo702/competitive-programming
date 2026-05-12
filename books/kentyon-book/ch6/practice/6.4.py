# std::lower_bound()はbisectが相当する

import bisect


class Solution:
    INF = 1 << 32

    def optimizePairSum(self, list_a: list[int], list_b: list[int], k: int) -> int:
        list_b = sorted(list_b)
        min_sum = self.INF

        # O(N)
        for a in list_a:
            sub = k - a
            min_index = bisect.bisect_left(list_b, sub)  # O(logN)

            if min_index < len(list_b):
                # 範囲外参照にならないようにチェック
                candidate = a + list_b[min_index]  # 和に戻すのを忘れない
                if min_sum > candidate:
                    min_sum = list_b[min_index]

        return min_sum
