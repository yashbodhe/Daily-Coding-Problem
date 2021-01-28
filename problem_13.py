def longestSubstringKDistinct(s, k):
    dic=dict()
    q=[]
    maxx,start=0,0
    res=""
    for i in range(len(s)):
        if s[i] in dic:
            if len(q):q.pop(0)
            q.append(s[i])
            dic[s[i]]=i
        elif len(q)<k:
            q.append(s[i])
            dic[s[i]]=i
        else:
            tmp=q.pop(0)
            if i-start>maxx:
                maxx=i-start
                res=s[start:i]
            start=dic[tmp]+1
            del dic[tmp]
            q.append(s[i])
            dic[s[i]]=i
    if len(s)-start>maxx:
        maxx=len(s)-start
        res=s[start:len(s)]
    return res
            
print(longestSubstringKDistinct("abcba",2))
#['deer', 'deal']uytjki