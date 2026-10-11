from collections import deque

class Solution:
    def countStudents(self, students: list[int], sandwiches: list[int]) -> int:
        students = deque(students)
        sandwiches = deque(sandwiches)
        counter = 0

        while students:
            if counter == len(students):
                break

            if students[0] == sandwiches[0]:
                students.popleft()
                sandwiches.popleft()
                counter = 0
            else:
                students.append(students.popleft())
                counter += 1

        return len(students)