from sys import stdin, stdout

def I(): return stdin.readline().strip(" \r\n")
def II(): return int(I())
def IL(): return I().split()
def ICL(): return list(I())
def IIL(): return list(map(int, IL()))
def IM(): return map(str, IL())
def IIM(): return map(int, IL())
def P(*args,sep=' ',end=''): stdout.write(sep.join([str(s) for s in args]) + end)
def PL(*args,sep=' '): P(*args, sep=sep, end='\n')
def F(): stdout.flush()

def main():
    #for _ in range(II()):
        solve()
  
def solve():
    return

if __name__ == "__main__":
    main()
