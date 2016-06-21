Use dynamic programming with 2D matrix(or rolling vector).

dp[i][j] = min(dp[i][j-1],dp[i-1][j],dp[i-1][j-1])+1  if (i,j) == 1
dp[i][j] = 1  else
