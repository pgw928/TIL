import sys


def dfs2(node):
    
    if node > 7:
        return
    dfs2(node*2)
    print(node, end=' ')
    dfs2(node*2+1)
dfs2(1)

print('')

def dfs3(node):
    
    if node > 7:
        return
    dfs3(node*2)
    dfs3(node*2+1)
    print(node, end=' ')
dfs3(1)