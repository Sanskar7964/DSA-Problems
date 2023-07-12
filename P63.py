def floodFill(image, sr, sc, newColor):
    if image[sr][sc] == newColor:
        return image
    
    oldColor = image[sr][sc]
    dfs(image, sr, sc, oldColor, newColor)
    return image


def dfs(image, r, c, oldColor, newColor):
    if r<0 or r>= len(image) or c<0 or c> len(image[0]) or image[r][c]!= oldColor:
        return 
    
    image[r][c] = newColor

    dfs(image, r+1, c, oldColor, newColor)
    dfs(image, r-1, c, oldColor, newColor)
    dfs(image, r, c+1, oldColor, newColor)
    dfs(image, r, c-1, oldColor, newColor)