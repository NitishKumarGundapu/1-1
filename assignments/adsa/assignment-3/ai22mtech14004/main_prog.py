import sys

class dijkstras :
    noparent = -1

    @staticmethod
    def dijkstra(G,sv) :
        n = len(G[0])
        sd = [0]*(n)
        added = [False] * (n)
        vi = 0
        while (vi < n) :
            sd[vi] = sys.maxsize
            added[vi] = False
            vi += 1
        sd[sv] = 0
        p = [0]*(n)
        p[sv] = dijkstras.noparent
        i = 1
        while (i < n) :
            nv = -1
            mindist = sys.maxsize
            vi = 0
            while (vi < n) :
                if (not added[vi] and sd[vi] < mindist) :
                    nv = vi
                    mindist = sd[vi]
                vi += 1
            added[nv] = True
            vi = 0
            while (vi < n) :
                ed = G[nv][vi]
                if (ed > 0 and ((mindist + ed) < sd[vi])) :
                    p[vi] = nv
                    sd[vi] = mindist + ed
                vi += 1
            i += 1
        return dijkstras.getSolution(sv, sd, p)

    @staticmethod
    def getSolution(sv,d,p) :
        vi = 0
        res = []
        while (vi < len(d)) :
            if (vi != sv) :
                res.append([d[vi],dijkstras.getPath(vi, p)[::-1]])
            else :
                res.append([0,[]])
            vi += 1
        return res

    @staticmethod
    def getPath(cv,p):
        res = []
        while cv != dijkstras.noparent :
            res.append(cv)
            cv = p[cv]
        return res

    @staticmethod
    def main(G,vertex) :
        return dijkstras.dijkstra(G, vertex)

def get_metric_graph(G):
    res = []
    for v in range(len(G)):
        res.append(dijkstras.main(G,v))
    return res

class krushkal_mst:
    def __init__(self, vertex):
        self.V = vertex
        self.graph = []
 
    def add_edge(self, u, v, w):
        self.graph.append([u, v, w])
 
    def print_graph(self):
        print(self.graph)
 
    def search(self, parent, i):
        if parent[i] == i:
            return i
        return self.search(parent, parent[i])
 
    def apply_union(self, parent, rank, x, y):
        xroot = self.search(parent, x)
        yroot = self.search(parent, y)
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1
 
  
    def kruskal_algo(self):
        result = []
        i, e = 0, 0
        self.graph = sorted(self.graph, key=lambda item: item[2])
        parent = []
        rank = []
        for node in range(self.V):
            parent.append(node)
            rank.append(0)
        
        while e < self.V - 1:
            try:
                u, v, w = self.graph[i]
                i = i + 1
                x = self.search(parent, u)
                y = self.search(parent, v)
                if x != y:
                    e = e + 1
                    result.append([[u, v], w])
                    self.apply_union(parent, rank, x, y)
            except:
                break
        return result

    @staticmethod
    def main(mat,steiner_vertices=[]):
        if len(mat) - len(steiner_vertices) >= 2:
            get_value = lambda x : x
            if type(mat[0][0]) == list:
                get_value = lambda x : x[0]
            n = len(mat)
            n1 = n - len(steiner_vertices)
            mat1 = []
            for i in range(n):
                t = []
                for j in range(n):
                    if i+1 not in steiner_vertices and j+1 not in steiner_vertices:
                        t.append(get_value(mat[i][j]))
                if t != []:
                    mat1.append(t)
            
            res_indexes = [i for i in range(n) if i+1 not in steiner_vertices]
            g = krushkal_mst(n1)
            for i in range(n1):
                for j in range(n1):
                    if mat1[i][j] > 0 and i<j:
                        g.add_edge(i,j,mat1[i][j])
           
            res = []
            if type(mat[0][0]) == list:
                for a,b in g.kruskal_algo():
                    i,j = res_indexes[a[0]],res_indexes[a[1]]
                    res.append([[i,j],mat[i][j]])
            else:
                for a,b in g.kruskal_algo():
                    i,j = res_indexes[a[0]],res_indexes[a[1]]
                    res.append([[i,j],b])

            return res
        # elif len(mat) - len(steiner_vertices) == 0:
        #     l,n = [],len(mat)
        #     for i in range(n):
        #         for j in range(n):
        #             if i != j:
        #                 l.append([i,j,mat[i][j][0],mat[i][j][1]])
        #     res = sorted(l , key = lambda x: x[2])[0]
        #     return [[[res[0],res[1]],[res[2],res[3]]]]

        # elif len(mat) - len(steiner_vertices) == 1:
        #     n = len(mat)
        #     rem = [i for i in range(n) if i+1 not in steiner_vertices]
        #     l = mat[rem[0]]
        #     res = []
        #     for i in range(n):
        #         if i != rem[0]:
        #             res.append([rem[0],i,l[i][0],l[i][1]])
        #     res1 = sorted(res , key = lambda x: x[2])[0]
        #     return [[[res1[0],res1[1]],[res1[2],res1[3]]]]
        else:
            raise Exception("terminal vertices must be atleast 2")
            

def get_graph_and_vertices():
    graph = []
    with open("input.txt",'r') as f:
        graph= f.readlines()
    graph = [list(map(int,a.split())) for a in graph]
    print('The input matrix A the program read from the file is displayed below:')
    for i in graph: print(*i)
    print("Enter the steiner vertices , end with '*'")
    steiner_vertices = []
    cnt = 0
    n = len(graph)
    try:
        while True:
            t = input()
            if t == "*":
                break
            elif cnt > n :
                raise Exception("Count exceded")
            elif int(t) <= 0 or int(t) > n:
                raise Exception("error occured , enter the input correctly")
            else:
                steiner_vertices.append(int(t))
            cnt += 1

        steiner_vertices = sorted(set(steiner_vertices))
        result_G = [[0 for i in range(n)] for j in range(n)]
        complete_graph = get_metric_graph(graph)
        mst = krushkal_mst.main(complete_graph,steiner_vertices)
        cost_mst = 0
        for a,b in mst:
            cost_mst += b[0]
            for i in range(len(b[1])-1):
                result_G[b[1][i]][b[1][i+1]] = graph[b[1][i]][b[1][i+1]]
                result_G[b[1][i+1]][b[1][i]] = graph[b[1][i+1]][b[1][i]]

        final_cost = 0
        result_graph = [[0 for i in range(n)] for j in range(n)]
        for a,b in krushkal_mst.main(result_G):
            final_cost += b
            result_graph[a[0]][a[1]] = b
            result_graph[a[1]][a[0]] = b

        print(f'The final cost obtained for steiner tree is {final_cost}\n')
        print("""The 2-factor approximate tree we have computed is given below (we describe this tree by listing all the neighbors of all the vertices in the tree):\n""")
        for a in range(n):
            l = []
            for i in range(n):
                if result_graph[a][i]>0 :
                    l.append(f'{i+1} with cost {result_graph[a][i]}')
            if l != []:
                print(f"Neighbors of Vertex {a+1} : ",end='')
                print(*l,sep=' , ')
                print()

    except Exception as e:
        print(e)

if __name__ == "__main__":
    get_graph_and_vertices()
