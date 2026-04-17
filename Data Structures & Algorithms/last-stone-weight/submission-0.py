class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) >= 2:
            stones = sorted(stones, reverse=True)
            a = stones.pop(0)
            b = stones.pop(0)
            
            if a != b:
                stones.append(a - b)

        return stones[0] if stones else 0