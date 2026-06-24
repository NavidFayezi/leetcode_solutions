class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        res = []
        self.backtrack([], 1, n, res, k)
        return res
    
    def backtrack(self, path, begining, end, result, k):
        if len(path) == k:
            result.append(path[:])
            return None

        else:
            for i in range(begining, end + 1):
                path.append(i)
                self.backtrack(path, i + 1, end, result, k)
                path.pop()
        return None
