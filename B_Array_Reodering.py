from math import gcd
"""Worst performance as I didn't notice that n < 2000 and o(n^2) would have been ok. :("""
for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        for j in range(i+1, n):
            if gcd(l[i], 2*l[j]) > 1 or gcd(l[i]*2, l[j]) > 1:
                ans += 1
    print(ans)
