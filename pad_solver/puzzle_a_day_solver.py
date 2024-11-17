import pad_solver.piece_utils as pu
from pad_solver.calendar_board import CalendarBoard
from pad_solver.piece import Piece
from pad_solver.row import Row


class PuzzleADaySolver:

    def __init__(self, month, day, available_pieces):
        self.month = month
        self.day = day
        self.available_pieces = available_pieces
        self.calendar_board = CalendarBoard(month=month, day=day)
        self.board = self.calendar_board.board

    def generate_rows(self, pieces:list[Piece]):
        matrix = list()
        board = self.board
        for piece in pieces:
            # consider piece and variations
            for variation in pu.get_all_variations(piece.points):
                for r in range(len(board)):
                    for c in range(len(board[0])):
                        variation_at_position = pu.traslate(variation,(r,c))
                        if self.can_place(variation_at_position):
                            piece_variation_at_position = Piece(piece.name, variation_at_position, piece.emoji)
                            matrix.append(self.piece_to_idx(piece_variation_at_position))
        return matrix
    
    def piece_to_idx(self, piece:Piece):
        col_idxs = list()
        for point in piece.points:
            x,y = point
            col_idxs.append(self.calendar_board.point_to_idx[(x,y)])
        row = list()
        for i in range(43):
            if i in col_idxs:
                row.append(1)
            else:
                row.append(0)
        r = Row(name=piece.name, nodes=row, emoji=piece.emoji)
        return r
    
    def can_place(self, points):
        for point in points:
            x,y = point
            if x > len(self.board[0])-1 or y > len(self.board)-1 or y < 0 or x < 0 or self.board[x][y] != 'x':
                return False
        return True

    def dance_iterative(self,matrix,month_idx,day_idx):
        covered_cols = set()
        available_rows = set(range(len(matrix)))
        chosen_rows = set()

        state = [(covered_cols, available_rows, chosen_rows)]
        
        while state:
            covered_cols, available_rows, chosen_rows = state.pop()
            
            if month_idx not in covered_cols and day_idx not in covered_cols and len(covered_cols) == len(matrix[0].nodes) - 2:
                return True, chosen_rows

            if not available_rows:
                continue

            for rd_row_idx in available_rows:
                # choose a row (place a piece on the board)
                chosen_row = matrix[rd_row_idx]
                
                new_available_rows = available_rows - {rd_row_idx} - {r for r in available_rows if matrix[r] == chosen_row}
                new_covered_cols = covered_cols | {i for i, elm in enumerate(chosen_row.nodes) if elm == 1}

                new_available_rows -= {r for r, row in enumerate(matrix) if r in new_available_rows and any(elm == 1 and i in new_covered_cols for i, elm in enumerate(row.nodes))}
                
                state.append((new_covered_cols, new_available_rows, chosen_rows | {rd_row_idx}))
        return False, None
    

    def solve(self):
        matrix = self.generate_rows(self.available_pieces)
        found, rows = self.dance_iterative(matrix=matrix,month_idx=self.calendar_board.month_idx,day_idx=self.calendar_board.day_idx)
        return found, rows
    
    def solve_and_pretty_print(self):
        board = self.calendar_board.get_pretty_board()
        matrix = self.generate_rows(self.available_pieces)
        found, rows = self.dance_iterative(matrix=matrix,month_idx=self.calendar_board.month_idx,day_idx=self.calendar_board.day_idx)
        if found:
            print('*** SOLUTION ***')
            for r in rows:
                for i,n in enumerate(matrix[r].nodes):
                    if n == 1:
                        x,y = self.calendar_board.idx_to_point[i]
                        board[x][y] = matrix[r].emoji
            for b in board:
                print("".join(b),end='\n')
        else:
            print('not found')

        