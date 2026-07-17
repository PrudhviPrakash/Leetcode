class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph={}
        for i in range(n):
            graph[i]=[]
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        q=deque()
        v=set()
        q.append(source)
        while q:
            node=q.popleft()
            if node==destination:
                return True
            if node not in v:
                v.add(node)
                for neg in graph[node]:
                    if neg not in v:
                        q.append(neg)
        return False
            
