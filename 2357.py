import sys
import math
input = sys.stdin.readline

def init_min(a, tree, node, start, end):
    if start == end:
        tree[node] = a[start]
    else:
        init_min(a, tree, node*2, start, (start+end)//2)
        init_min(a, tree, node*2+1, (start+end)//2+1, end)
        tree[node] = min(tree[node*2], tree[node*2+1])
        
def query_min(tree, node, start, end, left, right):
    if left > end or right < start:
        return -1
    if left <= start and end <= right:
        return tree[node]
    lmin = query_min(tree, node*2, start, (start+end)//2, left, right)
    rmin = query_min(tree, node*2+1, (start+end)//2+1, end, left, right)
    if lmin == -1:
        return rmin
    elif rmin == -1:
        return lmin
    else:
        return min(lmin, rmin)

def init_max(a, tree, node, start, end):
    if start == end:
        tree[node] = a[start]
    else:
        init_max(a, tree, node*2, start, (start+end)//2)
        init_max(a, tree, node*2+1, (start+end)//2+1, end)
        tree[node] = max(tree[node*2], tree[node*2+1])
    
def query_max(tree, node, start, end, left, right):
    if left > end or right < start:
        return -1
    if left >= start and end >= right:
        return tree[node]
    lmax = query_max(tree, node*2, start, (start+end)//2, left, right)
    rmax = query_max(tree, node*2+1, (start+end)//2+1, end, left, right)
    if lmax == -1:
        return rmax
    elif rmax == -1:
        return lmax
    else:
        return max(lmax, rmax)

n, m = map(int, input().split())
a = []
for _ in range(n):
    a.append(int(input()))
h = math.ceil(math.log2(n))
tree_size = 1 << (h+1)

tree_min = [0] * tree_size
init_min(a, tree_min, 1, 0, n-1)

tree_max = [0] * tree_size
init_max(a, tree_max, 1, 0, n-1)

print(tree_min)
print(tree_max)
for _ in range(m):
    ans1, ans2 = 0, 0
    t1, t2 = map(int, input().split())
    left, right = t1, t2
    ans1 = query_min(tree_min, 1, 0, n-1, left-1, right-1)
    ans2 = query_max(tree_max, 1, 0, n-1, left-1, right-1)
    print(ans1,ans2)