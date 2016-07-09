import pickle

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
            return "Not found!"
    else :
        return "Not found!"


dbase = pickle.load(open( "dictionary.p", "rb" ) )    
while True:
    w = input("Enter word within '' (or 'q' to quit) : ")
    if w == 'q':
        break
    else:
        print lookUp(w , dbase)
