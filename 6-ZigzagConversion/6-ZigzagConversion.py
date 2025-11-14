# Last updated: 11/14/2025, 8:47:59 AM
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        # Edge cases: one row or shorter than numRows → no zigzag needed
        if numRows == 1 or numRows >= len(s):
            return s

        rows = [""] * numRows
        i, step = 0, 1  # i = current row, step = +1 (down) or -1 (up)

        for ch in s:
            rows[i] += ch
            # Flip direction at the top or bottom row
            if i == 0:
                step = 1
            elif i == numRows - 1:
                step = -1
            i += step

        return "".join(rows)
