class Solution:
    def toHex(self, num: int) -> str:
        # Chech if num is 0 and return 0
        if num == 0:
            return ("0")
        # Initalize hex representation chars
        hex_representation = ['0', '1', '2', '3', '4', '5',
                              '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
        # Initalize string to carry hex representation
        hex_represent = ""
        # Check if num is negative and add to power 2**32
        if num < 0:
            num = pow(2, 32) + num
        # Loop and compute hex
        while (num != 0):
            remain = num % 16
            base = int((num - remain) / 16)
            hex_represent = hex_representation[remain] + hex_represent
            num = base
        return hex_represent
