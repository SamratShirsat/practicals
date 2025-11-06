def lcs(X, Y):
 m, n = len(X), len(Y)
 dp = [[0] * (n + 1) for _ in range(m + 1)]

 for i in range(1, m + 1):
    for j in range(1, n + 1):
        if X[i - 1] == Y[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

 lcs_string = []
 i, j = m, n
 while i > 0 and j > 0:
    if X[i - 1] == Y[j - 1]:
        lcs_string.append(X[i - 1])
        i -= 1
        j -= 1
    elif dp[i - 1][j] > dp[i][j - 1]:
        i -= 1
    else:
        j -= 1

 return ''.join(reversed(lcs_string))

if __name__ == "__main__":
    str1 = input("\nEnter the first string: ")
    str2 = input("Enter the second string: ")
    print(f"The Longest Common Subsequence is: {lcs(str1, str2)}")
    print(f"Length: {len(lcs(str1, str2))} \n")