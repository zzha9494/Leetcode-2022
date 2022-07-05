class Solution:
    def intToRoman(self, num: int) -> str:
        res = ''

        m = num // 1000
        num = num % 1000
        res += 'M' * m

        c = num // 100
        num = num % 100
        if c == 9:
            res += 'CM'
        elif c == 4:
            res += 'CD'
        else:
            d = c // 5
            c = c % 5
            res = res + 'D' * d + 'C' * c

        x = num // 10
        num = num % 10
        if x == 9:
            res += 'XC'
        elif x == 4:
            res += 'XL'
        else:
            l = x // 5
            x = x % 5
            res = res + 'L' * l + 'X' * x

        if num == 9:
            res += 'IX'
        elif num == 4:
            res += 'IV'
        else:
            v = num // 5
            i = num % 5
            res = res + 'V' * v + 'I' * i

        return res
