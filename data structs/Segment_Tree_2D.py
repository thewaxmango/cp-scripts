import random, time

# IMPLEMENTATION FOR RANGE SUM

def build(in_arr):
    cols, rows = len(in_arr[0]), len(in_arr)
    seg_arr = [[None]*cols*2 for _ in range(rows*2)]
    
    # insert initial values
    for ri, rf in enumerate(range(rows, rows*2)):
        for ci, cf in enumerate(range(cols, cols*2)):
            seg_arr[rf][cf] = in_arr[ri][ci]

    # propagate horizontally
    for r in range(rows, 2*rows):
        for c in range(cols-1, 0, -1):
            seg_arr[r][c] = seg_arr[r][c<<1] + seg_arr[r][c<<1|1]

    # propagate vertically
    for c in range(cols*2-1, 0, -1):
        for r in range(rows-1, 0, -1):
            seg_arr[r][c] = seg_arr[r<<1][c] + seg_arr[r<<1|1][c]

    return seg_arr

def modify(seg_arr, row, col, value):
    cols, rows = len(seg_arr[0])//2, len(seg_arr)//2
    col, row = col + cols, row + rows
    seg_arr[row][col] = value

    # propagate horizontally
    c = col
    while c > 1:
        seg_arr[row][c>>1] = seg_arr[row][c] + seg_arr[row][c^1]
        c >>= 1

    # propagate vertically
    while col > 0:
        r = row
        while r > 1:
            seg_arr[r>>1][col] = seg_arr[r][col] + seg_arr[r^1][col]
            r >>= 1
        col >>= 1

def query(seg_arr, row_l, row_r, col_l, col_r):
    cols, rows = len(seg_arr[0])//2, len(seg_arr)//2
    col_l, col_r, row_l, row_r = col_l + cols, col_r + cols, row_l + rows, row_r + rows
    out = 0

    while col_l < col_r:
        if (col_l&1):
            r_l, r_r = row_l, row_r
            while r_l < r_r:
                if (r_l&1):
                    out += seg_arr[r_l][col_l]
                    r_l += 1
                if (r_r&1):
                    r_r -= 1
                    out += seg_arr[r_r][col_l]
                r_l >>= 1
                r_r >>= 1
            col_l += 1
        if (col_r&1):
            col_r -= 1
            r_l, r_r = row_l, row_r
            while r_l < r_r:
                if (r_l&1):
                    out += seg_arr[r_l][col_r]
                    r_l += 1
                if (r_r&1):
                    r_r -= 1
                    out += seg_arr[r_r][col_r]
                r_l >>= 1
                r_r >>= 1
            
        col_l >>=1
        col_r >>=1
    
    return out


def main():
    cols, rows = 10**3, 10**3
    in_arr = [[random.randint(1, 3) for _ in range(cols)] for __ in range(rows)]

    t = time.time()
    seg_arr = build(in_arr)
    print("build time:", time.time()-t)
    # print(*seg_arr, '', sep='\n')
    t = time.time()
    modify(seg_arr, 0, 0, 5)
    print("modify time:", time.time()-t)
    # print(*seg_arr, '', sep='\n')
    t = time.time()
    print(query(seg_arr, 123, 882, 94, 399))
    print("query time:", time.time()-t)

if __name__ == "__main__":
    main()