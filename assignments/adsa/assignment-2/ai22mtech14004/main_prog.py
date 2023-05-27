
w = lambda a,b,p : sum(p[a:b])

#to get the preorder of the BST
def get_preorder(cost,w,a,b):
    r = cost[a][b]
    if r[1] == 0:
        return
    else:
        print(w[r[1]-1],end = " ")
        get_preorder(cost,w,a,r[1]-1)
        get_preorder(cost,w,r[1],b)
    
#Cost Function to calculate the cost for the each node of bst
def cost_function(w,p):
    n = len(p)
    arr = [[[0,0] for i in range(n+1)] for i in range(n+1)]
    for a in range(n):
        arr[a][a][0] = p[a]
        arr[a][a][1] = a+1
    
    w = lambda a,b : round(sum(p[a:b+1]),3)

    for k in range(2,n+1):
        for i in range(n-k+2):
            j = i+k-1
            if i>=n or j>=n:
                break
            arr[i][j][0] = 32768
            for a in range(i,j+1):
                temp = 0
                if a>i: temp += round(arr[i][a-1][0],3)
                if a<j: temp += round(arr[a+1][j][0],3)
                temp += round(w(i,j),3)
                if temp < arr[i][j][0]:
                    arr[i][j][0] = round(temp,3)
                    arr[i][j][1] = a+1
            #print(res)

    return (arr)

#Optimal BS trees
def btree(w,p):
    cost = cost_function(w,p)
    for i in range(len(cost)):
        cost[i].insert(0,[0,0])
        cost[i].pop()
    print("Optimal Cost : ",cost[0][-1][0])
    print("The preorder for the Opt BST is : ",end='')
    get_preorder(cost,w,0,len(p))

#checking the input
def check(w,p):
    s1 = sum(p)
    p1 = list(set(p))
    w1 = sorted(w)
    res = [0,""]
    if w1 != w:
        res[1] += "Words are not sorted \n"
    if w1 != sorted(set(w)):
        res[1] += "Words are not distinct \n"
    if round(s1,3) != 1.000:
        res[1] += "Probabilities does not add up to 1 \n"
    if len(p) != len(p1):
        res[1] += "Probabilities are not distinct \n"
    if len(p) == len(p1) and w1 == w and round(s1,5) == 1.000 and w1 == sorted(set(w)):
        res[0] = 1
        res[1] = "nice"
    return res

def main():
    n = int(input())
    w,p= [],[]
    for _ in range(n):
        w.append(input())
        p.append(float(input()))
    res = check(w,p)
    if res[0] == 0:
        print(res[1])
    else:
        btree(w,p)

main()