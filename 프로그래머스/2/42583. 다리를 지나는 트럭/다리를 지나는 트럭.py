from collections import deque
def solution(bridge_length, weight, truck_weights):
    bridge = deque([0]*bridge_length)
    truck = deque(truck_weights)
    
    answer = 0
    current_weight = 0
    while bridge:
        answer += 1
        current = bridge.popleft()
        current_weight -= current
        
        if truck:
            if current_weight + truck[0] <= weight:
                t = truck.popleft()
                current_weight += t
                bridge.append(t)
            else:
                bridge.append(0)
    return answer