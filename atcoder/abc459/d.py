class Solution:
    def solve(self, case: str) -> str:
        char_to_cnt = {}
        for char in case:
            char_to_cnt[char] = char_to_cnt.get(char, 0) + 1
        most_frequent = max(char_to_cnt.values())
        if (len(case) + 1) // 2 >= most_frequent:
            return "Yes"
        # ここで並び替え処理
        return "No"


if __name__ == "__main__":
    t: int = int(input())
    sol = Solution()
    for _ in range(t):
        case: str = input()
        canSort = sol.solve(case)
        print(canSort)
