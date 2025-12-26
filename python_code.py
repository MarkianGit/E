s, a = input().split('=')
a = int(a)
n = len(s)

dp = [[None] * (a + 1) for _ in range(n + 1)]
dp[0][0] = []

for i in range(n):
    for sm in range(a + 1):
        if dp[i][sm] is not None:
            for j in range(i + 1, n + 1):
                val = int(s[i:j])
                if sm + val <= a:
                    cur = dp[i][sm] + [s[i:j]]
                    if dp[j][sm + val] is None or len(cur) < len(dp[j][sm + val]):
                        dp[j][sm + val] = cur

res = dp[n][a]
print('+'.join(res))
