import collections
def mostPopularCreator(creators, ids, views):
        
    cvid=collections.defaultdict(list)
    n = len(ids)
    for i in range(n):
        c=creators[i]
        cvid[c].append(i)
    mx=0
    mp=collections.Counter()
    m2={}
    mostpop=""
    for c,vids in cvid.items():
        mxvid=float("-inf")
        for i in vids:
            mp[c]+=views[i]
            if mxvid<views[i]:
                mxvid=views[i]
                # mostpop=ids[i]
        # m2[c]=mostpop
        


    a=max(mp.values())
    res=[]
    creats=[]
    for c,pop in mp.items():
        if pop==a:
            creats.append(c)

    for c in creats:
        ep = cvid[c]
        z=[]
        for idx in ep:
            idz = ids[idx]
            v = views[idx]
            z.append((v,idz))
        z.sort()
        print(z)
        idx=len(z)-1
        tmp = z[idx][0]
        idx-=1
        toadd=z[idx][1]
        while idx>=0 and z[idx][0]==tmp:
            toadd = min(toadd,z[idx][1])
            idx-=1
        res.append([c,toadd])
            
    # for c in res:
    #     idxs = cvid[c]
    #         for a in idxs:
    #             if ids[a]
    return res
creators=["a","a"]
ids=["aa","a"]
views=[5,5]
a=mostPopularCreator(creators,ids,views)
print("a,",a)