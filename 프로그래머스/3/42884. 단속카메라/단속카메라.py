def solution(routes):
    routes.sort(key = lambda x:x[1])
    answer=1
    install = routes[0][1]
    for route in routes:
        if route[0] <= install <= route[1]:
            continue
        else:
            answer+=1
            install = route[1]
    return answer