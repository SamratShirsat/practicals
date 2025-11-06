def rod_cutting():
    n = int(input("Enter the length of the rod: "))
    prices = [int(input(f"Price for length {i + 1}: ")) for i in range(n)]

    dp = [[0] * (n + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i <= j:
                dp[i][j] = max(dp[i - 1][j], prices[i - 1] + dp[i][j - i])
            else:
                dp[i][j] = dp[i - 1][j]

    print("\nProfit Matrix:")
    for row in dp:
        print("".join(f"{v:>8}" for v in row))

    print(f"\nMaximum obtained value is {dp[n][n]}")

    pieces, i, j = [], n, n
    while j:
        if dp[i][j] == dp[i - 1][j]:
            i -= 1
        else:
            pieces.append(i)
            j -= i

    print("\nPieces used for maximum profit:")
    print(" ".join(map(str, pieces)))


if __name__ == "__main__":
    rod_cutting()
