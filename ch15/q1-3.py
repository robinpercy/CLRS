__author__ = 'rpercy'

# Input = N p1 p2 p3 p4 C
# where N = size of rod and pN = price of size N
# C= cost of cut
test_input = [
    "10 1 2 3 4 5 6 7 8 9 10 1", # 10
    "10 0 0 0 0 5 0 0 0 0 0 1", #  9
    "10 2 0 0 0 0 0 0 0 0 0 1", #  11
    "10 0 0 2 0 0 0 0 0 0 0 1", #  3
    "10 1 1 1 1 1 1 1 1 1 1 1",
    "10 1 1 1 1 1 1 1 1 1 10 1",
    "10 7 8 1 5 6 3 2 4 10 9 1"
    ]

# r[l] = max(p[l],p[i] + r[l-i])
def solve(N, p, C):
    r = p
    sizes = [[i] for i in range(N+1)]
    for l in range(1,N+1):
        for i in range(l+1):
            x = p[i] + r[l-i] - C
            if (x > r[l]):
                r[l] = x
                sizes[l] = [i] + sizes[l-i]
    return (r[N], sizes[N])

def solution():
    i = 1
    for line in test_input:
        digits = [int(d) for d in line.split()]
        N = digits[0]
        print "Case #%d: %s" % (i, solve(N, [0] + digits[1:-1], digits[-1]))
        i += 1

solution()
