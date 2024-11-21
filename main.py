
from pad_solver.piece import Piece
from pad_solver.puzzle_a_day_solver import PuzzleADaySolver

# 8 pieces, 43 cells
# 43*8 pentominoes to check (without reflections)

month = 'jan'
day = '14'
solver = PuzzleADaySolver(month=month, day=day)
solver.solve_and_pretty_print()