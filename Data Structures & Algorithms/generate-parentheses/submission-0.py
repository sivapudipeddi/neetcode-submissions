class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        subset = []
        def dfs(open_n, closed_n):
            if open_n == closed_n == n:
                result.append("".join(subset))
                return 

            # Rule 1: Can we add an OPEN parenthesis?
            # This handles your "open_n == 0" case and any case where we haven't hit the limit.
            if open_n < n:
                subset.append("(")
                dfs(open_n + 1, closed_n)
                subset.pop() # Backtrack to clean the list for the next choice

            # Rule 2: Can we add a CLOSED parenthesis?
            # This matches your "closed_n < open_n" logic.
            if closed_n < open_n:
                subset.append(")")
                dfs(open_n, closed_n + 1)
                subset.pop() # Backtrack

        dfs(0,0)
        return result