class SquareGame:
    @staticmethod
    def make_board(self,square_count):
        # extra rows
        # cordinates
        line = square_count-1
        range_limit=((2*square_count)-1)*square_count
        ls = [i for i in range(range_limit)]
        ls1=[ls[(line*i):(i+1)*line]for i in range(4)]
        for i in range(len(ls1)):
            for j in range(len(ls1[i])):
                if j%2 == 0:
                    ls1[i][j] = '.'

    def draw_line(self):
        pass

    def print_board(self):
        pass

    def write_letter(self):
        pass
