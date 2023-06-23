#Ninja's training
def Training( self, day, last, points, dp):

    if (dp[day][last] != -1):
        return dp[day][last]

    if day == 0:
        maxpoints = 0
        for i in range(3):
            if i != last:
                maxpoints = max(maxpoints, points[0][i])
        dp[day][last] = maxpoints
        return dp[day][last]

    maxpoints = 0
    for i in range(3):
        if i != last:
            activity = points[day][i] + Training(day - 1, i, points, dp)
            maxpoints = max(maxpoints, activity)

    dp[day][last] = maxpoints

    return dp[day][last]
