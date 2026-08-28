class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # We should construct an adjacency list
        # Key Course: prereq
        
        crsMap = defaultdict(list)
        for crs,prereq in prerequisites:
            crsMap[crs].append(prereq)
        
        visitedSet = set()
        
        for crs in range(numCourses):
            if not self.dfs(crs,visitedSet, crsMap):
                return False
        return True


    def dfs(self, crs,visitedSet, crsMap):
        
        if crs in visitedSet:
            return False

        if crsMap[crs] == []:
            return True

        visitedSet.add(crs)
        for newCrs in crsMap[crs]:
            if not self.dfs(newCrs,visitedSet, crsMap):
                return False
        visitedSet.remove(crs)
        crsMap[crs] = []
        return True
