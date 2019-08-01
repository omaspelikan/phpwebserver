def run(arr,start_lane):
    global p
    swap = 0
    check = 0
    current_lane = start_lane
    path = [0 for _ in range(l)]
    for i in range(l):
        if arr[current_lane][i] == '.':
            path[i] = 1
        else:
            current_lane ^=1
            if arr[current_lane][i] == '.':
                swap+=1
                path[i] = 1
            else:
                check = 1
                break
    if not check:
        p[1][start_lane]= swap

for _ in range(int(input())):
    lane = []
    ans = []
    lane.append(list(input()))
    lane.append(list(input()))
    end = 0
    l = len(lane[0])
    p = [[0,0],[-1,-1]]
    path1 = [0 for _ in range(l)]
    jump = []
    if lane[0][0] == '.' and ((lane[0][-1] == '.') or (lane[1][-1]=='.')):
        p[0][0] = 1
    if lane[1][0] == '.' and ((lane[0][-1] == '.') or (lane[1][-1]=='.')):
        p[0][1] = 1
    for i in range (2):
        if p[0][i]:
            run(lane,i)
            if p[1][i] != -1:
                ans.append(p[1][i])
    if len(ans) > 0:
        print('Yes')
        print(min(ans))
    else:
        print('No')

