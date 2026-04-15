class Solution:
    def countBits(self, n: int) -> List[int]:
        list1 = []
        for i in range(n+1):
            list1.append(bin(i).count("1"))
        return list1