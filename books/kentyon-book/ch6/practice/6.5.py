from typing import List


class Solution:
    def min_max_penalty(self, H: List[int], S: List[int]) -> int:
        """
        H[i]: 風船iの初期高度
        S[i]: 風船iの1秒あたりの上昇速度
        戻り値：最終的なペナルティ（割った時の高度の最大値）の最小値
        """

        N = len(H)

        # 最大ペナルティをx以下にできるか？
        def can(x: int) -> bool:
            time_limits = []
            for hi, si in zip(H, S):
                if x < hi:
                    return False
                t = (x - hi) // si  # ペナルティを受けた場合の時刻
                time_limits.append(t)

            time_limits.sort()
            for i, limit in enumerate(time_limits):
                # i番目に割る風船は時刻iに割る
                if limit < i:
                    return False

            return True

        # 二分探索の上限は全ての風船を最後の時刻(N-1)に割った場合の最大ペナルティ
        right = (
            max(hi + si * (N - 1) for hi, si in zip(S, H)) + 1
        )  # 常に解ける領域にある
        left = 0  # 常に解けない領域

        while right - left > 1:
            mid = (left + right) // 2
            if can(mid):
                right = mid
            else:
                left = mid

        return right
