def findJudge(n: int, trust: List[List[int]]) -> int:
    possible_judges = [{"tc": 0} for i in range(n)]

    for c, t in trust:
        pj = possible_judges[t - 1]
        if pj:
            pj["tc"] += 1
        possible_judges[c - 1] = None

    for i, c in enumerate(possible_judges):
        if c and c["tc"] == n - 1:
            return i + 1
    return -1