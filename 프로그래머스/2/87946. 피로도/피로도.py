from itertools import permutations

def solution(k, dungeons):
    answer = -1
    
    # 던전 방문 수를 순열로 만든다.
    for permutation in permutations(dungeons):
        hp = k
        count = 0
        for min_have, cost in permutation:
            if hp < min_have:
                continue
            hp -= cost
            count += 1
            
        answer = max(answer, count)
    return answer