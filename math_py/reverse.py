class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return 0
        zero_count = 0
        x = str(x)
        n = len(x)

        for i in range(n-1, -1, -1):
            if x[i] == "0":
                zero_count += 1
            if x[i] != "0":
                break

        left = 0
        right = n - zero_count - 1
        ans = [""] * (right + 1)

        if x[0] == "-":
            left += 1
            ans[0] = "-"

        while left <= right:
            temp = x[left]
            ans[left] = x[right]
            ans[right] = temp
            left += 1
            right -= 1

        res = int("".join(ans))
        if res < -2**31 or res > 2**31-1:
            return 0

        return res
