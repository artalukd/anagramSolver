import cPickle as pickle
def lookUp( w, d):
    w = w.strip()
    l = ''
    j = list(w)
    j.sort()
    n = 0
    for i in j:
        l += i
        n += ord(i)
    if n in d:
        if l in d[n]:
            return d[n][l]
        else :
            return []
    else :
        return []

def fun(w , d, a):
    if len(w) > 0 :
        s = lookUp(w,d)
        for j in s:
            if j not in a:
                if len(j) > 0:
                    a.append(j)
    else:
        return a
    for i in range(len(w)):
        s = fun(w[:i]+w[i+1:], d, a)
    return a


dbase = pickle.load(open( "dictionary.p", "rb" ) )
a = []
while True:
    a = []
    w = input("Enter word within '' (or 'q' to quit) : ")
    if w == 'q':
        break
    else:
        print(fun(w,dbase,a))
        print (len(a))
