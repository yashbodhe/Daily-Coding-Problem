def get_same_prefix_query(query, pre):
    res = list()
    for q in query:
        if len(pre)<=len(q) and pre==q[:len(pre)]:
            res.append(q)
    return res


print(get_same_prefix_query(["dog", "deer", "deal"],"de"))
#['deer', 'deal']