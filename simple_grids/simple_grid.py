import arcade
import  numpy as np
from IPython.display import clear_output

class Grid(arcade.Window):

    def __init__(self, X, Y, rows, columns, title):
        self.x = X
        self.y = Y
        self.title = title
        self.columns = columns
        self.rows = rows
        self.grid = np.zeros((self.rows,self.columns))        
        self.column_x, self.row_y = self.get_column_and_row_size(self.rows, self.columns) 
        self.grid_coords = self.get_grid_coords(self.rows, self.columns)
        self.current_coordinate = "No current coordinate"
        super().__init__(X, Y, title)

        arcade.set_background_color((0,0,0))

    def on_draw(self):
        
        self.clear()
        for r_ind, row in enumerate(self.grid_coords):
            for c_ind, column in enumerate(row):
                try:
                    if self.grid[r_ind][c_ind] == 1:
                        arcade.draw_lrtb_rectangle_filled(column[0],column[1],column[2],column[3], arcade.color.BLUE)
                    arcade.draw_lrtb_rectangle_outline(column[0],column[1],column[2],column[3], arcade.csscolor.RED)
                    arcade.draw_text(self.current_coordinate, self.x // (1/3 * self.x), self.y - (self.row_y//2), arcade.color.WHITE, 12)
                except:
                    pass
    
    def on_mouse_press(self, x, y, button, key_modifiers):
        
        col = int(x) // self.column_x
        row = int(y) // self.row_y
        self.current_coordinate = f"Current Coordinate: {col}, {row}"
        
        if int(y) < self.y and int(x) < self.x:
            if self.grid[row][col] == 0:
                self.grid[row][col] = 1
            else:
                self.grid[row][col] = 0
                
    def get_grid_coords(self, rows, columns):
        column_x = self.column_x
        row_y = self.row_y
        init_x_points = range(0, X, column_x)
        init_y_points = range(0, Y, row_y)
        grid = []
        if init_x_points[-1] + column_x > X:
            init_x_points = init_x_points[:-1]
        if init_y_points[-1] + row_y > Y:
            init_y_points = init_y_points[:-1]
        first_row = np.array([[x, x+column_x, row_y, 0] for x in init_x_points])
        grid.append(first_row)

        for row in range(1,rows):
            new_row = first_row.copy()
            new_row[:,2] += row_y * row
            new_row[:,3] += row_y * row
            grid.append(new_row)

        return np.array(grid)
    def get_column_and_row_size(self,rows, columns):
        assert rows < Y and columns < X
        assert Y/rows > 3 and X/columns>3

        column_x = X // columns
        row_y = Y // rows

        return column_x, row_y

def main(X, Y, rows, columns, TITLE = 'Simple Grid'):
    game = Grid(X, Y, rows, columns, TITLE)
    arcade.run()

if __name__ == '__main__':
    start = False    
    while start is False:
        X = int(input('Width of the screen :: '))
        Y = int(input('Height of the screen :: '))
        rows = int(input('ROWS :: '))
        columns = int(input('COLUMNS :: '))
        try:
            assert Y < 1080 and X < 1920
            assert rows < Y and columns < X
            assert Y/rows > 3 and X/columns>3
            start = True
            break
        except:
            print("Your numbers are wrong I don't know what to tell you")
    
    
    main(X, Y, rows, columns)