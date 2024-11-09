import sys
input = sys.stdin.read
def my_round(x):
    return int(x+0.5) if x-int(x)>= 0.5 else int(x)

data = input().splitlines()
n = int(data[0])
if n==0:
    print(0)
else:
    cut = my_round(n*0.15)
    f_li = list(map(int, data[1:]))
    f_li.sort()

    s_list = f_li[cut:n-cut]
    print(my_round(sum(s_list)/len(s_list)))