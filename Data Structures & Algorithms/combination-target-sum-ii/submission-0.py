class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # Unsorted candidates -> Impact is that we need to sort to avoid duplicates
        # TC: O(nlogn)
        candidates.sort()
        res = []

        # Since we are exploring every signle combination, we are expecting a backtreking problem
        # TC: O(2^n)
        self.dfs(0, 0, [], candidates, target, res)
        return res

    def dfs(self, index, currTotal, currArray, candidates, target, res):
        if currTotal == target:
            res.append(currArray.copy())
            return
        # handle duplicates:
        if index == len(candidates) or currTotal > target:
            return
        val = candidates[index]
        # We choose to add the current val
        currArray.append(val)
        self.dfs(index + 1, currTotal + val, currArray, candidates, target, res)
        # We chose to not add the curr Val
        currArray.pop()
        while index+1<len(candidates) and candidates[index + 1] == candidates[index]:
            index += 1
        self.dfs(index + 1, currTotal, currArray, candidates, target, res)
