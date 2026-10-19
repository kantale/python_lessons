
'''
NC_003070.9     +       24452   24541
NC_003070.9     +       24656   24751
NC_003070.9     +       24963   25040
NC_003070.9     +       25744   25824
NC_003070.9     +       25998   26080
NC_003070.9     +       26204   26291
NC_003070.9     +       26453   26542
NC_003070.9     +       26777   26861
NC_003070.9     +       27013   27098
'''

t = set()
with open('splice_sites.tsv') as f:
    for l in f:
        ls = l.strip()
        a,b,c,d  = ls.split('\t')
        c = int(c)
        d = int(d)

        found = None
        for i in range(c,d+1):
            if i in t:
                found  = i
                break
        else:
            
            t.add(i)



