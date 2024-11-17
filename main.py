
from pad_solver.piece import Piece
from pad_solver.puzzle_a_day_solver import PuzzleADaySolver
# 8 pieces, 43 cells
# 43*8 pentominoes to check (without reflections)

p0 = Piece('a', [(0,0),(1,0),(0,1),(1,1),(0,2),(1,2)], '🟦')
p1 = Piece('b', [(0,0),(0,1),(0,2),(1,2),(1,3)],'🟪')
p2 = Piece('c', [(0,0),(1,0),(0,1),(1,1),(0,2)],'🟧')
p3 = Piece('d', [(0,0),(1,0),(0,1),(0,2),(1,2)],'🟩')
p4 = Piece('e', [(0,0),(0,1),(0,2),(0,3),(1,3)],'🟨')
p5 = Piece('f', [(0,0),(1,0),(2,0),(0,1),(0,2)],'🟫')
p6 = Piece('g', [(0,0),(0,1),(1,1),(2,1),(2,2)],'⬛')
p7 = Piece('h', [(0,0),(0,1),(1,1),(0,2),(0,3)],'⬜')

available_pieces = [p0,p1,p2,p3,p4,p5,p6,p7]


month = 'jan'
day = '15'
solver = PuzzleADaySolver(month=month, day=day, available_pieces=available_pieces)
found, solution = solver.solve()
if found:
    print('FOUND')
    print(solution)
else:
    print('not found')

"""
    board = get_pretty_board(month_idx=month_idx,day_idx=day_idx)

    for r in rows:
        for i,n in enumerate(matrix[r].nodes):
            if n == 1:
                x,y = i_to_p[i]
                board[x][y] = matrix[r].emoji
    for b in board:
        print("".join(b),end='\n')
"""