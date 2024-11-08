def hashing(a):
    r=31
    m = 1234567891
    answer=0
    for i in range(len(a)):
        n = ord(a[i]) - ord('a')+1
        answer += n*pow(r,i)
    return int(answer) % m

num = int(input())
l = input()
print(hashing(l))