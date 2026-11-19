# Island Perimeter

`island_perimeter(grid)` returns the perimeter of an island in a
rectangular grid, where 1 represents land and 0 represents water.

Each land cell contributes four sides. Subtract two for each edge
shared with land above or to the left. A grid with no land returns 0.

Time complexity is O(rows * columns). Extra space usage is O(1).
