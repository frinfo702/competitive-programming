from typing import List


class Solution:
    def solve(self, s: List[int], t: List[int]):
        """
        区間スケジューリング問題:
        N 個の仕事があり，i(＝0, 1, ..., N－1) 番目の仕事は時刻 si に開始し，時刻 ti に終了します．
        これらの中から自分が行う仕事をできるだけ多く選びたいとします．
        ただし時刻が重なっている複数の仕事を選ぶことはできません．
        最大で何個の仕事をこなすことができるでしょうか．
        """
        if not s or not t:
            return 0

        intervals = sorted(zip(s, t), key=lambda x: x[1])  # O(NlogN)
        n = len(intervals)

        count = 1
        last_end = intervals[0][1]

        for i in range(1, n):
            start, end = intervals[i]
            if last_end <= start:
                count += 1
                last_end = end

        return count


if __name__ == "__main__":
    sol = Solution()
    s = [1, 3, 0, 5, 8, 5]
    t = [2, 4, 6, 7, 9, 9]
    assert sol.solve(s, t) == 4

    s = [9, 10, 11, 13, 15, 19]
    t = [12, 15, 16, 18, 19, 23]
    assert sol.solve(s, t) == 3

    s = []
    t = []
    assert sol.solve(s, t) == 0

    s = [1]
    t = [2]
    assert sol.solve(s, t) == 1

    s = [1, 1]
    t = [2, 2]
    assert sol.solve(s, t) == 1
    print("all test passed")
