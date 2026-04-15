class Solution:
    def reverseBits(self, n: int) -> int:

        # 1. Convert to binary string, strip '0b', and pad to 32 bits
        binary_str = bin(n)[2:].zfill(32)

        binary_str_rev = binary_str[::-1]

        n2 = int(binary_str_rev,2)

        return n2

        