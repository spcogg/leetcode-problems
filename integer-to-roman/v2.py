# uses loop through dict only, however actually a lot slower
# than when looping through array to find next value
# 140ms, 13.6mb
class Solution:
    def intToRoman(self, num: int) -> str:
        if num < 1:
            return ""
        rom_nums = {
            1000:"M",
            900:"CM",
            500:"D",
            400:"CD",
            100:"C",
            90:"XC",
            50:"L",
            40:"XL",
            10:"X",
            9:"IX",
            5:"V",
            4:"IV",
            1:"I"
        }
        # rom_vals = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        ans = ""
        # num = 1994
        while num > 0:
            for key, v in rom_nums.items():
                print(key)
                if num - key >= 0:
                    num -= key
                    ans += v
                    print(ans)
                    break
        return ans

