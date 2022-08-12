v, l = map(int, input().split())
volumes = list(map(int, input().split()))
for i in volumes:
    v += i
    if v < 0:
        v = 0

    elif v > 100:
        v = 100

print(v)