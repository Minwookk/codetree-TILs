def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < m 

def get_max_sum(x, y):
    max_sum = 0 
    for shape in blocks:
        sum_of_nums = sum([
            grid[x + dx][y + dy]
            for dx in range(4)
            for dy in range(4)
            if in_range(x + dx, y + dy) and shape[dx][dy]
        ])
        max_sum = max(max_sum, sum_of_nums)

    return max_sum