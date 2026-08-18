class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # We should construct an adjacency list

        preReqMap = {i:[] for i in range(numCourses)}

        for course,prereq in prerequisites:
            preReqMap[course].append(prereq)
        
        # Avoid dup
        finishedCourses = set()

        for course in range(numCourses):
            if not self.dfs(course,preReqMap,finishedCourses):
                return False
        return True


    def dfs(self,course, preReqMap,finishedCourses):
        
        if course in finishedCourses:
            return False
        
        if preReqMap[course] == []:
            return True
        
        finishedCourses.add(course)

        for preReq in preReqMap[course]:
            if not self.dfs(preReq,preReqMap,finishedCourses):
                return False
        finishedCourses.remove(course)
        preReqMap[course] = []
        return True
