from typing import List

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for asteroid in asteroids:
            alive = True

            while stack and stack[-1] > 0 and asteroid < 0:
                top = stack[-1]

                if top < abs(asteroid):
                    stack.pop()

                elif top == abs(asteroid):
                    stack.pop()
                    alive = False
                    break

                else:
                    alive = False
                    break

            if alive:
                stack.append(asteroid)

        return stack

    # def asteroidCollision(self, asteroids: List[int]) -> List[int]:
    #     stack = []
    #
    #     for asteroid in asteroids:
    #         if asteroid < 0:
    #             if not stack:
    #                 stack.append(asteroid)
    #                 continue
    #
    #             last_element = stack[-1]
    #
    #             if last_element < 0:
    #                 stack.append(asteroid)
    #             else:
    #                 temp_asteroid = 0
    #                 while stack:
    #                     last_element = stack.pop()
    #
    #                     if last_element < 0:
    #                         stack.append(last_element)
    #                         stack.append(asteroid)
    #                         break
    #
    #                     if abs(asteroid) == abs(last_element):
    #                         temp_asteroid = 0
    #                         break
    #
    #                     if abs(asteroid) > abs(last_element):
    #                         temp_asteroid = asteroid
    #                         continue
    #                     elif abs(last_element) > abs(asteroid):
    #                         stack.append(last_element)
    #                         break
    #
    #                     if last_element < 0:
    #                         stack.append(last_element)
    #
    #                         if temp_asteroid != 0:
    #                             stack.append(temp_asteroid)
    #                         break
    #
    #                 if not stack and temp_asteroid != 0:
    #                     stack.append(temp_asteroid)
    #                     continue
    #         else:
    #             stack.append(asteroid)
    #
    #     return stack