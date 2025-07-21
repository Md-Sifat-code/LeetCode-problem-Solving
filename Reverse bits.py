class Solution:
    def reverseBits(self, n: int) -> int:
        binary_list = list(format(n,'032b'))
        print(binary_list)
        x = binary_list[::-1]
        print(x)
        binary_str = ''.join(x)
        result = int(binary_str,2)
        print(result)
        return result