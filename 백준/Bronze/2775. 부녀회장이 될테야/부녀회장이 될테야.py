def find(k, n, people):
    for f in range(1, k+1):
        for room in range(1,n):
            people[room] += people[room-1]
    return(people[-1])

t = int(input())
for i in range(t):
    k = int(input())
    n = int(input())

    people = [i for i in range(1, n+1)]
    print(find(k,n,people))