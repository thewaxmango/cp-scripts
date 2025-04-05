# Order Statistic Tree based on Red-Black
# Supports duplicate elements

from dataclasses import dataclass
@dataclass(repr=False, eq=False, slots=True)
class OST_Node:
    key   : object                   # Optional[T]   : NIL is unique None
    size  : int               = 1    # int
    color : bool              = True # boolean       : Black -> False; Red -> True
    par   : 'OST_Node | None' = None # Optional[int]
    left  : 'OST_Node | None' = None # Optional[int]
    right : 'OST_Node | None' = None # Optional[int]
    def __bool__(self):
        return self.key is not None
    def __eq__(self, other):
        return self is other

# Uses red-black tree structure with order statistic property
class Order_Statistic_Tree:
    def __init__(self) -> None:
        self.__nil  : OST_Node = OST_Node(None, 0, False)
        self.__root : OST_Node = self.__nil
        self.__nil.left = self.__nil
        self.__nil.right = self.__nil
        self.__nil.par = self.__nil

    # T -> bool
    # returns whether key exists
    def __contains__(self, v) -> bool:
        return self.__find(v) is not self.__nil
    
    # int -> Optional[T]
    # returns the 0-indexed ith smallest element
    def __getitem__(self, i: int) -> object | None:
        return self.select(i)
    
    # () -> int
    # returns number of keys in tree
    def __len__(self) -> int:
        return self.__root.size

    # () -> <Iterator[T]>
    # returns keys in order
    def __iter__(self):
        for v in self.__iterator(self.__root):
            yield v 

    # T -> None
    def insert(self, v) -> None:
        z = OST_Node(v)
        y = self.__nil
        x = self.__root
        
        # Find insertion position and update sizes
        while x is not self.__nil:
            x.size += 1  # Update size directly during traversal
            y = x
            if v < x.key:
                x = x.left
            else:
                x = x.right
                
        z.par = y
        if y is self.__nil:
            self.__root = z
        else:
            if z.key < y.key:
                y.left = z
            else:
                y.right = z
                
        z.left = self.__nil
        z.right = self.__nil
        
        self.__insert_repair(z)
        self.__root.color = False  # Root is always black

    # T -> bool
    # deletes one copy of the key
    # returns whether the key was found
    def erase(self, v) -> bool:
        # find element
        y = self.__find(v)
        if y is self.__nil:
            return False
        
        # find successor and swap
        z = y
        if y.left and y.right:
            z = self.__min_node(y.right)
            y.key = z.key
        
        # decrement sizes
        w = z.par
        while w is not self.__nil:
            w.size -= 1
            w = w.par
        
        # guaranteed z has zero or one children
        w = z.left if z.left else z.right
        if not z.par:
            self.__root = w
            w.par = self.__nil
            w.color = False
        else:
            if z is z.par.left:
                z.par.left = w
            else:
                z.par.right = w
            w.par = z.par
            
            # fix red-black properties
            if not z.color:
                if w.color:
                    w.color = False
                else:
                    self.__delete_repair(w)  # double black
            self.__nil.par = self.__nil

        return True
    
    # int -> Optional[T]
    # returns the 0-indexed i-th smallest key
    def select(self, i: int) -> object | None:
        if i < 0 or not self.__root or i >= self.__root.size:
            return None
            
        x = self.__root
        while x is not self.__nil:
            left_size = x.left.size
            if left_size == i:
                return x.key
            elif left_size > i:
                x = x.left
            else:
                i -= left_size + 1     
                x = x.right
    
    # T -> int
    # returns how many keys are strictly smaller
    def rank(self, v) -> int:
        x = self.__root
        total = 0
        while x is not self.__nil:
            if x.key < v:
                total += x.left.size + 1
                x = x.right
            else:
                x = x.left
        return total

    # () -> Optional[T]
    # returns the smallest key
    def min(self):
        return self.__min_node(self.__root).key
    
    # () -> Optional[T]
    # returns the largest key
    def max(self):
        return self.__max_node(self.__root).key

    # T -> Node
    # returns node with value T, or nil if not found
    def __find(self, v) -> OST_Node:
        x = self.__root
        while x is not self.__nil:
            if x.key == v:
                break
            x = x.right if x.key < v else x.left
        return x
    
    # Node -> Node
    # returns node in subtree of x with minimum value
    def __min_node(self, x: OST_Node) -> OST_Node:
        while x.left is not self.__nil:
            x = x.left
        return x
    
    # Node -> Node
    # returns node in subtree of x with maximum value
    def __max_node(self, x: OST_Node) -> OST_Node:
        while x.right is not self.__nil:
            x = x.right
        return x
    
    # Node -> <Iterator[T]>
    # yields keys in sorted order
    def __iterator(self, x: OST_Node):
        if x is self.__nil:
            return
        for v in self.__iterator(x.left):
            yield v
        yield x.key
        for v in self.__iterator(x.right):
            yield v
    
    # Node -> None
    # rotates with x as root
    def __left_rotate(self, x: OST_Node) -> None:
        y = x.right
        
        # Update child relationship
        x.right = y.left
        if y.left:
            y.left.par = x
            
        # Update parent relationship
        y.par = x.par
        if not x.par:
            self.__root = y
        elif x is x.par.left:
            x.par.left = y
        else:
            x.par.right = y
            
        # Set up y as x's parent
        y.left = x
        x.par = y
        
        y.size = x.size
        x.size = x.left.size + x.right.size + 1
        
    # Node -> None
    # rotates with x as root
    def __right_rotate(self, x: OST_Node) -> None:
        y = x.left
        
        # Update child relationship
        x.left = y.right
        if y.right:
            y.right.par = x
            
        # Update parent relationship
        y.par = x.par
        if not x.par:
            self.__root = y
        elif x is x.par.left:
            x.par.left = y
        else:
            x.par.right = y
            
        # Set up y as x's parent
        y.right = x
        x.par = y
        
        # Update sizes - only need to update x first then y
        y.size = x.size
        x.size = x.left.size + x.right.size + 1
        
    # Node -> None
    # repairs red-black mismatches following insertion
    def __insert_repair(self, z: OST_Node) -> None:
        while z.par.color:  # While parent is red
            if z.par is z.par.par.left:  # Parent is left child
                y = z.par.par.right  # Uncle
                if y.color:  # Uncle is red
                    z.par.color = False
                    y.color = False
                    z.par.par.color = True
                    z = z.par.par
                else:  # Uncle is black
                    if z is z.par.right:  # Inside case
                        z = z.par
                        self.__left_rotate(z)
                    # Outside case
                    z.par.color = False
                    z.par.par.color = True
                    self.__right_rotate(z.par.par)
            else:  # Parent is right child
                y = z.par.par.left  # Uncle
                if y.color:  # Uncle is red
                    z.par.color = False
                    y.color = False
                    z.par.par.color = True
                    z = z.par.par
                else:  # Uncle is black
                    if z is z.par.left:  # Inside case
                        z = z.par
                        self.__right_rotate(z)
                    # Outside case
                    z.par.color = False
                    z.par.par.color = True
                    self.__left_rotate(z.par.par)
                    
            if z is self.__root:
                break
    
    # Node -> None
    # repairs red-black mismatches following deletion
    # input node is the double black
    def __delete_repair(self, x: OST_Node) -> None:
        while x is not self.__root and not x.color:
            if x is x.par.left:  # x is left child
                w = x.par.right  # w is x's sibling
                
                if w.color:  # Case 1: sibling is red
                    w.color = False
                    x.par.color = True
                    self.__left_rotate(x.par)
                    w = x.par.right
                
                if not w.left.color and not w.right.color:  # Case 2: both children black
                    w.color = True
                    x = x.par
                else:  
                    if not w.right.color:  # Case 3: right child black
                        w.left.color = False
                        w.color = True
                        self.__right_rotate(w)
                        w = x.par.right
                    
                    # Case 4: right child red
                    w.color = x.par.color
                    x.par.color = False
                    w.right.color = False
                    self.__left_rotate(x.par)
                    x = self.__root
            else:  # x is right child
                w = x.par.left  # w is x's sibling
                
                if w.color:  # Case 1: sibling is red
                    w.color = False
                    x.par.color = True
                    self.__right_rotate(x.par)
                    w = x.par.left
                
                if not w.left.color and not w.right.color:  # Case 2: both children black
                    w.color = True
                    x = x.par
                else:
                    if not w.left.color:  # Case 3: left child black
                        w.right.color = False
                        w.color = True
                        self.__left_rotate(w)
                        w = x.par.left
                    
                    # Case 4: left child red
                    w.color = x.par.color
                    x.par.color = False
                    w.left.color = False
                    self.__right_rotate(x.par)
                    x = self.__root
                    
        x.color = False
