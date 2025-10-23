"""
    Testing Order Statistic Tree implementations
    -> values [-1e9, 1e9]
    -> size [0, 1e6]
    -> operations [0, 1e6]
"""

from Control import OrderStatisticTree
from Order_Statistic_Tree import Order_Statistic_Tree
from random import randint, random, choice
from time import time

def verify(n = 10**6, bound = 10**9):
    # chance to:
    # insert
    # delete
    # select
    # rank
    
    vs = []
    sz = 0
    ostc = OrderStatisticTree()
    ost = Order_Statistic_Tree()
    ct = [0, 0, 0, 0]
    t = [0, 0, 0, 0]
    for _ in range(min(n, 10**6)):
        z = random()
        if z < 0.4 or sz == 0:
            v = randint(-bound, bound)
            vs.append(v)
            # print(f"I {v}")
            a = time()
            ostc.insert(v)
            ct[0] += time() - a
            a = time()
            ost.insert(v)
            t[0] += time() - a
            sz += 1
            
        elif z < 0.65:
            if random() < 0.8:
                v = choice(vs)
            else:
                v = randint(-bound, bound)
            # print(f"D {v}")
            a = time()
            j = ostc.delete(v)
            ct[1] += time() - a
            a = time()
            k = ost.erase(v)
            t[1] += time() - a
            # print(f"  {j} {k}")
            sz -= 1
            
        elif z < 0.85:
            if random() < 0.8:
                i = randint(0, sz - 1)
            else:
                i = randint(-bound, bound)
            
            a = time()
            j = ostc.select(i)
            ct[2] += time() - a
            a = time()
            k = ost.select(i)
            t[2] += time() - a
            if j != k:
                header = '\033[93m'
                print(f"S {i}")
                print(f"{header}  {j} {k}\033[0m", flush=True)
            
        else:
            if random() < 0.8:
                v = choice(vs) * (random() - 0.5) * 6
            else:
                v = randint(-bound, bound)
            a = time()
            j = ostc.rank(v)
            ct[3] += time() - a
            a = time()
            k = ost.rank(v)
            t[3] += time() - a
            if j != k:
                header = '\033[93m'
                print(f"R {i}")
                print(f"{header}  {j} {k}\033[0m", flush=True)
    
    print(f'control time: {sum(ct):.4f}\n', " | ".join(['%.4f' % f for f in ct]))
    print(f'testing time: {sum(t):.4f}\n', " | ".join(['%.4f' % f for f in t]))
    
    i = iter(ost)
    print(next(i))
        
def compare():
    pass

if __name__ == "__main__":
    verify(10**6, 10**9)