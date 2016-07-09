import pickle

def makeDict():
    with open('WORDS.txt','r') as fh:
        d = {}
        for lines in fh:
            w = lines.strip()
            l = ''
            j = list(w)
            j.sort()
            for i in j:
                l += i        
            n = 0
            for i in w:
                n += ord(i)
            if n in d:
                if l in d[n]:
                    d[n][l].append(w)
                else :
                    d[n][l] = [w]
            else :
                d[n] = {l:[w]}
                print n
    pickle.dump( d, open( "dictionary.p", "wb" ) )

def printDict():
    dbase = pickle.load(open( "dictionary.p", "rb" ) )    
    
    
makeDict() 
printDict()



