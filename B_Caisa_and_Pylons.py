n = int(input())
l = [0] + list(map(int, input().split()))
x = 0
ans = 0
h = 0
for i in range(n):
    x = l[i] - l[i+1]
    if h + x < 0:
        ans += abs(x + h)
        h, x = 0, 0
    h += x
    #print(l[i], l[i+1], h, ans)
print(ans)
