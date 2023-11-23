from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # DFS on Adjacency list
        # Creating an adjacency map for every course from prerequisites
        preqs = {c: [] for c in range(numCourses)}
        for preq, course in prerequisites:
            preqs[course].append(preq)
        # Creating a visited set to store all visited vertices along DFS
        visited = set()

        # Defining DFS function which going to be used recursively for a graph search
        def dfs(course):
            # defining base case 1
            if course in visited:
                return False
            # defining base case 2
            if not preqs[course]:
                return True
            visited.add(course)
            for preq in preqs[course]:
                if not dfs(preq): return False
            visited.remove(course)
            preqs[course] = []
            return True

        # Execute DFS for every course from numCourses
        for course in range(numCourses):
            if not (dfs(course)):
                return False
        return True
