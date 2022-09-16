from typing import List
class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        # when is not valid?
        # first byte is not 0x, 110x, 1110x, 11110x
        # or, when parsing a new character, the data list is empty, or next byte is not 10x
        byte_remain = 0
        for byte in data:
            # read a new character
            if byte_remain == 0:
                if byte >> 7 == 0 : # 1-byte character
                    continue
                elif byte >> 5 == 0b110: # 2-byte character
                    byte_remain = 1
                elif byte >> 4 == 0b1110: # 3-byte character
                    byte_remain = 2
                elif byte >> 3 == 0b11110: # 4-byte character
                    byte_remain = 3
                else:
                    return False
            # continue parse existing character
            else:
                if byte >> 6 == 0b10: # start with 10x
                    byte_remain -= 1
                else:
                    return False
        
        return byte_remain == 0
                


if __name__ == "__main__":
    data = [197,130,1]
    assert Solution().validUtf8(data) == True

    data = [235,140,4]
    assert Solution().validUtf8(data) == False