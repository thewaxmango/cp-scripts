from sys import stdin, stdout

def I(): return stdin.readline().strip(" \r\n")
def II(): return int(I())
def IL(): return I().split()
def ICL(): return list(I())
def IIL(): return list(map(int, IL()))
def IFL(): return list(map(float, IL()))
def IM(): return map(str, IL())
def IIM(): return map(int, IL())
def IFM(): return map(float, IL())
def ICLM(): return map(int, ICL())
def P(*args,sep=' ',end=''): stdout.write(sep.join([str(s) for s in args]) + end)
def PL(*args,sep=' '): P(*args, sep=sep, end='\n')
def PA(arg,end='\n'): P(*arg, sep='\n', end=end)
def F(): stdout.flush()
def Y(): PL("YES")
def N(): PL("NO")

def main():
    for _ in range(II()):
	    solve()

def solve():
	pass

main()
