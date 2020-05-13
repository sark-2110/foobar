#python3 code

from itertools import combinations
def solution(num_buns, num_required):
    # Your code here
    buns = [[] for i in range(num_buns)]
    if num_required == 0:
        return buns
    start = 0
    for c in combinations(buns, num_buns - num_required + 1):
        for item in c:
            item.append(start)
        start += 1
    return buns
    [[0], [1], [2], [3]]
