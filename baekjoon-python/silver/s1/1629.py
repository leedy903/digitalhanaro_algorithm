import sys
input = sys.stdin.readline

a, b, c = map(int, input().split())

def getRest(a, b, c):
    rest_list = []
    rest_set = set()
    
    for i in range(b):
        rest = a % c
        if rest in rest_set:
            break
        rest_list.append(rest)
        rest_set.add(rest)
        a *= a
    return rest_list[b % len(rest_set)]

ans = getRest(a, b, c)
print(ans)