"""
1. 누굴 신고했는지 저장하는 딕셔너리 값은 집합(신고 당한 사람들)
2. 누가 몇번 신고 당했는지 횟수를 저장하는 딕셔너리
(동일인이 같은 사람을 2번 신고할수 없음)
3. 이제 2번에 있는 딕셔너리에서 k번 이상인 사람을 추출
4. id_list를 순회하며 해당 사람이 신고한 사람이 k번이상이면 answer에 추가
"""

def solution(id_list, report, k):
    answer = []
    
    record = dict()
    call_count = dict()
    sub_answer = set()
    
    # 누굴 신고했는지 저장
    for id in id_list:
        record[id] = set()
        
    # 누가 몇번 신고 당했는지 횟수를 저장
    for r in report:
        caller, called = r.split()
        if called in record[caller]:
            continue
        
        record[caller].add(called)
        
        if called not in call_count:
            call_count[called] = 1
        else:
            call_count[called] += 1
        
        if call_count[called] >=k:
            sub_answer.add(called)
    
    for id in id_list:
        count = len(record[id].intersection(sub_answer))
        answer.append(count)
        
    return answer