from collections import deque

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        d_queue, r_queue = deque(), deque()

        for i in range(len(senate)):
            if senate[i] == "R":
                r_queue.append(i)
            else:
                d_queue.append(i)

        while d_queue and r_queue:
            d_turn = d_queue.popleft()
            r_turn = r_queue.popleft()

            if r_turn < d_turn:
                r_queue.append(r_turn + len(senate))
            else:
                d_queue.append(d_turn + len(senate))

        return "Radiant" if r_queue else "Dire"