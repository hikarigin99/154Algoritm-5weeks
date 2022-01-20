# 12:00 ->12:30 |16| -> 1:17
# 1:15 [FAIL]
# 반례 : https://www.acmicpc.net/board/view/72534 
N = int(input())
s = [0]
for _ in range(N):
    s.append(int(input()))
if N < 3:
    print(sum(s))
else:
    dp = [0]*(N+1)

    dp[1] = s[1]
    dp[2] = s[1] + s[2]
    dp[3] = max(s[0]+s[1]+s[3],s[0]+s[2]+s[3])
    for i in range(4, N+1):
        # if i == N: <- 마지막 계단일 경우에 처리해주기 위해서
        #     dp[i] = max(s[i]+s[i-1]+dp[i-3], dp[i-2]+s[i])
        #     continue
        dp[i] = max(s[i]+s[i-1]+dp[i-3], s[i]+dp[i-2])
        # dp[i] = max(dp[i-1], s[i]+s[i-1]+dp[i-3], dp[i-2]+s[i])
    print(dp[N])

# 질문은 포도주 문제와 계단문제의 점화식 차이 같은걸 어떻게 빠르게 캐치할수 있을까입니다.

# 포도주 문제에서는 자기자신을 스킵하고 넘어가는것도 점화식에 포함을 시켰는데,
# 이 문제에서는 스킵을하게 되면 틀리고, 반드시 자기자신을 포함하는 점화식으로 dp를 만들어야 풀렸습니다.
# 물론, 마지막 계단을 밞아야 하기에, 마지막 계단의 경우는 추가적인 작업을 해주려했습니다.
