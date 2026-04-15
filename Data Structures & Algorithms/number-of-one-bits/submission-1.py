class Solution:
    def hammingWeight(self, n: int) -> int:
        binary1 = bin(n)
        counter = 0
        for char in binary1:
            if char == "1":
                counter = counter + 1

        return counter
