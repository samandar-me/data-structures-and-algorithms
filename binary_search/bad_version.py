class Solution:
    def firstBadVersion(self, n: int) -> int:
        left = 0
        right = n - 1

        while left <= right:
            mid = left + ((right - left) // 2)
            if self.isBadVersion(mid):
                right = mid - 1
            else:
                left = mid + 1

        return left

    def isBadVersion(self, version: int) -> bool:
        return True if version == 1 else False