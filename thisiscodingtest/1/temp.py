def migrate(n, l, r, a):
    # Initialize a counter to track the number of days of population movement
    days = 0
    while True:
        # Initialize a 2D array to track which countries have had their populations changed
        changed = [[False for _ in range(n)] for _ in range(n)]
        # Iterate through each country and check if the population difference between it and any of its neighbors is between L and R
        for i in range(n):
            for j in range(n):
                neighbors = [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]
                for ni, nj in neighbors:
                    if ni >= 0 and ni < n and nj >= 0 and nj < n and l <= abs(a[i][j] - a[ni][nj]) <= r:
                        # Open the border between the two countries and mark both countries as changed
                        a[i][j] = (a[i][j] + a[ni][nj]) // 2
                        a[ni][nj] = a[i][j]
                        changed[i][j] = True
                        changed[ni][nj] = True
        # Disband the Union and close all borders
        # (no action needed since we're using a new array each iteration)
        # Increment the counter
        days += 1
        # Check if there are any changed countries
        if not any(any(row) for row in changed):
            # If not, exit the loop
            break
    # Return the number of days of population movement
    return days


print(migrate(3, 5, 10, [[10, 15, 20], [20, 30, 25], [40, 22, 10]]))
