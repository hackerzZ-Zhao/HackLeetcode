Question:
There is a row of n houses, where each house can be painted one of three colors: red, blue, or green. The cost of painting each house with a certain color is different. You have to paint all the houses such that no two adjacent houses have the same color.

The cost of painting each house with a certain color is represented by a n x 3 cost matrix. For example, costs[0][0] is the cost of painting house 0 with the color red; costs[1][2] is the cost of painting house 1 with color green, and so on... Find the minimum cost to paint all houses.

 
Example:
Input: costs = [[17,2,17],[16,16,5],[14,3,19]]
Output: 10
Explanation: Paint house 0 into blue, paint house 1 into green, paint house 2 into blue.
Minimum cost: 2 + 5 + 3 = 10.

Solution:

class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        # dp[i][j] represents the minimum cost of use j color to paint house i
        # so dp[i][red] = min(dp[i - 1][blue], dp[i - 1][green]) + costs[i][red]
        # since house i and i - 1 cannot be the same color and we only have three kinds of color
        # same idea:
        # dp[i][blue] = min(dp[i - 1][red], dp[i - 1][green]) + costs[i][blue]
        # dp[i][green] = min(dp[i - 1][blue], dp[i - 1][red]) + costs[i][green]
        if not costs:
            return 0
        
        n = len(costs)
        dp = [[sys.maxsize for col in range(3)] for row in range(n)]
        dp[0][0] = costs[0][0]
        dp[0][1] = costs[0][1]
        dp[0][2] = costs[0][2]
        for i in range(1, n):
            dp[i][0] = min(dp[i - 1][1], dp[i - 1][2]) + costs[i][0]
            dp[i][1] = min(dp[i - 1][0], dp[i - 1][2]) + costs[i][1]
            dp[i][2] = min(dp[i - 1][0], dp[i - 1][1]) + costs[i][2]
            
        return min(dp[n - 1][0], min(dp[n - 1][1], dp[n - 1][2]))
