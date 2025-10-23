# Convex hull

from dataclasses import dataclass
from functools import cmp_to_key

@dataclass 
class GSPt:
    x: float = 0
    y: float = 0

class Graham_Scan:
    @staticmethod
    def orientation(a: GSPt, b: GSPt, c: GSPt) -> int:
        v: float = a.x*(b.y-c.y)+b.x*(c.y-a.y)+c.x*(a.y-b.y)
        if v < 0: 
            return -1
        if v > 0:
            return 1
        return 0
    
    @staticmethod
    def cw(a: GSPt, b: GSPt, c: GSPt, include_collinear: bool) -> bool:
        o: int = Graham_Scan.orientation(a, b, c)
        return o < 0 or (include_collinear and o == 0)
    
    @staticmethod
    def collinear(a: GSPt, b: GSPt, c: GSPt) -> bool:
        return Graham_Scan.orientation(a, b, c) == 0
    
    @staticmethod
    def convex_hull(a: list[GSPt], include_collinear: bool = False) -> list[GSPt]:
        p0: GSPt = min(a, key=lambda p: (p.y, p.x))
        def _cmp(a, b):
            o: int = Graham_Scan.orientation(p0, a, b)
            if o == 0:
                return (p0.x-a.x)*(p0.x-a.x) + (p0.y-a.y)*(p0.y-a.y) < (p0.x-b.x)*(p0.x-b.x) + (p0.y-b.y)*(p0.y-b.y)
            return o < 0
        a.sort(key=cmp_to_key(_cmp))
        
        if include_collinear:
            i: int = len(a) - 1
            while i >= 0 and Graham_Scan.collinear(p0, a[i], a[-1]):
                i -= 1
            a[i+1:-1] = a[i+1:-1][::-1]
            
        st: list[GSPt] = []
        for i in range(len(a)):
            while len(st) > 1 and not Graham_Scan.cw(st[-2], st[-1], a[i], include_collinear):
                st.pop()
            st.append(a[i])
        
        if not include_collinear and len(st) == 2 and st[0] == st[1]:
            st.pop()
            
        return st