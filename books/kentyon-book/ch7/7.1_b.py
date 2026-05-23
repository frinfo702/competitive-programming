from typing import List


class Solution:
    """
    500円玉，100円玉，50円玉，５円玉，１円玉がそれぞれ a0, a1, a2, a3, a4, a5 枚あります
    これらを用いて X 円を支払いたいとします．
    ここで，支払いに用いるコインの合計枚数をなるべく少なくしたいと考えています．
    最小で何枚のコインで支払うことができるでしょうか．ただし，そのような支払い方が少なくとも１つは存在するものとします．
    """

    COIN_VALUES = [500, 100, 50, 10, 5, 1]

    def solve(self, coin_nums: List[int], X: int) -> int:
        if len(coin_nums) != 6:
            raise ValueError(f"coin_nums must have {len(self.COIN_VALUES)} elements")
        if X < 0 or any(c < 0 for c in coin_nums):
            raise ValueError("inputs must be non-negative")

        remaining = X
        total_coins = 0
        # 貪欲法
        for coin_value, coin_num in zip(self.COIN_VALUES, coin_nums):
            use = min(X // coin_value, coin_num)

            remaining -= coin_value * use
            total_coins += use

        if remaining != 0:
            raise ValueError("X cannot be paid with given coins")

        return total_coins
