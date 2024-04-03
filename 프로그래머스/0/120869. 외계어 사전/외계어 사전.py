def solution(spell, dic):
    for i in dic:
        k = list(i)
        if sorted(k) == sorted(spell):
            return 1
    return 2