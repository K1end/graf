# Graf
1.
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
    
dfs je rekurzivní funkce, která prochází graf a hledá cestu z vrcholu start do vrcholu end.
Parametr graph je seznam hran, kde každá hrana je reprezentována jako dvojice (u, v) označující hranu z vrcholu u do vrcholu v.
Parametr start je počáteční vrchol, ze kterého začínáme hledat cestu.
Parametr end je cílový vrchol, ke kterému hledáme cestu.
Parametr path je seznam vrcholů, které jsme dosud navštívili na naší cestě.

2.
  path = path + [start]
  if start == end:
      return path

V této části kódu přidáváme aktuální vrchol start do seznamu path, abychom si pamatovali, které vrcholy jsme již navštívili.
Pokud jsme dosáhli cílového vrcholu (start == end), funkce vrátí aktuální cestu path, která vede z start do end.

3.
for edge in graph:
    u, v = edge
    if u == start and v not in path:
        new_path = dfs(graph, v, end, path)
        if new_path:
            return new_path

  Tato část kódu prochází seznam hran graph a hledá hrany, které vycházejí z aktuálního vrcholu start a nevedou do vrcholů, které již byly navštíveny (v not in path).
Pokud najde takovou hranu (u, v), zavolá funkci dfs rekurzivně s novým cílovým vrcholem v.
Pokud funkce dfs nalezne cestu, která vede z aktuálního vrcholu start do cílového vrcholu end, vrátí tuto cestu.

4.
hrany = [('A', 'B'), ('A', 'C'), ('B', 'D'), ('B', 'E'), ('C', 'F'), ('E', 'F'), ('F', 'G')]
start_vrchol = 'A'
end_vrchol = 'G'
cesta = dfs(hrany, start_vrchol, end_vrchol)
print(cesta)  # Vypíše cestu z 'A' do 'G'.

V příkladu jsou definovány hrany mezi vrcholy a hledá se cesta z vrcholu 'A' do vrcholu 'G'.
Funkce dfs je zavolána s těmito parametry, a pokud nalezne cestu, vypíše ji na výstup.
