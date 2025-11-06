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
    

# Matrix chain Multiplication 

def matrix_chain_order(p):
 n = len(p) - 1
 m = [[0] * n for _ in range(n)]
 s = [[0] * n for _ in range(n)]
 for chain_len in range(2, n + 1):
    for i in range(n - chain_len + 1):
        j = i + chain_len - 1
        m[i][j] = float('inf')
 for k in range(i, j):
    cost = m[i][k] + m[k + 1][j] + p[i] * p[k + 1] * p[j +
1]
 if cost < m[i][j]:
    m[i][j] = cost
    s[i][j] = k
 return m, s
def print_optimal_parens(s, i, j):
 if i == j:
    return f"A{i+1}"
 else:
    left = print_optimal_parens(s, i, s[i][j])
    right = print_optimal_parens(s, s[i][j] + 1, j)
    return f"({left} x {right})"
def main():
 n = int(input("Enter the number of matrices: "))
 dims = []
 for i in range(n):
    r = int(input(f"Enter number of rows for matrix A{i+1}: "))
    c = int(input(f"Enter number of columns for matrix A{i+1}: "))
    if i == 0:
        dims.append(r)
        dims.append(c)
 m, s = matrix_chain_order(dims)
 print("\nMinimum number of multiplications required:", m[0][n - 1])
 print("Optimal parenthesization:", print_optimal_parens(s, 0, n -
1))
if __name__ == "__main__":
 main()