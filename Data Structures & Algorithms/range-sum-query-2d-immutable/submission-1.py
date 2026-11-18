class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        rows = len(matrix)
        cols = len(matrix[0])
        self.prefix = [[0] * cols for _ in range(rows)]
        for r in range(rows):
            total = 0
            for c in range(cols):
                total += matrix[r][c]
                self.prefix[r][c] = total
        
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        total = 0

        for r in range(row1, row2 + 1):

            # if region starts at column 0
            if col1 == 0:
                total += self.prefix[r][col2]

            else:
                total += self.prefix[r][col2] - self.prefix[r][col1 - 1]

        return total
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)