task = ''
fin = open(f'{task}.in', 'r')
fout = open(f'{task}.out', 'w')

def I(): return fin.readline().strip(" \r\n")
def II(): return int(I())
def IL(): return I().split()
def ICL(): return list(I())
def IIL(): return list(map(int, IL()))
def IM(): return map(str, IL())
def IIM(): return map(int, IL())
def P(*args,sep=' ',end=''): fout.write(sep.join([str(s) for s in args]) + end)
def PL(*args,sep=' '): P(*args, sep=sep, end='\n')

def main():
    #for _ in range(II()):
        solve()

def solve():
    pass 

if __name__ == "__main__":
    main()
    fout.close()
