import copy

puzzle = [
            [0, 0, 6, 1, 0, 0, 0, 0, 8],
            [0, 8, 0, 0, 9, 0, 0, 3, 0],
            [2, 0, 0, 0, 0, 5, 4, 0, 0],
            [4, 0, 0, 0, 0, 1, 8, 0, 0],
            [0, 3, 0, 0, 7, 0, 0, 4, 0],
            [0, 0, 7, 9, 0, 0, 0, 0, 3],
            [0, 0, 8, 4, 0, 0, 0, 0, 6],
            [0, 2, 0, 0, 5, 0, 0, 8, 0],
            [1, 0, 0, 0, 0, 2, 5, 0, 0]
        ]

ps = [[[] for _ in range(9)] for _ in range(9)]

def count_zeros(arr):
    count = 0
    for row in arr:
        count += row.count(0)
    return count

def num_possible(arr, poss):
    for r_i, r in enumerate(arr):
        v = [1,2,3,4,5,6,7,8,9]
        for e in r:
            if e != 0:
                if e in v: v.remove(e)
       
        for c_i, el in enumerate(r):
            if el == 0:
                v2 = [1,2,3,4,5,6,7,8,9]
                for j in range(9):
                    c = arr[j][c_i]
                    if c in v2: v2.remove(c)
               
                v3 = [1,2,3,4,5,6,7,8,9]
                bsr = (r_i // 3) * 3
                bsc = (c_i // 3) * 3
                for br in range(bsr, bsr + 3):
                    for bc in range(bsc, bsc + 3):
                        val = arr[br][bc]
                        if val != 0 and val in v3: v3.remove(val)
               
                final_poss = [k for k in v if k in v2 and k in v3]
                poss[r_i][c_i] = final_poss

def naked_singles(arr, poss):
    for r in range(9):
        for c in range(9):
            if arr[r][c] == 0 and len(poss[r][c]) == 1: 
                num = poss[r][c][0]
                arr[r][c] = num
                return True
    return False

def hidden_singles_rows_cols(arr, poss):
    for r in range(9):
        for num in range(1, 10):
            possible_cols = []
            for c in range(9):
                if arr[r][c] == 0 and num in poss[r][c]: possible_cols.append(c)
            if len(possible_cols) == 1:
                col = possible_cols[0]
                arr[r][col] = num
                return True
    
    for c in range(9):
        for num in range(1, 10):
            possible_rows = []
            for r in range(9):
                if arr[r][c] == 0 and num in poss[r][c]: possible_rows.append(r)
            if len(possible_rows) == 1:
                row = possible_rows[0]
                arr[row][c] = num
                return True
    return False

def singles_method(arr, poss):
    for c1 in [0,3,6]:
        for c2 in [0,3,6]:
            for num in range(1, 10):
                cwN = []
                for r in range(c1, c1+3):
                    for c in range(c2, c2+3):
                        if arr[r][c] == 0 and num in poss[r][c]: cwN.append((r, c))
                if len(cwN) == 1:
                    row, col = cwN[0]
                    arr[row][col] = num
                    return True
    return False

def constraint_propagation(arr):
    poss = [[[] for _ in range(9)] for _ in range(9)]
    while True:
        num_possible(arr, poss)
        if naked_singles(arr, poss): continue
        if singles_method(arr, poss): continue
        if hidden_singles_rows_cols(arr, poss): continue
        break 
    return poss

def is_valid(arr):
    poss = [[[] for _ in range(9)] for _ in range(9)]
    num_possible(arr, poss)
    for r in range(9):
        for c in range(9):
            if arr[r][c] == 0 and len(poss[r][c]) == 0: return False
    return True

def find_best_guess_cell(arr, poss):
    best_cell = None
    min_possibilities = 10
    for r in range(9):
        for c in range(9):
            if arr[r][c] == 0:
                num_poss = len(poss[r][c])
                if num_poss < min_possibilities: min_possibilities = num_poss; best_cell = (r, c)
    return best_cell

def solve_with_backtracking(arr, depth=0):
    print("  " * depth + f"Depth {depth}: {count_zeros(arr)} zeros left")
    poss = constraint_propagation(arr)
    if count_zeros(arr) == 0:
        print("  " * depth + "SOLVED!")
        return True
    if not is_valid(arr):
        print("  " * depth + "Invalid state - backtracking")
        return False
    guess_cell = find_best_guess_cell(arr, poss)
    if not guess_cell:
        return False
    
    r, c = guess_cell
    possibilities = poss[r][c]
    
    print("  " * depth + f"Guessing at ({r},{c}), options: {possibilities}")
    
    for num in possibilities:
        print("  " * depth + f"Trying {num} at ({r},{c})")
        
        arr_copy = copy.deepcopy(arr)
        arr_copy[r][c] = num
        
        if solve_with_backtracking(arr_copy, depth + 1):
            for i in range(9):
                for j in range(9):
                    arr[i][j] = arr_copy[i][j]
            return True
    
    print("  " * depth + "All guesses failed - backtracking")
    return False

initial_zeros = count_zeros(puzzle)
print(f"Initial puzzle: {initial_zeros} zeros")
for row in puzzle:
    print(row)

print("\n=== SOLVING ===")
if solve_with_backtracking(puzzle):
    print("\n solved")
else:
    print("\n no solution")

print("\nFinal puzzle:")
for row in puzzle:
    print(row)
