class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        # Adjacency List
        coursesMap = defaultdict(list)

        for course, prereq in prerequisites:
            coursesMap[course].append(prereq)
        
        cycleCheck = set()
        completeAllCourses = set()
        path = []

        for course in range(numCourses):
            if not self.dfs(course, completeAllCourses, cycleCheck, coursesMap, path):
                return [] # Cycle detected
        
        return path

    def dfs(self,course,completeAllCourses,cycleCheck,coursesMap,path):
        
        # Base Case:
        if course in completeAllCourses:
            return True
        if course in cycleCheck: 
            return False
        
        cycleCheck.add(course)
        preReqCourses = coursesMap[course]
        for preReqCourse in preReqCourses:
            if not self.dfs(preReqCourse,completeAllCourses,cycleCheck,coursesMap,path):
                return False 
        completeAllCourses.add(course)
        cycleCheck.remove(course)
        path.append(course)
        return True


        



