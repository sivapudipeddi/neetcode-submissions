class Solution:
    def reverseBits(self, n: int) -> int:

        # 1. Convert to binary string, strip '0b', and pad to 32 bits
        binary_str = bin(n)[2:].zfill(32)
        
        # 2. Reverse the entire string
        binary_str_rev = binary_str[::-1]
        
        # 3. Convert that reversed binary string back to an integer
        return int(binary_str_rev, 2)