class Solution:
    def romanToInt(self, s: str) -> int:
        roman_integer = {"I" : 1,"V" : 5, "X" : 10, "L" : 50, "C" : 100, "D" : 500, "M" : 1000}
        splited = list(s)
        integer = 0
        i= 0
        while i < len(splited):
            if i+1 < len(splited) and roman_integer[splited[i]] < roman_integer[splited[i+1]]:
                integer += roman_integer[splited[i+1]] - roman_integer[splited[i]]
                i += 2
            else:
                integer += roman_integer[splited[i]]
                i += 1
        return integer
            