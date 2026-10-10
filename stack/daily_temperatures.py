class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        n = len(temperatures)
        result = [0] * n
        stack = []

        for i, num in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < num:
                previous_index = stack.pop()
                result[previous_index] = i - previous_index

            stack.append(i)

        return result


    # def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
    #     n = len(temperatures)
    #     result = [0] * n
    #
    #     for i in range(n):
    #         for j in range(i+1, n):
    #             if temperatures[i] < temperatures[j]:
    #                 result[i] = j - i
    #                 break
    #
    #     return result