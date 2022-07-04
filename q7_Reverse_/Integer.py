class Solution:
    def reverse(self, x: int) -> int:
        flag = False

        if x == 0:
            return 0
        if x < 0:
            x = -x
            flag = True

        x = int(str(x)[::-1])

        if flag:
            x = -x

        if x not in range(-2 ** 31, 2 ** 31 - 1):
            return 0
        return x
