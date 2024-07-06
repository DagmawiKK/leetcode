class Solution:
    def addBinary(self, a: str, b: str) -> str:
        def binary(string):
            count = 0
            m = 0
            for i in range(len(string)-1, -1, -1):
                if(string[i] == "1"):
                    m = m + (2**count)
                count += 1
            return m
        num1 = binary(a)
        num2 = binary(b)
        return str(bin(num1 + num2))[2:]

        
