class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        start = 0
        max_length = 1
        # initialize a 2d array to save the state that represents the substring between i and including j is palindromic
        dp = [[False] * n for _ in range(n)]

        # single character must be palindromic string
        for i in range(n):
            dp[i][i] = True

        # the length of the answer can be between 2 and n
        for current_length in range(2, n + 1):
            for left in range(n):
                # right is determined by the left and current length
                right = current_length + left - 1

                # break the loop if exceed the right boundary(n)
                if right >= n:
                    break

                # update the array from bottom to top(short length to long)
                if s[left] == s[right]:
                    # they are clinging
                    if right - left == 1:
                        dp[left][right] = True
                    else:
                        # the nature of palindromic string
                        dp[left][right] = dp[left + 1][right - 1]

                # update the result
                if dp[left][right] and right - left + 1 > max_length:
                    max_length = right - left + 1
                    start = left

        return s[start: start + max_length]
