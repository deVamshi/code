class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        out = []
        if matrix == None or matrix == []: return out
        top, bottom, left, right = 0, len(matrix) - 1, 0, len(matrix[0]) - 1
        visited = 0
        total = len(matrix) * len(matrix[0])
        size = len(out)
        
        while left <= right and top <= bottom:
            for i in range(left, right + 1):
                out.append(matrix[top][i])
            top += 1
            
            for i in range(top, bottom + 1):
                out.append(matrix[i][right])
            right -= 1
            
            
            if not (left <= right and top <= bottom): break
            
            
            for i in range(right, left - 1, -1):
                out.append(matrix[bottom][i])
            bottom -= 1
            
            for i in range(bottom, top - 1, -1):
                out.append(matrix[i][left])
            left += 1
        
            
            
        return out
        
        
        