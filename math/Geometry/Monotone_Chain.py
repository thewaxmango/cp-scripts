# convex hull

from dataclasses import dataclass

@dataclass 
class MCPt:
    x: float = 0
    y: float = 0
    
class Monotone_Chain:
    @staticmethod
    def orientation(a: MCPt, b: MCPt, c: MCPt) -> int:
        v: float = a.x*(b.y-c.y)+b.x*(c.y-a.y)+c.x*(a.y-b.y)
        if v < 0: 
            return -1
        if v > 0:
            return 1
        return 0
    
    @staticmethod
    def cw(a: MCPt, b: MCPt, c: MCPt, include_collinear: bool) -> bool:
        o: int = Monotone_Chain.orientation(a, b, c)
        return o < 0 or (include_collinear and o == 0)
    
    @staticmethod
    def ccw(a: MCPt, b: MCPt, c: MCPt, include_collinear: bool) -> bool:
        o: int = Monotone_Chain.orientation(a, b, c)
        return o > 0 or (include_collinear and o == 0)
    
    @staticmethod
    def convex_hull(a: list[MCPt], include_collinear: bool = False) -> list[MCPt]:
        if len(a) == 1:
            return a
        a.sort(key=lambda p: (p.x, p.y))
        
        p1: MCPt = a[0]
        p2: MCPt = a[-1]
        
        up: list[MCPt] = []
        down: list[MCPt] = []
        up.append(p1)
        down.append(p2)
        
        for i in range(1, len(a)):
            if i == len(a) - 1 or Monotone_Chain.cw(p1, a[i], p2, include_collinear):
                while len(up) >= 2 and not Monotone_Chain.cw(up[-2], up[-1], a[i], include_collinear):
                    up.pop()
                up.append(a[i])
            if i == len(a) - 1 or Monotone_Chain.ccw(p1, a[i], p2, include_collinear):
                while len(down) >= 2 and not Monotone_Chain.ccw(down[-2], down[-1], a[i], include_collinear):
                    down.pop()
                down.append(a[i])
        
        if include_collinear and len(up) == len(a):
            return a[::-1]
        
        a = []
        for i in range(0, len(up)):
            a.append(up[i])
        for i in range(len(down) - 2, 0, -1):
            a.append(down[i])
        return a