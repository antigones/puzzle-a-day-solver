class CalendarBoard:

    day_month_to_idx = {
        'jan':0,
        'feb':1,
        'mar':2,
        'apr':3,
        'may':4,
        'jun':5,
        'jul':6,
        'aug':7,
        'sep':8,
        'oct':9,
        'nov':10,
        'dec':11,
        '1':12,
        '2':13,
        '3':14,
        '4':15,
        '5':16,
        '6':17,
        '7':18,

        '8':19,
        '9':20,
        '10':21,
        '11':22,
        '12':23,
        '13':24,
        '14':25,

        '15':26,
        '16':27,
        '17':28,
        '18':29,
        '19':30,
        '20':31,
        '21':32,

        '22':33,
        '23':34,
        '24':35,
        '25':36,
        '26':37,
        '27':38,
        '28':39,

        '29':40,
        '30':41,
        '31':42,
    }

    point_to_idx = {
        (0,0):0,
        (0,1):1,
        (0,2):2,
        (0,3):3,
        (0,4):4,
        (0,5):5,

        (1,0):6,
        (1,1):7,
        (1,2):8,
        (1,3):9,
        (1,4):10,
        (1,5):11,

        (2,0):12,
        (2,1):13,
        (2,2):14,
        (2,3):15,
        (2,4):16,
        (2,5):17,
        (2,6):18,

        (3,0):19,
        (3,1):20,
        (3,2):21,
        (3,3):22,
        (3,4):23,
        (3,5):24,
        (3,6):25,

        (4,0):26,
        (4,1):27,
        (4,2):28,
        (4,3):29,
        (4,4):30,
        (4,5):31,
        (4,6):32,

        (5,0):33,
        (5,1):34,
        (5,2):35,
        (5,3):36,
        (5,4):37,
        (5,5):38,
        (5,6):39,

        (6,0):40,
        (6,1):41,
        (6,2):42,
        }
    
    idx_to_point = {value: key for key, value in point_to_idx.items()}

    def __init__(self, month, day):
        self.month = month
        self.day = day
        self.month_idx = self.day_month_to_idx[month]
        self.day_idx = self.day_month_to_idx[day]
        self.board = self.get_board(month_idx=self.month_idx,day_idx=self.day_idx)
    
    def get_board(self,month_idx, day_idx):

        board = [
                ['x','x','x','x','x','x','w'],
                ['x','x','x','x','x','x','w'],
                ['x','x','x','x','x','x','x'],
                ['x','x','x','x','x','x','x'],
                ['x','x','x','x','x','x','x'],
                ['x','x','x','x','x','x','x'],
                ['x','x','x','w','w','w','w'],
                ]
        month_point_x,month_point_y = self.idx_to_point[month_idx]
        day_point_x,day_point_y = self.idx_to_point[day_idx]
        board[month_point_x][month_point_y] = '!'
        board[day_point_x][day_point_y] = '!'
        return board

    def get_pretty_board(self):
        board = [
                ['x','x','x','x','x','x','🔲'],
                ['x','x','x','x','x','x','🔲'],
                ['x','x','x','x','x','x','x'],
                ['x','x','x','x','x','x','x'],
                ['x','x','x','x','x','x','x'],
                ['x','x','x','x','x','x','x'],
                ['x','x','x','🔲','🔲','🔲','🔲'],
                ]
        month_point_x,month_point_y = self.idx_to_point[self.month_idx]
        day_point_x,day_point_y = self.idx_to_point[self.day_idx]
        board[month_point_x][month_point_y] = '⭕'
        board[day_point_x][day_point_y] = '⭕'
        return board