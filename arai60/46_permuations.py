from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []

        def backtrack(path, used):
            # 基底ケース：パスが完成したら結果に追加
            if len(path) == len(used):
                result.append(path[:])
                return

            for i in range(len(nums)):
                if used[i]:
                    continue

                # 選択
                used[i] = True
                path.append(nums[i])

                # 探索：次の要素を選ぶ
                backtrack(path, used)

                # 戻る：選択を取り消す(backtrack)
                path.pop()
                used[i] = False

        backtrack([], [False] * len(nums))
        return result
