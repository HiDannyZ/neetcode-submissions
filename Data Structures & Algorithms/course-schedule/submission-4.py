class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # This is a graph problem -> TC expect of O(E + V)
        # V is the courses
        # E is the connection of pre-req

        # Draft an Adjacency List - Determines the preReqs of each course since each course can have 0 or more courses as pre-req
        courseMap = defaultdict(list)

        for course, preReq in prerequisites:
            courseMap[course].append(preReq)
        
        # Concern: Cycle
        cycleCheck = set()

        for course in range(numCourses):
            if not self.dfs(course, courseMap, cycleCheck):
                return False
        return True

        
    # We will search through the adjacency list if it's completeable
    def dfs(self, course, courseMap, cycleCheck):
        # Base Case
        if courseMap[course] == []:
            return True
        if course in cycleCheck:
            return False

        cycleCheck.add(course)
        preReqCourses = courseMap[course]
        for preReqCourse in preReqCourses:
            if not self.dfs(preReqCourse, courseMap,cycleCheck):
                return False
        cycleCheck.remove(course)
        # we confirmed that we can reach the end for this one
        courseMap[course] = []
        return True
        

        