def dfs(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    for edge in graph:
        u, v = edge
        if u == start and v not in path:
            new_path = dfs(graph, v, end, path)
            if new_path:
                return new_path
    return None
hrany = [('A', 'B'), ('A', 'C'), ('B', 'D'), ('B', 'E'), ('C', 'F'), ('E', 'F'), ('F', 'G')]
start_vrchol = 'A'
end_vrchol = 'G'
cesta = dfs(hrany, start_vrchol, end_vrchol)
print(cesta)