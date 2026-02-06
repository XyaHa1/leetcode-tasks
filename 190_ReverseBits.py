class Solution:
    def reverseBits(self, n: int) -> int:
        reverse_num_b = bin(n)[:1:-1]
        return int(f"{reverse_num_b}{"0" * (32 - len(reverse_num_b))}", 2)
    