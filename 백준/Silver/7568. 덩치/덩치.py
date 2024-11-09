n = int(input())
weight=[]
height=[]
rank =[]
for i in range(n):
    w, h = map(int, input().split())
    score = 1
    if not rank:
        weight.append(w)
        height.append(h)
        rank.append(1)
    else:
        for j in range(0, i):
            if weight[j]<w and height[j] < h:
                rank[j] +=1
            elif weight[j]>w and height[j]>h:
                score +=1
        weight.append(w)
        height.append(h)
        rank.append(score)

print(" ".join(map(str, rank)))