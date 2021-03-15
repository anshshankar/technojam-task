class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        minr = {min(rows) for rows in matrix}
        maxc = {max(columns) for columns in zip(*matrix)}

        return list(minr & maxc)
