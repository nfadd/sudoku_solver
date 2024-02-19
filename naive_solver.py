import sys
import random

def find_num(row, col, num, grid):
    for i in range(9):
        if grid[i][col] == num:
            return False
    
    for i in range(9):
        if grid[row][i] == num:
            return False
        
    row = row - row%3
    col = col - col%3

    for i in range(3):
        for j in range(3):
            if grid[row+i][col+j] == num:
                return False
        
    return True


def solver(grid):
    flag = False
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                flag = True
                row = i
                col = j
                break

    if not flag:
        print('Solution: ')
        for i in grid:
            print(i)
        sys.exit()
    
    for i in range(1,10):
        if find_num(row, col, i, grid):
            grid[row][col] = i

            if solver(grid):
                return True
            else:
                grid[row][col] = 0
    return False


def rand_grid(grids):
    grid = [[0 for i in range(9)] for j in range(9)]

    temp = random.choice(grids)
    temp = ''.join(random.choice(grids).split('\n'))

    count = 0
    for i in range(9):
        for j in range(9):
            grid[i][j] = int(temp[count])
            count += 1
    
    return grid


if __name__ == "__main__":
    if len(sys.argv) > 1:
        level = sys.argv[1]

        levels = ['easy','medium','hard']
        if level not in levels:
            print('Please enter "easy", "medium", or "hard"')
            sys.exit()

        easy, medium, hard = [], [], []

        file = open('test_grids.txt', 'r')
        content = file.read()
        grids = content.split('*')

        for i, l in enumerate(grids):
            if l == 'easy':
                easy.append(grids[i+1])
            elif l == 'medium':
                medium.append(grids[i+1])
            elif l == 'hard':
                hard.append(grids[i+1])

        if level == 'easy':
            grid = rand_grid(easy)
        elif level == 'medium':
            grid = rand_grid(medium)
        elif level == 'hard':
            grid = rand_grid(hard)

        solver(grid)
    else:
        print('Please enter "easy", "medium", or "hard"')

