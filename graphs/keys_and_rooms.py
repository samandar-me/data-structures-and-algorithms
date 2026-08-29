from typing import List

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        if not rooms:
            return False

        visited = set()
        stack = [0]

        while stack:
            node = stack.pop()

            if node in visited:
                continue

            visited.add(node)

            for neighbor in rooms[node]:
                stack.append(neighbor)


        return len(visited) == len(rooms)
