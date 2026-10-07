"""
1. order에서 각 메뉴 조합들이 몇번 나왔는지 알아야 함.
2. 개수가 좋아지면 그 개수만큼 골랐을 때 가장 많이 나온 조합을 알아야 함.
3. WX == XW

메뉴 조합 -> 등장 횟수
course 개수 -> 가장 많이 등장한 메뉴 조합들
동일한 메뉴 count를 위해 정렬
"""
from itertools import combinations

def solution(orders, course):
    answer = []
    menu_count = {} # 각 메뉴 조합이 몇번 등장했는지
    course_count = {} # 예를 들어 2개에 해당하는 메뉴 조합들이 저장됨
    
    for c in course:
        course_count[c] = []
        max_count = 2
        for order in orders:
            for combination in combinations(order, c):
                combination = ''.join(sorted(combination))

                if combination not in menu_count:
                    menu_count[combination] = 0
                menu_count[combination] += 1
                
                if menu_count[combination] > max_count:
                    max_count = menu_count[combination]
                    course_count[c] = [combination]
                elif menu_count[combination] == max_count:
                    course_count[c].append(combination)
    
    for c in course:
        answer.extend(course_count[c])
        
    return sorted(answer)