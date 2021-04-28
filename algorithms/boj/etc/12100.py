import sys; input= sys.stdin.readline
from copy import deepcopy
n = int(input())
graph = [list(map(int, input().split()))for _ in range(n)]
M = 0
for row in graph:
    r_m = max(row)
    M = max(r_m, M)

def dfs(g, cnt):
    print(cnt)
    for row in g:
        print(row)
    print('----')
    global M 
    if cnt==5:
        for row in g:
            M = max(max(row), M)
        return
    
    for k in range(4):
        n_g = deepcopy(g)
        if k==0:
            for j in range(n):
                for i in range(n-1):
                    if n_g[i][j]!=0:
                        for idx in range(i+1,n):
                            if n_g[idx][j]!=0 and n_g[idx][j]!=n_g[i][j]:
                                break 
                            elif n_g[idx][j]==n_g[i][j]:
                                n_g[i][j], n_g[idx][j] =2*n_g[i][j], 0
                                break
                        # i = 0
                # while i<n-1:
                #     if n_g[i][j] == n_g[i+1][j]:
                #         n_g[i][j], n_g[i+1][j] = 2*n_g[i][j], 0
                #         i += 2
                #     else:
                #         i+=1
                for i in range(n-1):
                    if n_g[i][j]==0:
                        for idx in range(i+1,n):
                            if n_g[idx][j]!=0:
                                n_g[i][j], n_g[idx][j] = n_g[idx][j], 0
                                break
            if n_g!=g:
                dfs(n_g, cnt+1)
            else:
                for row in n_g:
                    r_m = max(row)
                    M = max(r_m, M)
                
                
        elif k==1:
            for j in range(n):
                for i in range(n-1, 0,-1):
                    if n_g[i][j]!=0:
                        for idx in range(i-1,-1, -1):
                            if n_g[idx][j]!=0 and n_g[idx][j]!=n_g[i][j]:
                                break 
                            elif n_g[idx][j]==n_g[i][j]:
                                n_g[i][j], n_g[idx][j] =2*n_g[i][j], 0
                                break
                # i = 0
                # while i>-(n-1):
                #     if n_g[n-1+i][j] == n_g[n-2+i][j]:
                #         n_g[n-1+i][j], n_g[n-2+i][j] = 2*n_g[n-1+i][j], 0
                #         i -= 2
                #     else:
                #         i -= 1
                for i in range(n-1, 0,-1):
                    if n_g[i][j]==0:
                        for idx in range(i-1,-1, -1):
                            if n_g[idx][j]!=0:
                                n_g[i][j], n_g[idx][j] = n_g[idx][j], 0
                                break
            if n_g!=g:
                dfs(n_g, cnt+1)
            else:
                for row in n_g:
                    r_m = max(row)
                    M = max(r_m, M)
            
        elif k==2:
            for i in range(n):
                for j in range(n-1):
                    if n_g[i][j]!=0:
                        for idx in range(j+1,n):
                            if n_g[i][idx]!=0 and n_g[i][idx]!=n_g[i][j]:
                                break 
                            elif n_g[i][idx]==n_g[i][j]:
                                n_g[i][j], n_g[i][idx] =2*n_g[i][j], 0
                                break    
                # j = 0
                # while j<n-1:
                #     if n_g[i][j] == n_g[i][j+1]:
                #         n_g[i][j], n_g[i][j+1] = 2*n_g[i][j], 0
                #         j += 2
                #     else:
                #         j+=1
                for j in range(n-1):
                    if n_g[i][j]==0:
                        for idx in range(j+1,n):
                            if n_g[i][idx]!=0:
                                n_g[i][j], n_g[i][idx] = n_g[i][idx], 0
                                break
            if n_g!=g:
                dfs(n_g, cnt+1)
            else:
                for row in n_g:
                    r_m = max(row)
                    M = max(r_m, M)
                
        elif k==3:
            for i in range(n):
                for j in range(n-1, 0,-1):
                    if n_g[i][j]!=0:
                        for idx in range(j-1,-1, -1):
                            if n_g[i][idx]!=0 and n_g[i][idx]!=n_g[i][j]:
                                break 
                            elif n_g[i][idx]==n_g[i][j]:
                                n_g[i][j], n_g[i][idx] =2*n_g[i][j], 0
                                break
                # j = 0
                # while j>-(n-1):
                #     if n_g[i][n-1+j] == n_g[i][n-2+j]:
                #         n_g[i][n-1+j], n_g[i][n-2+j] = 2*n_g[i][n-1+j], 0
                #         j -= 2
                #     else:
                #         j -= 1
                for j in range(n-1, 0,-1):
                    if n_g[i][j]==0:
                        for idx in range(j-1,-1, -1):
                            if n_g[i][idx]!=0:
                                n_g[i][j], n_g[i][idx] = n_g[i][idx], 0
                                break
            if n_g!=g:
                dfs(n_g, cnt+1)
            else:
                for row in n_g:
                    r_m = max(row)
                    M = max(r_m, M)
            

dfs(graph, 0)
print(M)


                # for i in range(n-1):
                #     if n_g[i][j]!=0:
                #         for idx in range(i+1,n):
                #             if n_g[idx][j]!=0 and n_g[idx][j]!=n_g[i][j]:
                #                 break 
                #             elif n_g[idx][j]==n_g[i][j]:
                #                 n_g[i][j], n_g[idx][j] =2*n_g[i][j],, 0
                #                 break