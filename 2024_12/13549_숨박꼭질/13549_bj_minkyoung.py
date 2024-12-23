N, K = (int(i) for i in input().split())

if N < K:
    if K % 2 == 0:  # K 짝수
        while N < K:
            K //= 2
        print(min(N-K, 2*K - N))
    else:           # K 홀수
        K -= 1
        while N < K:
            K //= 2
        print(min(N-K, 2*K - N) + 1)
else:
    print(N-K)
