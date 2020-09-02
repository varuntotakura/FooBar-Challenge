def solution(l, t):
    # Your code here
    c = 0
    ra = 0
    m = set(l)
    s = 0
    d = 0
    if len(m) != len(l):
        if sum(l) == t:
            ra = ([0,len(l)-1])
        else:
            for i in l:
                if ra == 0:
                    ra = rs(l[d:], t, l, d)
                    d += 1
        print(ra)
    else:
        for i in l:
            if ra == 0:
                ra = rec(l[c:], t)
                c += 1
        if ra == 0:
            return [-1, -1]
        else:
            print([l.index(ra[0]), l.index(ra[1])])
            
def rec(l,t):
    s = 0
    r = 0
    for n, i in enumerate(l):
        s  = s + i
        if(s == t):
            r = [l[0], l[n]]
    return r

def rs(l,t,fl,d):
    s = 0
    r = 0
    j = [0]*d
    jl = j+l
    for n, i in enumerate(jl):
        s = s + i
        if s == t:
            f = jl.index(l[0])
            r = (f, n)
    return r
        
solution([6, 4, 1, 1, 1], 3)















def solution(total_lambs):
    # Your code here
    if total_lambs >= 10**9:
        return 0
    doubledList=[]
    x=0
    runningtotal=0
    while x<= total_lambs:
        currentvalue=2**x
        doubledList.append(currentvalue)
        runningtotal=runningtotal + currentvalue
        if runningtotal > total_lambs:
            break
        x=x+1
    fiblist=[1,1]
    fibrunningtotal=2
    y=2
    while y<= total_lambs:
        value=fiblist[y-1] + fiblist[y-2]
        fiblist.append(value)
        fibrunningtotal=fibrunningtotal + int(fiblist[y])
        if fibrunningtotal > total_lambs:
            break
        y=y+1
    solution = len(fiblist) - len(doubledList)
    return abs(solution)
