from typing import List


class Solution:
    """
    500円玉，100円玉，50円玉，５円玉，１円玉がそれぞれ a0, a1, a2, a3, a4, a5 枚あります
    これらを用いて X 円を支払いたいとします．
    ここで，支払いに用いるコインの合計枚数をなるべく少なくしたいと考えています．
    最小で何枚のコインで支払うことができるでしょうか．ただし，そのような支払い方が少なくとも１つは存在するものとします．
    """

    _COIN_VALUES = [500, 100, 50, 10, 5, 1]

    def solve(self, coin_nums: List[int], X: int):
        if len(coin_nums) != 6:
            raise ValueError

        result = 0
        # 貪欲法
        for i in range(len(self._COIN_VALUES)):
            add = X // self._COIN_VALUES[i]
            if add > coin_nums[i]:
                add = coin_nums[i]

            X -= self._COIN_VALUES[i] * add
            result += add

        return result
