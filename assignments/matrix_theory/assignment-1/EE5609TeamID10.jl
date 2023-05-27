
sum = [[0,1,2,3],[1,0,3,2],[2,3,0,1],[3,2,1,0]]

mul = [[0,0,0,0],[0,1,2,3],[0,2,3,1],[0,3,1,2]]

inverse = [1,3,2]

function row_operation(arr1,arr2,n,ith)
    if arr1[ith] == 0
        return arr1
    elseif arr1[ith] == arr2[ith]
        res = [sum[arr1[i]+1][arr2[i]+1] for i in 1:n]
    else
        mul_inv2 = inverse[arr2[ith]]
        b = mul[arr1[ith]+1][mul_inv2+1]
        arr2 = [mul[b+1][arr2[i]+1] for i in 1:n]
        res = [sum[arr1[i]+1][arr2[i]+1] for i in 1:n]
    end
    return res
end

function echleon_form(ab)
    m,n = size(ab)
    c = 1
    for i in 1:m-1
        ab1 = ab[1:i-1,:]
        ab2 = ab[i:m,:]
        mv,mi = findmax(ab2[:,c])
        while mv == 0 && c<n
            c += 1
            mv,mi = findmax(ab2[:,c])
        end
        mi += i-1
        (ab[i,:],ab[mi,:]) = (ab[mi,:],ab[i,:])
        for j in i+1:m
            ab[j,:] = row_operation(ab[j,:],ab[i,:],n,c)
        end
        if c<n
            c=c+1
        end
    end
    return ab
end

function no_of_nzr(arr)
    m,n = size(arr)
    cnt = 0
    l = [0 for i in 1:n]
    for i in 1:m
        if arr[i,:] == l
            cnt += 1
        end
    end
    return m-cnt   
end

function rankconsistencyTeamID10(a,b)
    m,n = size(a)
    ab = hcat(a,b)
    e_ab = echleon_form(ab)
    e_a = e_ab[1:end , 1:end .!=n+1]
    rank_a = 0 ; rank_ab = 0
    rank_ab = no_of_nzr(e_ab)
    rank_a = no_of_nzr(e_a)
    consistent = true
    if rank_ab != rank_a
        consistent = false
    else
        consistent = true
    end
    return (e_a , rank_a , consistent)
end

# A = [0 0 1;0 0 1]; b = [3,3]; U = [3 0; 0 2; 0 0]
# u,r,c = rank_and_consistency(A,b)
# println(u ,"  ",r ," ", c)
