n = int(input())
for i in range(n):
    h, m, o = map(int, input().split())
    if o == 1:
        msg = ("A porta abriu!")

    else:
        msg = ("A porta fechou!")

    print("{:0>2}:{:0>2} -".format(h, m), msg)
    