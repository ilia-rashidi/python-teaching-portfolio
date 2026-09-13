m, n, a, k = map(int, input().split())

# ساخت ماتریس بازی
grid = []
for _ in range(m):
    row = list(map(int, input().split()))
    grid.append(row)

# لیست امتیاز‌ها
scores = [0]*a

# پردازش ستونی
for col in range(n):
    count = 1
    for row in range(1, m):
        if grid[row][col] == grid[row-1][col]:
            count += 1
        else:
            count = 1
        
        # اگر k مهره متوالی شد، امتیاز بده
        if count >= k:
            player = grid[row][col]
            scores[player] += 1

# چاپ خروجی
for i in range(a):
    print(scores[i], end=" ")
